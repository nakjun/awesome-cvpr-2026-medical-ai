#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a GitHub-style CVPR 2026 medical AI paper catalog."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


PAGE_URL = "https://cvpr.thecvf.com/virtual/2026/papers.html"
PAPERS_JSON_URL = "https://cvpr.thecvf.com/static/virtual/data/cvpr-2026-orals-posters.json"
ABSTRACTS_JSON_URL = "https://cvpr.thecvf.com/static/virtual/data/cvpr-2026-abstracts.json"
BASE_URL = "https://cvpr.thecvf.com"
USER_AGENT = "Mozilla/5.0 (compatible; CVPR2026MedicalAICatalog/1.0)"

README_PATH = Path("README.md")
OUT_DIR = Path("medical_ai_catalog")
OUT_JSON = OUT_DIR / "cvpr2026_medical_ai_papers.json"
OUT_CSV = OUT_DIR / "cvpr2026_medical_ai_papers.csv"
OUT_MODALITY_INDEX = OUT_DIR / "modality_index.md"

EXTERNAL_LINK_LABELS = {
    "paper_url": "Paper",
    "github_url": "GitHub",
    "code_url": "Code",
    "project_url": "Project",
    "demo_url": "Demo",
    "video_url": "Video",
    "arxiv_url": "arXiv",
    "slides_url": "Slides",
    "source_url": "Source",
}


MODALITY_RULES: dict[str, list[str]] = {
    "Medical AI / General": [
        r"\bmedical\b",
        r"\bbiomedical\b",
        r"\bclinical\b",
        r"\bclinician\b",
        r"\bhealthcare\b",
        r"\bradiology\b",
        r"\bradiologist\b",
        r"\bpatient\b",
        r"\bpatholog(?:y|ical|ist)\b",
    ],
    "X-Ray / Radiography": [
        r"\bx[- ]?ray\b",
        r"\bxray\b",
        r"\bradiograph(?:y|ic)?\b",
        r"\bchest x[- ]?ray\b",
        r"\bcxr\b",
    ],
    "Mammography / Breast": [
        r"\bmammograph(?:y|ic)?\b",
        r"\bmammogram(?:s)?\b",
        r"\bbreast\b",
        r"\bbi[- ]?rads\b",
    ],
    "Ultrasound / Sonography": [
        r"\bultrasound\b",
        r"\bsonograph(?:y|ic)?\b",
        r"\bechocardiograph(?:y|ic)?\b",
    ],
    "MRI / MR": [
        r"\bmri\b",
        r"\bmagnetic resonance\b",
        r"\bmr image\b",
        r"\bmr imaging\b",
    ],
    "CT / Tomography": [
        r"\bct\b",
        r"\bcomputed tomography\b",
        r"\btomograph(?:y|ic)?\b",
        r"\bcbct\b",
        r"\bcone[- ]beam\b",
    ],
    "PET / Nuclear Medicine": [
        r"\bpet\b",
        r"\bpositron emission\b",
        r"\bspect\b",
    ],
    "OCT / Ophthalmology / Retina": [
        r"\boct\b",
        r"\boptical coherence tomography\b",
        r"\bfundus\b",
        r"\bretina(?:l)?\b",
        r"\bophthalmolog(?:y|ic)?\b",
    ],
    "Pathology / Microscopy / Cells": [
        r"\bhistopatholog(?:y|ical)?\b",
        r"\bpathology\b",
        r"\bwhole[- ]slide\b",
        r"\bwsi\b",
        r"\bmicroscop(?:y|ic)?\b",
        r"\bcell microscopy\b",
        r"\bcytolog(?:y|ical)?\b",
        r"\bstain(?:ing)?\b",
    ],
    "Dermatology / Skin": [
        r"\bdermoscop(?:y|ic)?\b",
        r"\bdermatolog(?:y|ic)?\b",
        r"\bmelanoma\b",
        r"\bskin lesion\b",
        r"\bisic\b",
    ],
    "Endoscopy / Colonoscopy / Polyp": [
        r"\bendoscop(?:y|ic)?\b",
        r"\bcolonoscopy\b",
        r"\bpolyp(?:s)?\b",
        r"\bgastrointestinal\b",
    ],
    "Surgery / Medical Video": [
        r"\bsurgical\b",
        r"\blaparoscop(?:y|ic)?\b",
        r"\boperative\b",
        r"\bmedical video\b",
    ],
    "3D / Volumetric Medical Imaging": [
        r"\b3d medical\b",
        r"\bmedical volume\b",
        r"\bvolumetric medical\b",
        r"\bmulti[- ]organ\b",
        r"\borgan segmentation\b",
    ],
}


EXCLUSION_PATTERNS = [
    r"\bprohibited item\b",
    r"\bcontraband\b",
    r"\bsecurity screening\b",
    r"\bblack[- ]hole\b",
    r"\bhuman pose prediction\b",
    r"\battention surgery\b",
    r"\bspectral scalpel\b",
]


DISEASE_RULES: dict[str, list[str]] = {
    "Cancer / Tumor / Lesion": [
        r"\bcancer\b",
        r"\btumou?r\b",
        r"\blesion(?:s)?\b",
        r"\bmalignan(?:t|cy)\b",
        r"\bneoplasm\b",
        r"\bcarcinoma\b",
    ],
    "Organs / Anatomy": [
        r"\bbrain\b",
        r"\blung\b",
        r"\bliver\b",
        r"\bkidney\b",
        r"\bcardiac\b",
        r"\bheart\b",
        r"\bprostate\b",
        r"\bpancrea(?:s|tic)\b",
        r"\babdominal\b",
        r"\banatom(?:y|ical)\b",
    ],
}


TASK_RULES: dict[str, list[str]] = {
    "Segmentation": [r"\bsegmentation\b", r"\bsegment\b", r"\bmask\b"],
    "Detection / Diagnosis": [r"\bdetection\b", r"\bdiagnos(?:is|tic|e)\b", r"\banomaly detection\b"],
    "Registration": [r"\bregistration\b", r"\bdiffeomorphism\b"],
    "Restoration / Reconstruction": [r"\brestoration\b", r"\breconstruction\b", r"\bdenois(?:e|ing)\b"],
    "Medical VLM / VQA / Reasoning": [
        r"\bmedical vqa\b",
        r"\bvisual question answering\b",
        r"\bvision[- ]language\b",
        r"\bmedical reasoning\b",
        r"\bmultimodal reasoning\b",
        r"\bmedical report\b",
    ],
    "Foundation / Adaptation": [
        r"\bfoundation model\b",
        r"\bpre[- ]?training\b",
        r"\bfine[- ]?tuning\b",
        r"\badaptation\b",
        r"\btest[- ]time\b",
    ],
    "Generative / Diffusion": [
        r"\bdiffusion\b",
        r"\bgenerative\b",
        r"\bgeneration\b",
        r"\bsynthesis\b",
        r"\bimage[- ]to[- ]image\b",
    ],
    "Federated / Continual / Generalization": [
        r"\bfederated\b",
        r"\bcontinual\b",
        r"\bgeneralization\b",
        r"\bgeneralizable\b",
        r"\bdomain shift\b",
        r"\bout[- ]of[- ]distribution\b",
        r"\bood\b",
    ],
}


PRIORITY_CATEGORIES = [
    "X-Ray / Radiography",
    "Mammography / Breast",
    "Ultrasound / Sonography",
    "MRI / MR",
    "CT / Tomography",
    "PET / Nuclear Medicine",
    "OCT / Ophthalmology / Retina",
    "Pathology / Microscopy / Cells",
    "Dermatology / Skin",
    "Endoscopy / Colonoscopy / Polyp",
    "Surgery / Medical Video",
    "3D / Volumetric Medical Imaging",
    "Medical AI / General",
]


def fetch_json(session: requests.Session, url: str) -> Any:
    response = session.get(url, timeout=45)
    response.raise_for_status()
    return response.json()


def absolute_url(url: str | None, base_url: str = BASE_URL) -> str:
    return urljoin(base_url, url or "") if url else ""


def compact_authors(authors: list[str], limit: int = 10) -> str:
    if len(authors) <= limit:
        return ", ".join(authors)
    return ", ".join(authors[:limit]) + f", ... (+{len(authors) - limit} more)"


def normalize_text(*parts: Any) -> str:
    text = " ".join(str(part or "") for part in parts)
    text = text.replace("‑", "-").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", text).strip()


def empty_external_links() -> dict[str, str]:
    return {key: "" for key in EXTERNAL_LINK_LABELS if key.endswith("_url") and key != "paper_url"}


def should_ignore_link(url: str) -> bool:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    if not host:
        return True
    if url.lower().startswith(("mailto:", "tel:", "javascript:")):
        return True
    if host.endswith("cvpr.thecvf.com"):
        return True
    if host.endswith("computer.org") or host.endswith("thecvf.com"):
        return True
    if host == "openaccess.thecvf.com":
        return path == "/menu" or "/content/cvpr2026/" in path
    return False


def add_external_link(links: dict[str, str], key: str, url: str) -> None:
    if not url or key not in links:
        return
    if not links[key]:
        links[key] = url


def classify_external_link(label: str, url: str) -> list[str]:
    lower = f"{label} {url}".lower()
    keys: list[str] = []
    if "github.com" in lower:
        keys.extend(["github_url", "code_url"])
    if any(token in lower for token in ["gitlab.com", "bitbucket.org", "paperswithcode.com"]):
        keys.append("code_url")
    if re.search(r"\b(code|source code|implementation)\b", lower):
        keys.append("code_url")
    if "arxiv.org" in lower:
        keys.append("arxiv_url")
    if any(token in lower for token in ["youtube.com", "youtube-nocookie.com", "youtu.be", "vimeo.com"]):
        keys.append("video_url")
    if re.search(r"\b(video|talk|presentation)\b", lower):
        keys.append("video_url")
    if any(token in lower for token in ["huggingface.co/spaces", "gradio", "streamlit"]):
        keys.append("demo_url")
    if re.search(r"\b(demo|playground|app)\b", lower):
        keys.append("demo_url")
    if re.search(r"\b(project|project page|website|homepage)\b", lower):
        keys.append("project_url")
    return list(dict.fromkeys(keys))


def collect_links_from_url(label: str, url: str, base_url: str = BASE_URL) -> dict[str, str]:
    links = empty_external_links()
    if not url:
        return links
    absolute = absolute_url(url, base_url)
    if should_ignore_link(absolute):
        return links
    keys = classify_external_link(label, absolute)
    if not keys:
        keys = ["project_url"]
    for key in keys:
        add_external_link(links, key, absolute)
    return links


def merge_external_links(target: dict[str, str], source: dict[str, str]) -> None:
    for key, url in source.items():
        add_external_link(target, key, url)


def find_matches(text: str, rules: dict[str, list[str]]) -> dict[str, list[str]]:
    matches: dict[str, list[str]] = {}
    for label, patterns in rules.items():
        hits = []
        for pattern in patterns:
            if re.search(pattern, text, flags=re.IGNORECASE):
                hits.append(pattern)
        if hits:
            matches[label] = hits
    return matches


def authors_from_event(event: dict[str, Any]) -> list[str]:
    return [a.get("fullname", "").strip() for a in event.get("authors", []) if a.get("fullname")]


def collect_images(event: dict[str, Any]) -> tuple[str, str]:
    poster = ""
    thumb = ""
    for media in event.get("eventmedia", []):
        if media.get("resourcetype") != "EventmediaImageFile" or not media.get("file"):
            continue
        if media.get("detailed_kind") == "thumb":
            thumb = absolute_url(media.get("file"))
        elif not poster:
            poster = absolute_url(media.get("file"))
    return poster, thumb


def collect_event_links(event: dict[str, Any]) -> dict[str, str]:
    links = empty_external_links()
    merge_external_links(links, collect_links_from_url("Project Page", event.get("url", "")))
    if event.get("sourceurl"):
        add_external_link(links, "source_url", event["sourceurl"])
    for media in event.get("eventmedia", []):
        media_url = media.get("uri") or media.get("url") or media.get("file")
        if not media_url:
            continue
        absolute = absolute_url(media_url)
        media_type = normalize_text(media.get("type"), media.get("name"), media.get("resourcetype")).lower()
        if "slide" in media_type or media.get("type") == "PDF":
            add_external_link(links, "slides_url", absolute)
        else:
            merge_external_links(links, collect_links_from_url(media_type, absolute))
    return links


def extract_external_links_from_soup(soup: BeautifulSoup, base_url: str) -> dict[str, str]:
    links = empty_external_links()
    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].strip()
        if not href or href.startswith("#"):
            continue
        label = " ".join(anchor.stripped_strings)
        absolute = absolute_url(href, base_url)
        if should_ignore_link(absolute):
            continue
        merge_external_links(links, collect_links_from_url(label, absolute, base_url))
    for iframe in soup.find_all("iframe", src=True):
        src = iframe["src"].strip()
        if not src:
            continue
        absolute = absolute_url(src, base_url)
        if any(token in absolute.lower() for token in ["youtube", "youtu.be", "vimeo"]):
            add_external_link(links, "video_url", absolute)
    return links


def parse_detail_page(session: requests.Session, url: str) -> dict[str, Any]:
    html = session.get(url, timeout=45)
    html.raise_for_status()
    soup = BeautifulSoup(html.text, "html.parser")
    detail = {
        "abstract": "",
        "paper_url": "",
        "poster_image_url": "",
        "thumbnail_url": "",
        "external_links": extract_external_links_from_soup(soup, url),
    }
    abstract = soup.select_one(".abstract-text-inner")
    if abstract:
        detail["abstract"] = " ".join(abstract.stripped_strings)
    for link in soup.find_all("a", href=True):
        href = link["href"]
        label = " ".join(link.stripped_strings).lower()
        is_cvpr2026_paper = "openaccess.thecvf.com/content/CVPR2026/" in href
        is_detail_paper_button = "paper pdf" in label and "openaccess.thecvf.com/menu" not in href
        if is_cvpr2026_paper or is_detail_paper_button:
            detail["paper_url"] = absolute_url(href)
            break
    for script in soup.find_all("script", {"type": "application/ld+json"}):
        if not script.string:
            continue
        try:
            data = json.loads(script.string)
        except json.JSONDecodeError:
            continue
        if isinstance(data.get("image"), str):
            detail["poster_image_url"] = absolute_url(data["image"])
        if isinstance(data.get("thumbnailUrl"), str):
            detail["thumbnail_url"] = absolute_url(data["thumbnailUrl"])
    return detail


def parse_openaccess_page(session: requests.Session, url: str) -> dict[str, str]:
    html = session.get(url, timeout=45)
    html.raise_for_status()
    soup = BeautifulSoup(html.text, "html.parser")
    return extract_external_links_from_soup(soup, url)


def is_medical_candidate(
    title: str,
    abstract: str,
    keywords: list[str],
    modality_hits: dict[str, list[str]],
    disease_hits: dict[str, list[str]],
    task_hits: dict[str, list[str]],
) -> bool:
    title_text = normalize_text(title)
    full_text = normalize_text(title, abstract, " ".join(keywords))
    if any(re.search(pattern, full_text, flags=re.IGNORECASE) for pattern in EXCLUSION_PATTERNS):
        return False
    title_modality = find_matches(title_text, MODALITY_RULES)
    title_disease = find_matches(title_text, DISEASE_RULES)
    title_task = find_matches(title_text, TASK_RULES)
    general_hit = "Medical AI / General" in modality_hits
    concrete_modality_hit = any(k != "Medical AI / General" for k in modality_hits)
    strong_title_disease_hit = "Cancer / Tumor / Lesion" in title_disease
    concrete_title_hit = any(k != "Medical AI / General" for k in title_modality) or strong_title_disease_hit
    title_general_hit = "Medical AI / General" in title_modality
    title_has_medical_modality_context = concrete_title_hit and (
        title_general_hit
        or strong_title_disease_hit
        or any(k in task_hits for k in ["Segmentation", "Detection / Diagnosis", "Medical VLM / VQA / Reasoning"])
        or re.search(r"\bmedical\b|\bclinical\b|\bbiomedical\b|\bradiolog", full_text, re.I)
    )

    if title_general_hit:
        return True
    if title_has_medical_modality_context:
        return True
    if general_hit and (concrete_modality_hit or "Cancer / Tumor / Lesion" in disease_hits):
        return True
    if concrete_modality_hit and (disease_hits or task_hits or re.search(r"\bmedical\b|\bclinical\b|\bbiomedical\b", full_text, re.I)):
        return True
    if "Cancer / Tumor / Lesion" in disease_hits and (
        "Segmentation" in task_hits or "Detection / Diagnosis" in task_hits or "Medical VLM / VQA / Reasoning" in task_hits
    ):
        return True
    return False


def build_paper_record(event: dict[str, Any], abstracts: dict[str, str], events_by_id: dict[int, dict[str, Any]]) -> dict[str, Any]:
    paper_id = int(event["id"])
    title = event.get("name") or ""
    abstract = abstracts.get(str(paper_id), "") or event.get("abstract", "")
    poster_image, thumbnail = collect_images(event)
    external_links = collect_event_links(event)
    related_sessions = []
    related_events = []
    sessions = [event.get("session")] if event.get("session") else []
    for related_id in event.get("related_events_ids", []) or []:
        related = events_by_id.get(int(related_id))
        if not related:
            continue
        related_sessions.append(related.get("session"))
        if related.get("session"):
            sessions.append(related["session"])
        related_events.append(
            {
                "id": related.get("id"),
                "eventtype": related.get("eventtype"),
                "session": related.get("session"),
                "url": absolute_url(related.get("virtualsite_url")),
            }
        )
    keywords = event.get("keywords") or []
    text = normalize_text(title, abstract, " ".join(keywords), event.get("session") or "", event.get("topic") or "")
    modality_hits = find_matches(text, MODALITY_RULES)
    disease_hits = find_matches(text, DISEASE_RULES)
    task_hits = find_matches(text, TASK_RULES)
    categories = [label for label in PRIORITY_CATEGORIES if label in modality_hits]
    disease_tags = list(disease_hits)
    task_tags = list(task_hits)
    primary_category = next((c for c in categories if c != "Medical AI / General"), categories[0] if categories else "Medical AI / General")
    return {
        "id": paper_id,
        "uid": event.get("uid"),
        "title": title,
        "authors": authors_from_event(event),
        "abstract": abstract,
        "keywords": keywords,
        "decision": event.get("decision"),
        "eventtype": event.get("eventtype"),
        "session": event.get("session"),
        "sessions": list(dict.fromkeys(s for s in sessions if s)),
        "topic": event.get("topic"),
        "cvpr_url": absolute_url(event.get("virtualsite_url")),
        "paper_url": event.get("paper_pdf_url") or "",
        "source_url": event.get("sourceurl") or "",
        "poster_image_url": poster_image,
        "thumbnail_url": thumbnail,
        "external_links": external_links,
        "related_events": related_events,
        "categories": categories,
        "primary_category": primary_category,
        "disease_tags": disease_tags,
        "task_tags": task_tags,
        "match_patterns": {
            "modalities": modality_hits,
            "diseases": disease_hits,
            "tasks": task_hits,
        },
    }


def link(label: str, url: str) -> str:
    return f"[{label}]({url})" if url else ""


def paper_links(paper: dict[str, Any]) -> str:
    links = []
    seen_urls = set()
    external_links = paper.get("external_links", {}) or {}
    ordered_links = {
        "paper_url": paper.get("paper_url", ""),
        "github_url": external_links.get("github_url", ""),
        "code_url": external_links.get("code_url", ""),
        "project_url": external_links.get("project_url", ""),
        "demo_url": external_links.get("demo_url", ""),
        "video_url": external_links.get("video_url", ""),
        "arxiv_url": external_links.get("arxiv_url", ""),
        "slides_url": external_links.get("slides_url", ""),
        "source_url": external_links.get("source_url", "") or paper.get("source_url", ""),
    }
    for key, url in ordered_links.items():
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)
        links.append(link(EXTERNAL_LINK_LABELS[key], url))
    return " ".join(links)


def poster_preview(paper: dict[str, Any]) -> str:
    image_url = paper.get("poster_image_url") or paper.get("thumbnail_url")
    if not image_url:
        return ""
    alt = html.escape(f"{paper['title']} poster", quote=True)
    return f'  <img src="{image_url}" alt="{alt}" width="420">'


def render_paper_item(paper: dict[str, Any]) -> list[str]:
    lines = [
        f"- {link('CVPR', paper['cvpr_url'])} **{paper['title']}**",
    ]
    links = paper_links(paper)
    if links:
        lines.append(f"  - {links}")
    preview = poster_preview(paper)
    if preview:
        lines.append(preview)
    if paper.get("authors"):
        lines.append(f"  - Authors: {compact_authors(paper['authors'])}")
    if paper.get("sessions"):
        lines.append(f"  - Session: {' | '.join(paper['sessions'])}")
    tags = paper["categories"] + paper["disease_tags"] + paper["task_tags"]
    if tags:
        lines.append(f"  - Tags: {', '.join(f'`{tag}`' for tag in tags)}")
    return lines


def write_markdown(papers: list[dict[str, Any]], generated: str) -> None:
    category_map: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for paper in papers:
        for category in paper["categories"] or [paper["primary_category"]]:
            category_map[category].append(paper)

    counts = Counter()
    for paper in papers:
        for category in paper["categories"] or [paper["primary_category"]]:
            counts[category] += 1
    image_count = sum(1 for paper in papers if paper.get("poster_image_url") or paper.get("thumbnail_url"))
    link_counts = Counter()
    project_demo_video_papers = 0
    for paper in papers:
        external_links = paper.get("external_links") or {}
        for key, url in external_links.items():
            if url:
                link_counts[key] += 1
        if any(external_links.get(key) for key in ["project_url", "demo_url", "video_url"]):
            project_demo_video_papers += 1

    readme: list[str] = [
        "# Awesome CVPR 2026 Medical AI",
        "",
        "A modality-oriented catalog of medical AI papers from the [CVPR 2026 virtual paper list](https://cvpr.thecvf.com/virtual/2026/papers.html).",
        "",
        "The list is generated from CVPR metadata and enriched with poster images plus GitHub/code/project/demo/video links when those links are exposed on the CVPR virtual or OpenAccess pages.",
        "",
        f"- Generated: {generated}",
        f"- Total medical-AI candidates: {len(papers)}",
        f"- Papers with poster thumbnails: {image_count}",
        f"- GitHub links: {link_counts['github_url']}",
        f"- Code links: {link_counts['code_url']}",
        f"- Papers with project/demo/video links: {project_demo_video_papers}",
        f"- arXiv links: {link_counts['arxiv_url']}",
        f"- Source data: [CVPR papers JSON]({PAPERS_JSON_URL}), [CVPR abstracts JSON]({ABSTRACTS_JSON_URL})",
        "- Inclusion rule: keyword-assisted matching over titles, abstracts, keywords, sessions, and topics.",
        "- Curation note: verify borderline entries with `medical_ai_catalog/cvpr2026_medical_ai_papers.json` and its `match_patterns` field.",
        "",
        "## Modality Index",
        "",
        "| Modality / Topic | Papers |",
        "|---|---:|",
    ]
    for category in PRIORITY_CATEGORIES:
        if counts.get(category):
            readme.append(f"| [{category}](#{slugify(category)}) | {counts[category]} |")
    readme.extend(["", "## Papers", ""])

    for category in PRIORITY_CATEGORIES:
        category_papers = sorted(category_map.get(category, []), key=lambda p: p["title"].lower())
        if not category_papers:
            continue
        anchor_id = slugify(category)
        readme.extend([f'<a id="{anchor_id}"></a>', f"### {category}", ""])
        seen = set()
        for paper in category_papers:
            if paper["id"] in seen:
                continue
            seen.add(paper["id"])
            readme.extend(render_paper_item(paper))
        readme.append("")

    README_PATH.write_text("\n".join(readme), encoding="utf-8")

    index_lines = [
        "# CVPR 2026 Medical AI Modality Index",
        "",
        f"Generated: {generated}",
        "",
    ]
    for category in PRIORITY_CATEGORIES:
        category_papers = sorted(category_map.get(category, []), key=lambda p: p["title"].lower())
        if not category_papers:
            continue
        index_lines.extend([f"## {category} ({len(category_papers)})", ""])
        for paper in category_papers:
            index_lines.append(f"- [{paper['title']}]({paper['cvpr_url']})")
        index_lines.append("")
    OUT_MODALITY_INDEX.write_text("\n".join(index_lines), encoding="utf-8")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text.strip())


def write_structured_outputs(papers: list[dict[str, Any]]) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    OUT_JSON.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    fields = [
        "id",
        "title",
        "primary_category",
        "categories",
        "disease_tags",
        "task_tags",
        "authors",
        "session",
        "cvpr_url",
        "paper_url",
        "github_url",
        "code_url",
        "project_url",
        "demo_url",
        "video_url",
        "arxiv_url",
        "slides_url",
        "source_url",
        "poster_image_url",
        "thumbnail_url",
        "abstract",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for paper in papers:
            row = {field: paper.get(field, "") for field in fields}
            row["authors"] = "; ".join(paper["authors"])
            row["categories"] = "; ".join(paper["categories"])
            row["disease_tags"] = "; ".join(paper["disease_tags"])
            row["task_tags"] = "; ".join(paper["task_tags"])
            external_links = paper.get("external_links", {}) or {}
            for key in ["github_url", "code_url", "project_url", "demo_url", "video_url", "arxiv_url", "slides_url", "source_url"]:
                row[key] = external_links.get(key, "") or paper.get(key, "")
            writer.writerow(row)


def build_catalog(enrich_details: bool = False, enrich_external_links: bool = False) -> list[dict[str, Any]]:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    raw_papers = fetch_json(session, PAPERS_JSON_URL)
    abstracts = fetch_json(session, ABSTRACTS_JSON_URL)
    events = raw_papers["results"]
    events_by_id = {int(event["id"]): event for event in events if event.get("id") is not None}
    poster_events = [event for event in events if event.get("eventtype") == "Poster"]

    candidates: list[dict[str, Any]] = []
    for event in poster_events:
        record = build_paper_record(event, abstracts, events_by_id)
        if is_medical_candidate(
            record["title"],
            record["abstract"],
            record["keywords"],
            record["match_patterns"]["modalities"],
            record["match_patterns"]["diseases"],
            record["match_patterns"]["tasks"],
        ):
            candidates.append(record)

    if enrich_details or enrich_external_links:
        for paper in candidates:
            has_core_details = paper.get("abstract") and paper.get("paper_url") and (
                paper.get("poster_image_url") or paper.get("thumbnail_url")
            )
            if has_core_details and not enrich_external_links:
                continue
            try:
                detail = parse_detail_page(session, paper["cvpr_url"])
            except requests.RequestException:
                detail = {}
            if not paper.get("abstract") and detail.get("abstract"):
                paper["abstract"] = detail["abstract"]
            if not paper.get("paper_url") and detail.get("paper_url"):
                paper["paper_url"] = detail["paper_url"]
            if not paper.get("poster_image_url") and detail.get("poster_image_url"):
                paper["poster_image_url"] = detail["poster_image_url"]
            if not paper.get("thumbnail_url") and detail.get("thumbnail_url"):
                paper["thumbnail_url"] = detail["thumbnail_url"]
            if enrich_external_links and detail.get("external_links"):
                merge_external_links(paper["external_links"], detail["external_links"])
            if enrich_external_links and paper.get("paper_url"):
                try:
                    openaccess_links = parse_openaccess_page(session, paper["paper_url"])
                except requests.RequestException:
                    openaccess_links = {}
                merge_external_links(paper["external_links"], openaccess_links)

    candidates.sort(key=lambda p: (p["primary_category"], p["title"].lower(), p["id"]))
    generated = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    OUT_DIR.mkdir(exist_ok=True)
    write_structured_outputs(candidates)
    write_markdown(candidates, generated)
    return candidates


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a CVPR 2026 medical AI paper catalog.")
    parser.add_argument("--enrich-details", action="store_true", help="Fetch detail pages for missing abstract/paper/image links.")
    parser.add_argument(
        "--enrich-external-links",
        action="store_true",
        help="Fetch CVPR/OpenAccess pages for GitHub/code/project/demo/video/arXiv links.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    papers = build_catalog(enrich_details=args.enrich_details, enrich_external_links=args.enrich_external_links)
    counts = Counter()
    for paper in papers:
        for category in paper["categories"] or [paper["primary_category"]]:
            counts[category] += 1
    print(f"medical_ai_candidates={len(papers)}")
    for category, count in counts.most_common():
        print(f"{category}: {count}")
    print(f"readme={README_PATH.resolve()}")
    print(f"json={OUT_JSON.resolve()}")
    print(f"csv={OUT_CSV.resolve()}")


if __name__ == "__main__":
    main()
