# Awesome CVPR 2026 Medical AI

A modality-oriented catalog of medical AI papers from the [CVPR 2026 virtual paper list](https://cvpr.thecvf.com/virtual/2026/papers.html).

The list is generated from CVPR metadata and enriched with poster images plus GitHub/code/project/demo/video links when those links are exposed on the CVPR virtual or OpenAccess pages.

- Generated: 2026-06-07T00:04:45+09:00
- Total medical-AI candidates: 265
- Papers with poster thumbnails: 179
- GitHub links: 25
- Code links: 25
- Papers with project/demo/video links: 131
- arXiv links: 109
- Source data: [CVPR papers JSON](https://cvpr.thecvf.com/static/virtual/data/cvpr-2026-orals-posters.json), [CVPR abstracts JSON](https://cvpr.thecvf.com/static/virtual/data/cvpr-2026-abstracts.json)
- Inclusion rule: keyword-assisted matching over titles, abstracts, keywords, sessions, and topics.
- Curation note: verify borderline entries with `medical_ai_catalog/cvpr2026_medical_ai_papers.json` and its `match_patterns` field.

## Modality Index

| Modality / Topic | Papers |
|---|---:|
| [X-Ray / Radiography](#x-ray-radiography) | 15 |
| [Mammography / Breast](#mammography-breast) | 3 |
| [Ultrasound / Sonography](#ultrasound-sonography) | 8 |
| [MRI / MR](#mri-mr) | 40 |
| [CT / Tomography](#ct-tomography) | 32 |
| [PET / Nuclear Medicine](#pet-nuclear-medicine) | 7 |
| [OCT / Ophthalmology / Retina](#oct-ophthalmology-retina) | 8 |
| [Pathology / Microscopy / Cells](#pathology-microscopy-cells) | 109 |
| [Dermatology / Skin](#dermatology-skin) | 3 |
| [Endoscopy / Colonoscopy / Polyp](#endoscopy-colonoscopy-polyp) | 11 |
| [Surgery / Medical Video](#surgery-medical-video) | 17 |
| [3D / Volumetric Medical Imaging](#3d-volumetric-medical-imaging) | 12 |
| [Medical AI / General](#medical-ai-general) | 203 |

## Papers

<a id="x-ray-radiography"></a>
### X-Ray / Radiography

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41094) **AnatomiX, an Anatomy-Aware Grounded Multimodal Large Language Model for Chest X-Ray Interpretation**
  - Session: Findings Poster Session 2
  - Tags: `X-Ray / Radiography`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36514) **DARC: Dual Adjustment Reasoning with Counterfactuals for Trustworthy Chest X-ray Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_DARC_Dual_Adjustment_Reasoning_with_Counterfactuals_for_Trustworthy_Chest_X-ray_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/8AC2roAq1I8) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36514.png" alt="DARC: Dual Adjustment Reasoning with Counterfactuals for Trustworthy Chest X-ray Classification poster" width="420">
  - Authors: Zhifang Liao, Junhao Li, HaoKang Ding, Yucheng Song
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36661) **Efficient Unrolled Networks for Large-Scale 3D Inverse Problems**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Vo_Efficient_Unrolled_Networks_for_Large-Scale_3D_Inverse_Problems_CVPR_2026_paper.html) [Project](https://romainvo.github.io/efficient-unrolling/) [Video](https://www.youtube-nocookie.com/embed/ENMY8fVFM9A) [arXiv](https://arxiv.org/abs/2601.02141) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36661.png" alt="Efficient Unrolled Networks for Large-Scale 3D Inverse Problems poster" width="420">
  - Authors: Romain Vo, Julián Tachella
  - Session: Poster Session 6 | Oral Session 6D: Large-Scale Neural Modeling
  - Tags: `X-Ray / Radiography`, `MRI / MR`, `CT / Tomography`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36497) **Exact-GS: Mathematically Rigorous and Accurate 3D Gaussian Splatting for 3D X-ray Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Exact-GS_Mathematically_Rigorous_and_Accurate_3D_Gaussian_Splatting_for_3D_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/MsCFB3z-cJU) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36497.png" alt="Exact-GS: Mathematically Rigorous and Accurate 3D Gaussian Splatting for 3D X-ray Reconstruction poster" width="420">
  - Authors: Guangpu Yang, Steffen Kieß, Hanxiang Luo, Xingyu Liu, Sven Simon
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38390) **Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Instruction-Guided_Lesion_Segmentation_for_Chest_X-rays_with_Automatically_Generated_Large-Scale_CVPR_2026_paper.html) [GitHub](https://github.com/checkoneee/ROSALIA) [Video](https://www.youtube-nocookie.com/embed/1el0IQG3nJU) [arXiv](https://arxiv.org/abs/2511.15186) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38390.png" alt="Instruction-Guided Lesion Segmentation for Chest X-rays with Automatically Generated Large-Scale Dataset poster" width="420">
  - Authors: Geon Choi, Hangyul Yoon, Hyunju Shin, Hyunki Park, Sang Hoon Seo, Eunho Yang, Edward Choi
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `Cancer / Tumor / Lesion`, `Segmentation`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41034) **MAE-XNT: A Foundation Model for Segmenting Neuronal Tissue Volumes Generated with X-Ray Nanotomography**
  - Session: Findings Poster Session 2
  - Tags: `X-Ray / Radiography`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40162) **OralGPT-Plus: Learning to Use Visual Tools via Reinforcement Learning for Panoramic X-ray Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Fan_OralGPT-Plus_Learning_to_Use_Visual_Tools_via_Reinforcement_Learning_for_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.06366) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40162.png" alt="OralGPT-Plus: Learning to Use Visual Tools via Reinforcement Learning for Panoramic X-ray Analysis poster" width="420">
  - Authors: Yuxuan Fan, JING HAO, Hong Chen, Jiahao Bao, Yihua Shao, Yuci Liang, Kuo Feng Hung, Hao Tang
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40112) **OraPO: Oracle-educated Reinforcement Learning for Data-efficient and Factual Radiology Report Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_OraPO_Oracle-educated_Reinforcement_Learning_for_Data-efficient_and_Factual_Radiology_Report_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/LyjMwISk-R0) [arXiv](https://arxiv.org/abs/2509.18600) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40112.png" alt="OraPO: Oracle-educated Reinforcement Learning for Data-efficient and Factual Radiology Report Generation poster" width="420">
  - Authors: Zhuoxiao Chen, Hongyang Yu, Ying Xu, Yadan Luo, Long Duong, Yuan-Fang Li
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38827) **Personalized Longitudinal Medical Report Generation via Temporally-Aware Federated Adaptation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Personalized_Longitudinal_Medical_Report_Generation_via_Temporally-Aware_Federated_Adaptation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2602.19668) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: He Zhu, Ren Togo, Takahiro Ogawa, Kenji Hirata, Minghui Tang, Takaaki Yoshimura, Hiroyuki Sugimori, Noriko Nishioka, Yukie Shimizu, Kohsuke Kudo, ... (+1 more)
  - Session: Poster Session 6
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36623) **Phrase-grounded APO for Improving Chest X-ray Report Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mahmood_Phrase-grounded_APO_for_Improving_Chest_X-ray_Report_Generation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/uDIE70Ei-vk) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Raziuddin Mahmood, Tanveer Syeda-Mahmood
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36920) **Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Revisiting_Pose_Sensitivity_in_Splat-based_Computed_Tomography_under_Sparse-view_Reconstruction_CVPR_2026_paper.html) [Project](https://vclab.kaist.ac.kr/cvpr2026p2/) [Video](https://www.youtube-nocookie.com/embed/vqliZ-OyNIg) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36920.png" alt="Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction poster" width="420">
  - Authors: Kiseok Choi, Hyeongjun Cho, Inchul Kim, Min H. Kim
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37552) **SAT-RRG: LLM-Guided Self-Adaptive Training for Radiology Report Generation with Token-Level Push–Pull Optimization**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SAT-RRG_LLM-Guided_Self-Adaptive_Training_for_Radiology_Report_Generation_with_Token-Level_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/PJdtoAPCO64) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37552-thumb.png" alt="SAT-RRG: LLM-Guided Self-Adaptive Training for Radiology Report Generation with Token-Level Push–Pull Optimization poster" width="420">
  - Authors: YUNYI LIU, Yingshu Li, Tong Chen, Lingqiao Liu, Lei Wang, Luping Zhou
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38465) **Splat-Based Metal Artifact Reduction in Cone-Beam CT via Compact Attenuation Modeling**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Splat-Based_Metal_Artifact_Reduction_in_Cone-Beam_CT_via_Compact_Attenuation_CVPR_2026_paper.html) [Project](https://vclab.kaist.ac.kr/cvpr2026p1/) [Video](https://www.youtube-nocookie.com/embed/eBYZAX7rQPw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38465.png" alt="Splat-Based Metal Artifact Reduction in Cone-Beam CT via Compact Attenuation Modeling poster" width="420">
  - Authors: Kiseok Choi, Jaemin Cho, Inchul Kim, Min H. Kim
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Segmentation`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39575) **Temporal Inversion for Learning Interval Change in Chest X-Rays**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ko_Temporal_Inversion_for_Learning_Interval_Change_in_Chest_X-Rays_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/hbrnlS8hkWU) [arXiv](https://arxiv.org/abs/2604.04563) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39575.png" alt="Temporal Inversion for Learning Interval Change in Chest X-Rays poster" width="420">
  - Authors: Hanbin Ko, Kyungmin Jeon, Doowoong Choi, Chang Min Park
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36840) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_X-WIN_Building_Chest_Radiograph_World_Model_via_Predictive_Sensing_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/ZzPPjRx9hDI) [arXiv](https://arxiv.org/abs/2511.14918) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36840.png" alt="X-WIN: Building Chest Radiograph World Model via Predictive Sensing poster" width="420">
  - Authors: Zefan Yang, Ge Wang, James Hendler, Mannudeep K. Kalra, Pingkun Yan
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`

<a id="mammography-breast"></a>
### Mammography / Breast

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37344) **D2T2 - Multimodal Automated Planning for Brachytherapy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Moore_D2T2_-_Multimodal_Automated_Planning_for_Brachytherapy_CVPR_2026_paper.html) [GitHub](https://github.com/UCSD-Health-QUIVER/D2T2) [Video](https://www.youtube-nocookie.com/embed/TAcxI1204cw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37344.png" alt="D2T2 - Multimodal Automated Planning for Brachytherapy poster" width="420">
  - Authors: Lance C. Moore, Aranyo Mitra, Ryan Truong, Karoline Kallis, Kelly Kisling, Sandra M. Meyers, Nuno Vasconcelos
  - Session: Poster Session 6
  - Tags: `Mammography / Breast`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38951) **LUMINA: A Multi-Vendor Mammography Benchmark with Energy Harmonization Protocol**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_LUMINA_A_Multi-Vendor_Mammography_Benchmark_with_Energy_Harmonization_Protocol_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/rtUfsZegJCM) [arXiv](https://arxiv.org/abs/2603.14644) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38951.png" alt="LUMINA: A Multi-Vendor Mammography Benchmark with Energy Harmonization Protocol poster" width="420">
  - Authors: Hongyi Pan, Gorkem Durak, Halil Ertugrul Aktas, Andrea M. Bejar, Baver Tutun, Emre Uysal, Ezgi Bülbül, Mehmet Faith Dogan, Berrin Erok, Berna Yildirim, ... (+2 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Mammography / Breast`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41047) **Meta-CDMTransNet: Cross-Domain Multi-Scale Transformer Meta-Learning Framework for Few-Shot Breast Histopathological Image Classification**
  - Session: Findings Poster Session 2
  - Tags: `Mammography / Breast`, `Pathology / Microscopy / Cells`, `Medical AI / General`

<a id="ultrasound-sonography"></a>
### Ultrasound / Sonography

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39285) **EchoPOSE: 6D Pose Estimation of Sparse Echocardiograms for Left-Ventricular 3D Shape Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Iijima_EchoPOSE_6D_Pose_Estimation_of_Sparse_Echocardiograms_for_Left-Ventricular_3D_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/VcV4cmd0RnI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39285.png" alt="EchoPOSE: 6D Pose Estimation of Sparse Echocardiograms for Left-Ventricular 3D Shape Reconstruction poster" width="420">
  - Authors: Lucas Iijima, Yihao Luo, Dario Sesia, Amit Kaura, Jamil Mayet, Choon Hwai Yap
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Ultrasound / Sonography`, `Medical AI / General`, `Organs / Anatomy`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38146) **EchoVDiff: Cardiac-Cycle Echocardiography Video Generation from Arbitrary Frame**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_EchoVDiff_Cardiac-Cycle_Echocardiography_Video_Generation_from_Arbitrary_Single_Frame_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Jiansong Zhang, Xiaying Yang, Xiaoling Luo, Linlin Shen
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Ultrasound / Sonography`, `Organs / Anatomy`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36172) **F^2-Assist: Multi-Phase Fetal Growth Forecast and Report Generation from Ultrasound Examination**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pu_F2-Assist_Multi-Phase_Fetal_Growth_Forecast_and_Report_Generation_from_Ultrasound_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36172.png" alt="F^2-Assist: Multi-Phase Fetal Growth Forecast and Report Generation from Ultrasound Examination poster" width="420">
  - Authors: Bin Pu, XUSHENG LIANG, Xinpeng Ding, Jinlin Wu, Zhen Lei, Shengli Li, Kenli Li, Jiawei Ma
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39074) **GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kong_GaussianPile_A_Unified_Sparse_Gaussian_Splatting_Framework_for_Slice-based_Volumetric_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/0UNUSuksZzY) [arXiv](https://arxiv.org/abs/2603.20611) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39074.png" alt="GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction poster" width="420">
  - Authors: Di Kong, Yikai Wang, Wenjie Guo, Yifan Bu, Boya Zhang, Yuexin Duan, Xiawei Yue, Wenbiao Du, Yiman Zhong, Yuwen Chen, ... (+1 more)
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `Pathology / Microscopy / Cells`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38145) **Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Khan_Keep_It_Frozen_Domain-Routed_Conditional_Residual_Modulation_for_Multi-Domain_Vision_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/q18ZYEyK7Tw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38145.png" alt="Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers poster" width="420">
  - Authors: Ufaq Khan, Umair Nawaz, Massimo Caputo, Muhammad Bilal, Junaid Qadir, Muhammad Haris Khan
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36220) **OSA: Echocardiography Video Segmentation via Orthogonalized State Update and Anatomical Prior-aware Feature Enhancement**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_OSA_Echocardiography_Video_Segmentation_via_Orthogonalized_State_Update_and_Anatomical_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/InheKgsZkTk) [arXiv](https://arxiv.org/abs/2603.26188) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36220.png" alt="OSA: Echocardiography Video Segmentation via Orthogonalized State Update and Anatomical Prior-aware Feature Enhancement poster" width="420">
  - Authors: Rui Wang, Huisi Wu, Jing Qin
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37844) **Semi-supervised Echocardiography Video Segmentation via Anchor Semantic Awareness and Continuous Pseudo-label Reforging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Fang_Semi-supervised_Echocardiography_Video_Segmentation_via_Anchor_Semantic_Awareness_and_Continuous_CVPR_2026_paper.html) [GitHub](https://github.com/YunPeng-Fang/EchoForge) [Video](https://www.youtube-nocookie.com/embed/W6KlsEieXXc) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37844.png" alt="Semi-supervised Echocardiography Video Segmentation via Anchor Semantic Awareness and Continuous Pseudo-label Reforging poster" width="420">
  - Authors: Yunpeng Fang, Yimu Sun, Jingxing Guo, Huisi Wu, Jing Qin
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Ultrasound / Sonography`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38535) **Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_Ultrasound-CLIP_Semantic-Aware_Contrastive_Pre-training_for_Ultrasound_Image-Text_Understanding_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/p5AF42K_oz4) [arXiv](https://arxiv.org/abs/2604.01749) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38535.png" alt="Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding poster" width="420">
  - Authors: Jiayun Jin, Haolong Chai, Xueying Huang, Xiaoqing Guo, Zengwei Zheng, Zhan Zhou, Junmei Wang, Xinyu Wang, Jie Liu, Binbin Zhou
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`

<a id="mri-mr"></a>
### MRI / MR

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37656) **Adaptive Anisotropic Gaussian Splatting for Multi-contrast MRI Arbitrary-Scale Super-Resolution with Anatomy Guidance**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yan_Adaptive_Anisotropic_Gaussian_Splatting_for_Multi-contrast_MRI_Arbitrary-Scale_Super-Resolution_with_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37656.png" alt="Adaptive Anisotropic Gaussian Splatting for Multi-contrast MRI Arbitrary-Scale Super-Resolution with Anatomy Guidance poster" width="420">
  - Authors: Qiuhai Yan, Kang Chen, Zhengjie Lu, Tingting Wang, Faming Fang, Guixu Zhang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Organs / Anatomy`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41056) **Anatomy-Aware Adaptive Feature Perturbation Framework for Semi-Supervised MRI Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37720) **Beyond the Static-World: Lifelong Learning for All-in-One Medical Image Restoration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shan_Beyond_the_Static-World_Lifelong_Learning_for_All-in-One_Medical_Image_Restoration_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37720.png" alt="Beyond the Static-World: Lifelong Learning for All-in-One Medical Image Restoration poster" width="420">
  - Authors: Shihao Shan, Hongying Liu, Fanhua Shang, Liang Wan, Jingjing Deng
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `Medical AI / General`, `Restoration / Reconstruction`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36592) **Breaking the Continuum: Discrete Distribution Learning for Structural MRI Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_Breaking_the_Continuum_Discrete_Distribution_Learning_for_Structural_MRI_Reconstruction_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36592.png" alt="Breaking the Continuum: Discrete Distribution Learning for Structural MRI Reconstruction poster" width="420">
  - Authors: Tianle Lyu, Mengjingcheng Mo, Ting Wen, Zhen Song, Zinan Xiong, Yanjie Zhu
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38911) **Bridging Brain and Semantics: A Hierarchical Framework for Semantically Enhanced fMRI-to-Video Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_Bridging_Brain_and_Semantics_A_Hierarchical_Framework_for_Semantically_Enhanced_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2605.14569) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38911.png" alt="Bridging Brain and Semantics: A Hierarchical Framework for Semantically Enhanced fMRI-to-Video Reconstruction poster" width="420">
  - Authors: Yujie Wei, Chenglong Ma, Jianxiong Gao, Chenhui Wang, Shiwei Zhang, Biao Gong, Shuai Tan, Hangjie Yuan, Hongming Shan
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `Organs / Anatomy`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40014) **Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling?**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Can_Natural_Image_Autoencoders_Compactly_Tokenize_fMRI_Volumes_for_Long-Range_CVPR_2026_paper.html) [Project](https://concarne2.github.io/tablet_project_page/) [Video](https://www.youtube-nocookie.com/embed/D9sMMdMtZsM) [arXiv](https://arxiv.org/abs/2604.03619) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40014.png" alt="Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling? poster" width="420">
  - Authors: Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, Taesup Moon
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37941) **CMR-RD: Long-Tailed Adaptive VLM for Explainable CMR Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CMR-RD_Long-Tailed_Adaptive_VLM_for_Explainable_CMR_Diagnosis_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37941.png" alt="CMR-RD: Long-Tailed Adaptive VLM for Explainable CMR Diagnosis poster" width="420">
  - Authors: Yansong Li, Zhongxi Qiu, Yun Tian, Zheng jinyu, Shuo Li
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36817) **Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Continual_Learning_for_fMRI-Based_Brain_Disorder_Diagnosis_via_Functional_Connectivity_CVPR_2026_paper.html) [GitHub](https://github.com/4me808/FORGE) [arXiv](https://arxiv.org/abs/2604.14259) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36817.png" alt="Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay poster" width="420">
  - Authors: qianyu Chen, Shujian Yu
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39371) **Cross-domain Dual-stream Feature Disentanglement for Brain Disorder Prediction with Sparsely Labeled PET**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Cross-domain_Dual-stream_Feature_Disentanglement_for_Brain_Disorder_Prediction_with_Sparsely_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/OJvup4i7O50) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39371.png" alt="Cross-domain Dual-stream Feature Disentanglement for Brain Disorder Prediction with Sparsely Labeled PET poster" width="420">
  - Authors: Huabin Wang, Xinyu Chen, Yuan Zhou, Fei Liu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38658) **CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_CROWn_A_Unified_Framework_for_Anti-Aliased_Downsampling_and_Phase-Calibrated_Fusion_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38658.png" alt="CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation poster" width="420">
  - Authors: Xingru Huang, Shuanghua Ye, Zhao Huang, Wenwen Tang, Huiyu Zhou, Zhiwen Zheng, Jin Liu, Xiaoshuai Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `OCT / Ophthalmology / Retina`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37051) **Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Delving_Aleatoric_Uncertainty_in_Medical_Image_Segmentation_via_Vision_Foundation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.10963) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37051.png" alt="Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models poster" width="420">
  - Authors: Ruiyang Li, Fang Liu, Licheng Jiao, Xinglin Xie, Jiayao Hao, Shuo Li, Xu Liu, Jingyi yang, Lingling Li, Puhua Chen, ... (+1 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37988) **Diffusion MRI Transformer with a Diffusion Space Rotary Positional Embedding (D-RoPE)**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kung_Diffusion_MRI_Transformer_with_a_Diffusion_Space_Rotary_Positional_Embedding_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/B-JsuTK1luk) [arXiv](https://arxiv.org/abs/2603.25977) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37988.png" alt="Diffusion MRI Transformer with a Diffusion Space Rotary Positional Embedding (D-RoPE) poster" width="420">
  - Authors: Gustavo Chau Loo Kung, Mohammad H. Abbasi, Camila Blank, Juze Zhang, Alan Q. Wang, Sophie Ostmeier, Akshay Chaudhari, Kilian Pohl, Ehsan Adeli
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37060) **DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_DK-DDIL_Adaptive_Knowledge_Retention_for_Dynamic_Domain-Incremental_Learning_in_Medical_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37060.png" alt="DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging poster" width="420">
  - Authors: Yuxi Ma, Sujie Liu, Jing Yang, Jiacheng Wang, Yiping Chen, Baptiste Magnier, Liansheng Wang
  - Session: Poster Session 6 | Oral Session 6C: Medical Vision
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36661) **Efficient Unrolled Networks for Large-Scale 3D Inverse Problems**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Vo_Efficient_Unrolled_Networks_for_Large-Scale_3D_Inverse_Problems_CVPR_2026_paper.html) [Project](https://romainvo.github.io/efficient-unrolling/) [Video](https://www.youtube-nocookie.com/embed/ENMY8fVFM9A) [arXiv](https://arxiv.org/abs/2601.02141) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36661.png" alt="Efficient Unrolled Networks for Large-Scale 3D Inverse Problems poster" width="420">
  - Authors: Romain Vo, Julián Tachella
  - Session: Poster Session 6 | Oral Session 6D: Large-Scale Neural Modeling
  - Tags: `X-Ray / Radiography`, `MRI / MR`, `CT / Tomography`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37063) **Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Qiu_Elucidating_the_Design_Space_of_Arbitrary-Noise-Based_Diffusion_Models_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2507.18534) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37063.png" alt="Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models poster" width="420">
  - Authors: Xingyu Qiu, Mengying Yang, Xinghua Ma, Dong Liang, Fanding Li, Gongning Luo, wei wang, Kuanquan Wang, Shuo Li
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Restoration / Reconstruction`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39300) **EMAD: Evidence-Centric Grounded Multimodal Diagnosis for Alzheimer’s Disease**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_EMAD_Evidence-Centric_Grounded_Multimodal_Diagnosis_for_Alzheimers_Disease_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Qiuhui Chen, Xuancheng Yao, Zhenglei Zhou, Xinyue Hu, Yi Hong
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38590) **ERMoE: Eigen-Reparameterized Mixture-of-Experts for Stable Routing and Interpretable Specialization**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_ERMoE_Eigen-Reparameterized_Mixture-of-Experts_for_Stable_Routing_and_Interpretable_Specialization_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/EIfqoIgfHn4) [arXiv](https://arxiv.org/abs/2511.10971) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38590.png" alt="ERMoE: Eigen-Reparameterized Mixture-of-Experts for Stable Routing and Interpretable Specialization poster" width="420">
  - Authors: Anzhe Cheng, Shukai Duan, Shixuan Li, Chenzhong Yin, Mingxi Cheng, Heng Ping, Tamoghna Chattopadhyay, Sophia Thomopoulos, Shahin Nazarian, Paul Thompson, ... (+1 more)
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38836) **fMRI-LM: Towards a Universal Foundation Model for Language-Aligned fMRI Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_fMRI-LM_Towards_a_Universal_Foundation_Model_for_Language-Aligned_fMRI_Understanding_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/mtbHo7gNE-k) [arXiv](https://arxiv.org/abs/2511.21760) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38836.png" alt="fMRI-LM: Towards a Universal Foundation Model for Language-Aligned fMRI Understanding poster" width="420">
  - Authors: Yuxiang Wei, Yanteng Zhang, Xi Xiao, Chengxuan Qian, Tianyang Wang, Vince D. Calhoun
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Organs / Anatomy`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36613) **GenTract: Generative Global Tractography**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sargood_GenTract_Generative_Global_Tractography_CVPR_2026_paper.html) [Project](https://alecsargood.github.io/GenTract/) [Video](https://www.youtube-nocookie.com/embed/AOqxqgsWqr8) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36613.png" alt="GenTract: Generative Global Tractography poster" width="420">
  - Authors: Alec Sargood, Lemuel Puglisi, Elinor Thompson, Mirco Musolesi, Daniel C. Alexander
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `Organs / Anatomy`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39862) **HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_HalluGen_Synthesizing_Realistic_and_Controllable_Hallucinations_for_Evaluating_Image_Restoration_CVPR_2026_paper.html) [GitHub](https://github.com/edshkim98/HalluGen) [arXiv](https://arxiv.org/abs/2512.03345) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39862.png" alt="HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration poster" width="420">
  - Authors: Seunghoi Kim, Henry F. J. Tregidgo, Chen Jin, Matteo Figini, Daniel C. Alexander
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39258) **IEBGL:An Interpretability-Enhanced Brain Graph Learning Framework with LLM-Instructed Topology and Literature-Augmented Semantics**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Duan_IEBGLAn_Interpretability-Enhanced_Brain_Graph_Learning_Framework_with_LLM-Instructed_Topology_and_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39258.png" alt="IEBGL:An Interpretability-Enhanced Brain Graph Learning Framework with LLM-Instructed Topology and Literature-Augmented Semantics poster" width="420">
  - Authors: Yihang Duan, Shuo Huang, Lizhang Lizhang, Meiling Wang, Li Zhang
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38145) **Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Khan_Keep_It_Frozen_Domain-Routed_Conditional_Residual_Modulation_for_Multi-Domain_Vision_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/q18ZYEyK7Tw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38145.png" alt="Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers poster" width="420">
  - Authors: Ufaq Khan, Umair Nawaz, Massimo Caputo, Muhammad Bilal, Junaid Qadir, Muhammad Haris Khan
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36397) **Learning complete and explainable visual representations from itemized text supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_Learning_complete_and_explainable_visual_representations_from_itemized_text_supervision_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/X9lDEqtVGpo) [arXiv](https://arxiv.org/abs/2512.11141) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36397.png" alt="Learning complete and explainable visual representations from itemized text supervision poster" width="420">
  - Authors: Yiwei Lyu, Chenhui Zhao, Soumyanil Banerjee, Shixuan Liu, Akshay Rao, Akhil Kondepudi, Honglak Lee, Todd C. Hollon
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36666) **Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Learning_Generalizable_3D_Medical_Image_Representations_from_Mask-Guided_Self-Supervision_CVPR_2026_paper.html) [GitHub](https://github.com/Stanford-AIMI/MASS?tab=readme-ov-file) [arXiv](https://arxiv.org/abs/2603.13660) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36666.png" alt="Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision poster" width="420">
  - Authors: Yunhe Gao, Yabin Zhang, Chong Wang, Jiaming Liu, Maya Varma, Jean-Benoit Delbrouck, Akshay Chaudhari, Curtis Langlotz
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39592) **Masked-Diffusion Autoencoders for 3D Medical Vision Representation Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Tu_Masked-Diffusion_Autoencoders_for_3D_Medical_Vision_Representation_Learning_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Jiachen Tu, Guanghui Qin, Theodore Zhengde Zhao, Jeya Maria Jose Valanarasu, Sheng Zhang, Tristan Naumann, Fan Lam, Sheng Wang, Hoifung Poon
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40632) **Modality-Aware and Anatomical Vector-Quantized Autoencoding for Multimodal Brain MRI**
  - Session: Findings Poster Session 1
  - Tags: `MRI / MR`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36320) **Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Qu_Modeling_Spatiotemporal_Neural_Frames_for_High_Resolution_Brain_Dynamic_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.24176) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36320.png" alt="Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic poster" width="420">
  - Authors: Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Organs / Anatomy`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37934) **MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_MorphSeek_Fine-grained_Latent_Representation-Level_Policy_Optimization_for_Deformable_Image_Registration_CVPR_2026_paper.html) [GitHub](https://github.com/cai114514/MorphSeek) [Video](https://www.youtube-nocookie.com/embed/DGljUXt-A_w) [arXiv](https://arxiv.org/abs/2511.17392) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37934.png" alt="MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration poster" width="420">
  - Authors: Runxun Zhang, Yizhou Liu, Dongrui Li, Bo XU, Jingwei Wei
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Registration`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37460) **MRI Contrast Enhancement Kinetics World Model**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kong_MRI_Contrast_Enhancement_Kinetics_World_Model_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2602.19285) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37460.png" alt="MRI Contrast Enhancement Kinetics World Model poster" width="420">
  - Authors: Jindi Kong, Yuting He, Cong Xia, Rongjun Ge, Shuo Li
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38185) **PGR-Net: Prior-Guided ROI Reasoning Network for Brain Tumor MRI Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_PGR-Net_Prior-Guided_ROI_Reasoning_Network_for_Brain_Tumor_MRI_Segmentation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.21626) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38185.png" alt="PGR-Net: Prior-Guided ROI Reasoning Network for Brain Tumor MRI Segmentation poster" width="420">
  - Authors: Jiacheng Lu, Hui Ding, Shiyu Zhang, Guoping Huo
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38321) **PnP-CM: Consistency Models as Plug-and-Play Priors for Inverse Problems**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gulle_PnP-CM_Consistency_Models_as_Plug-and-Play_Priors_for_Inverse_Problems_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/dUHmaobgx7o) [arXiv](https://arxiv.org/abs/2509.22736) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38321.png" alt="PnP-CM: Consistency Models as Plug-and-Play Priors for Inverse Problems poster" width="420">
  - Authors: Merve Gulle, junno yun, Yasar Utku Alcalar, Mehmet Akcakaya
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37228) **Prospective Dynamic 3D MRI Reconstruction via Latent-Space Motion Tracking from Single Measurement**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Prospective_Dynamic_3D_MRI_Reconstruction_via_Latent-Space_Motion_Tracking_from_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37228.png" alt="Prospective Dynamic 3D MRI Reconstruction via Latent-Space Motion Tracking from Single Measurement poster" width="420">
  - Authors: Lixuan Chen, Zhongnan Liu, Jesse Hamilton, James M. Balter, Jeong Joon Park, Liyue Shen
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36495) **SHAPE: Structure-aware Hierarchical Unsupervised Domain Adaptation with Plausibility Evaluation for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_SHAPE_Structure-aware_Hierarchical_Unsupervised_Domain_Adaptation_with_Plausibility_Evaluation_for_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/4Y3OLaeNn0Y) [arXiv](https://arxiv.org/abs/2603.21904) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36495.png" alt="SHAPE: Structure-aware Hierarchical Unsupervised Domain Adaptation with Plausibility Evaluation for Medical Image Segmentation poster" width="420">
  - Authors: Linkuan Zhou, Yinghao Xia, Yufei Shen, Xiangyu Li, Wenjie Du, Cong Cong, leyi wei, Ran Su, Qiangguo Jin
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39772) **Solving a Nonlinear Blind Inverse Problem for Tagged MRI with Physics and Deep Generative Priors**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Bian_Solving_a_Nonlinear_Blind_Inverse_Problem_for_Tagged_MRI_with_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/NC5aeuQ1rKg) [arXiv](https://arxiv.org/abs/2603.00882) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39772.png" alt="Solving a Nonlinear Blind Inverse Problem for Tagged MRI with Physics and Deep Generative Priors poster" width="420">
  - Authors: Zhangxing Bian, Shuwen Wei, Samuel W. Remedios, Junyu Chen, Aaron Carass, Blake E. Dewey, Jerry L Prince
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `Organs / Anatomy`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38535) **Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_Ultrasound-CLIP_Semantic-Aware_Contrastive_Pre-training_for_Ultrasound_Image-Text_Understanding_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/p5AF42K_oz4) [arXiv](https://arxiv.org/abs/2604.01749) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38535.png" alt="Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding poster" width="420">
  - Authors: Jiayun Jin, Haolong Chai, Xueying Huang, Xiaoqing Guo, Zengwei Zheng, Zhan Zhou, Junmei Wang, Xinyu Wang, Jie Liu, Binbin Zhou
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36954) **Uni-Encoder Meets Multi-Encoders: Representation Before Fusion for Brain Tumor Segmentation with Missing Modalities**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Song_Uni-Encoder_Meets_Multi-Encoders_Representation_Before_Fusion_for_Brain_Tumor_Segmentation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.22177) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36954.png" alt="Uni-Encoder Meets Multi-Encoders: Representation Before Fusion for Brain Tumor Segmentation with Missing Modalities poster" width="420">
  - Authors: Peibo Song, Xiaotian Xue, Jinshuo Zhang, zihao wang, Jinhua liu, Shujun Fu, Fangxun Bao, Si Yong Yeo
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38473) **Virtual Full-stack Scanning of Brain MRI via Imputing Any Quantised Code**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Virtual_Full-stack_Scanning_of_Brain_MRI_via_Imputing_Any_Quantised_CVPR_2026_paper.html) [GitHub](https://github.com/ycwu1997/CodeBrain) [Video](https://www.youtube-nocookie.com/embed/oHKOVApCouk) [arXiv](https://arxiv.org/abs/2501.18328) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38473_Bv2IkSb.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38473.png" alt="Virtual Full-stack Scanning of Brain MRI via Imputing Any Quantised Code poster" width="420">
  - Authors: Yicheng Wu, Tao Song, Zhonghua Wu, Jin Ye, Zongyuan Ge, Wenjia Bai, Zhaolin Chen, Jianfei Cai
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38048) **Virtual Nodes Guided Dynamic Graph Neural Network for Brain Tumor Segmentation with Missing Modalities**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Tao_Virtual_Nodes_Guided_Dynamic_Graph_Neural_Network_for_Brain_Tumor_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/oBxp1sjjJzA) [arXiv](https://arxiv.org/abs/2605.16880) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38048.png" alt="Virtual Nodes Guided Dynamic Graph Neural Network for Brain Tumor Segmentation with Missing Modalities poster" width="420">
  - Authors: Sha Tao, Jiao PAN, Yu Guo, Chao Yao
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41023) **Volumetrically Consistent Implicit Atlas Learning via Neural Diffeomorphic Flow for Placenta MRI**
  - Session: Findings Poster Session 2
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37454) **VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rokuss_VoxTell_Free-Text_Promptable_Universal_3D_Medical_Image_Segmentation_CVPR_2026_paper.html) [GitHub](https://github.com/MIC-DKFZ/VoxTell) [Video](https://www.youtube-nocookie.com/embed/enF-YrdY-mI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37454.png" alt="VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation poster" width="420">
  - Authors: Maximilian Rokuss, Moritz Langenberg, Yannick Kirchhoff, Fabian Isensee, Benjamin Hamm, Constantin Ulrich, Sebastian Regnery, Lukas Bauer, Efthimios Katsigiannopulos, Tobias Norajitra, ... (+1 more)
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`

<a id="ct-tomography"></a>
### CT / Tomography

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40545) **3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction**
  - Session: Findings Poster Session 1
  - Tags: `CT / Tomography`, `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37500) **A Supervised Multi-task Framework for Joint cryo-ET Restoration Enabled by Generative Physical Simulation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_A_Supervised_Multi-task_Framework_for_Joint_cryo-ET_Restoration_Enabled_by_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/l6dUjN6fWEU) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37500.png" alt="A Supervised Multi-task Framework for Joint cryo-ET Restoration Enabled by Generative Physical Simulation poster" width="420">
  - Authors: Xinsheng Wang, Zhidong Yang, Xiaohua Wan, Renmin Han, Shuai Tang, Hao Dong, Fa Zhang, Bin Hu
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `CT / Tomography`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36230) **Any2Any 3D Diffusion Models with Knowledge Transfer: A Radiotherapy Planning Study**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Any2Any_3D_Diffusion_Models_with_Knowledge_Transfer_A_Radiotherapy_Planning_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/iWkIgkP-mtU) [arXiv](https://arxiv.org/abs/2605.09622) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36230.png" alt="Any2Any 3D Diffusion Models with Knowledge Transfer: A Radiotherapy Planning Study poster" width="420">
  - Authors: Yuhan Wang, Zihan Li, Han Liu, Simon Arberet, Martin F. Kraus, Yuyin Zhou, Florin-Cristian Ghesu, Dorin Comaniciu, Ali Kamen, Riqiang Gao
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37720) **Beyond the Static-World: Lifelong Learning for All-in-One Medical Image Restoration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shan_Beyond_the_Static-World_Lifelong_Learning_for_All-in-One_Medical_Image_Restoration_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37720.png" alt="Beyond the Static-World: Lifelong Learning for All-in-One Medical Image Restoration poster" width="420">
  - Authors: Shihao Shan, Hongying Liu, Fanhua Shang, Liang Wan, Jingjing Deng
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `Medical AI / General`, `Restoration / Reconstruction`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39371) **Cross-domain Dual-stream Feature Disentanglement for Brain Disorder Prediction with Sparsely Labeled PET**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Cross-domain_Dual-stream_Feature_Disentanglement_for_Brain_Disorder_Prediction_with_Sparsely_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/OJvup4i7O50) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39371.png" alt="Cross-domain Dual-stream Feature Disentanglement for Brain Disorder Prediction with Sparsely Labeled PET poster" width="420">
  - Authors: Huabin Wang, Xinyu Chen, Yuan Zhou, Fei Liu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38658) **CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_CROWn_A_Unified_Framework_for_Anti-Aliased_Downsampling_and_Phase-Calibrated_Fusion_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38658.png" alt="CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation poster" width="420">
  - Authors: Xingru Huang, Shuanghua Ye, Zhao Huang, Wenwen Tang, Huiyu Zhou, Zhiwen Zheng, Jin Liu, Xiaoshuai Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `OCT / Ophthalmology / Retina`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37051) **Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Delving_Aleatoric_Uncertainty_in_Medical_Image_Segmentation_via_Vision_Foundation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.10963) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37051.png" alt="Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models poster" width="420">
  - Authors: Ruiyang Li, Fang Liu, Licheng Jiao, Xinglin Xie, Jiayao Hao, Shuo Li, Xu Liu, Jingyi yang, Lingling Li, Puhua Chen, ... (+1 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36661) **Efficient Unrolled Networks for Large-Scale 3D Inverse Problems**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Vo_Efficient_Unrolled_Networks_for_Large-Scale_3D_Inverse_Problems_CVPR_2026_paper.html) [Project](https://romainvo.github.io/efficient-unrolling/) [Video](https://www.youtube-nocookie.com/embed/ENMY8fVFM9A) [arXiv](https://arxiv.org/abs/2601.02141) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36661.png" alt="Efficient Unrolled Networks for Large-Scale 3D Inverse Problems poster" width="420">
  - Authors: Romain Vo, Julián Tachella
  - Session: Poster Session 6 | Oral Session 6D: Large-Scale Neural Modeling
  - Tags: `X-Ray / Radiography`, `MRI / MR`, `CT / Tomography`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37063) **Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Qiu_Elucidating_the_Design_Space_of_Arbitrary-Noise-Based_Diffusion_Models_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2507.18534) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37063.png" alt="Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models poster" width="420">
  - Authors: Xingyu Qiu, Mengying Yang, Xinghua Ma, Dong Liang, Fanding Li, Gongning Luo, wei wang, Kuanquan Wang, Shuo Li
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Restoration / Reconstruction`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36497) **Exact-GS: Mathematically Rigorous and Accurate 3D Gaussian Splatting for 3D X-ray Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Exact-GS_Mathematically_Rigorous_and_Accurate_3D_Gaussian_Splatting_for_3D_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/MsCFB3z-cJU) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36497.png" alt="Exact-GS: Mathematically Rigorous and Accurate 3D Gaussian Splatting for 3D X-ray Reconstruction poster" width="420">
  - Authors: Guangpu Yang, Steffen Kieß, Hanxiang Luo, Xingyu Liu, Sven Simon
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38379) **Gastric-X: A Multimodal Multi-Phase Benchmark Dataset for Advancing Vision-Language Models in Gastric Cancer Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Gastric-X_A_Multimodal_Multi-Phase_Benchmark_Dataset_for_Advancing_Vision-Language_Models_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/u-wJG8A8JqY) [arXiv](https://arxiv.org/abs/2603.19516) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38379.png" alt="Gastric-X: A Multimodal Multi-Phase Benchmark Dataset for Advancing Vision-Language Models in Gastric Cancer Analysis poster" width="420">
  - Authors: Yuanzhe Li, Hao Chen, Rui Yin, Juyan Ba, Yu Zhang, Sheng Lu
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `CT / Tomography`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40015) **GH-NAF: Grid-Adaptive Hash-Level–Attended Neural Attenuation Fields for Discrepancy-Aware CBCT**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Oh_GH-NAF_Grid-Adaptive_Hash-Level-Attended_Neural_Attenuation_Fields_for_Discrepancy-Aware_CBCT_CVPR_2026_paper.html) [Project](https://limchaeyeon1003.github.io/GH_NAF_CVPR/) [Video](https://www.youtube-nocookie.com/embed/iNo39VR-ieY) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/40015.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40015.png" alt="GH-NAF: Grid-Adaptive Hash-Level–Attended Neural Attenuation Fields for Discrepancy-Aware CBCT poster" width="420">
  - Authors: Seong Je Oh, Ju Hwan Lee, Chae Yeon Lim, Donghwan Lee, Myung Jin Ching, Kyungsu Kim
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38145) **Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Khan_Keep_It_Frozen_Domain-Routed_Conditional_Residual_Modulation_for_Multi-Domain_Vision_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/q18ZYEyK7Tw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38145.png" alt="Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers poster" width="420">
  - Authors: Ufaq Khan, Umair Nawaz, Massimo Caputo, Muhammad Bilal, Junaid Qadir, Muhammad Haris Khan
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37660) **KLIP: Localized Distribution Shift Detection via KL-Divergence with Diffusion Priors in Inverse Problems**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kheirandish_KLIP_Localized_Distribution_Shift_Detection_via_KL-Divergence_with_Diffusion_Priors_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/2ROqNZJZclk) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37660.png" alt="KLIP: Localized Distribution Shift Detection via KL-Divergence with Diffusion Priors in Inverse Problems poster" width="420">
  - Authors: Alireza Kheirandish, Jihoon Hong, Sara Fridovich-Keil
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `CT / Tomography`, `Organs / Anatomy`, `Detection / Diagnosis`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36397) **Learning complete and explainable visual representations from itemized text supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_Learning_complete_and_explainable_visual_representations_from_itemized_text_supervision_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/X9lDEqtVGpo) [arXiv](https://arxiv.org/abs/2512.11141) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36397.png" alt="Learning complete and explainable visual representations from itemized text supervision poster" width="420">
  - Authors: Yiwei Lyu, Chenhui Zhao, Soumyanil Banerjee, Shixuan Liu, Akshay Rao, Akhil Kondepudi, Honglak Lee, Todd C. Hollon
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39688) **Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Matinkia_Learning_Diffeomorphism_for_Medical_Image_Registration_with_Time-Embedded_Architectures_Using_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/ss_GC9hi-7k) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39688.png" alt="Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization poster" width="420">
  - Authors: Mohammadjavad Matinkia, Nilanjan Ray
  - Session: Poster Session 5 & Exhibit Hall | Oral Session 5C: Geometry and Robotics
  - Tags: `CT / Tomography`, `Medical AI / General`, `Registration`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36666) **Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Learning_Generalizable_3D_Medical_Image_Representations_from_Mask-Guided_Self-Supervision_CVPR_2026_paper.html) [GitHub](https://github.com/Stanford-AIMI/MASS?tab=readme-ov-file) [arXiv](https://arxiv.org/abs/2603.13660) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36666.png" alt="Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision poster" width="420">
  - Authors: Yunhe Gao, Yabin Zhang, Chong Wang, Jiaming Liu, Maya Varma, Jean-Benoit Delbrouck, Akshay Chaudhari, Curtis Langlotz
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37934) **MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_MorphSeek_Fine-grained_Latent_Representation-Level_Policy_Optimization_for_Deformable_Image_Registration_CVPR_2026_paper.html) [GitHub](https://github.com/cai114514/MorphSeek) [Video](https://www.youtube-nocookie.com/embed/DGljUXt-A_w) [arXiv](https://arxiv.org/abs/2511.17392) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37934.png" alt="MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration poster" width="420">
  - Authors: Runxun Zhang, Yizhou Liu, Dongrui Li, Bo XU, Jingwei Wei
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Registration`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39104) **PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Maqbool_PETAR_Localized_Findings_Generation_with_Mask-Aware_Vision-Language_Modeling_for_PET_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/vlHR_NcGlDs) [arXiv](https://arxiv.org/abs/2510.27680) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39104.png" alt="PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting poster" width="420">
  - Authors: Danyal Maqbool, Changhee Lee, Zachary Huemann, Samuel D. Church, Matthew E. Larson, Scott B. Perlman, Tomas A. Romero, Joshua D. Warner, Meghan Lubner, Xin Tie, ... (+4 more)
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41016) **PTF-CT: Polar-Aware Temporal-Frequential Iterative Reconstruction for Sparse-View CT**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41013) **Rethinking Whole-Body CT Image Interpretation: An Abnormality-Centric Approach**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36920) **Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Revisiting_Pose_Sensitivity_in_Splat-based_Computed_Tomography_under_Sparse-view_Reconstruction_CVPR_2026_paper.html) [Project](https://vclab.kaist.ac.kr/cvpr2026p2/) [Video](https://www.youtube-nocookie.com/embed/vqliZ-OyNIg) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36920.png" alt="Revisiting Pose Sensitivity in Splat-based Computed Tomography under Sparse-view Reconstruction poster" width="420">
  - Authors: Kiseok Choi, Hyeongjun Cho, Inchul Kim, Min H. Kim
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36984) **Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Claessens_Scaling_Self-Supervised_and_Cross-Modal_Pretraining_for_Volumetric_CT_Transformers_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/tFdLkc0v998) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36984.png" alt="Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers poster" width="420">
  - Authors: Cris Claessens, Christiaan Viviers, Giacomo D&amp;#x27;Amicantonio, Egor Bondarev, Fons van der Sommen
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36495) **SHAPE: Structure-aware Hierarchical Unsupervised Domain Adaptation with Plausibility Evaluation for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_SHAPE_Structure-aware_Hierarchical_Unsupervised_Domain_Adaptation_with_Plausibility_Evaluation_for_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/4Y3OLaeNn0Y) [arXiv](https://arxiv.org/abs/2603.21904) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36495.png" alt="SHAPE: Structure-aware Hierarchical Unsupervised Domain Adaptation with Plausibility Evaluation for Medical Image Segmentation poster" width="420">
  - Authors: Linkuan Zhou, Yinghao Xia, Yufei Shen, Xiangyu Li, Wenjie Du, Cong Cong, leyi wei, Ran Su, Qiangguo Jin
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36477) **Sketch2CT: Multimodal Diffusion for Structure-Aware 3D Medical Volume Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/An_Sketch2CT_Multimodal_Diffusion_for_Structure-Aware_3D_Medical_Volume_Generation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/RiNNzMcykok) [arXiv](https://arxiv.org/abs/2603.22509) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36477.png" alt="Sketch2CT: Multimodal Diffusion for Structure-Aware 3D Medical Volume Generation poster" width="420">
  - Authors: Delin An, Chaoli Wang
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Segmentation`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38465) **Splat-Based Metal Artifact Reduction in Cone-Beam CT via Compact Attenuation Modeling**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Splat-Based_Metal_Artifact_Reduction_in_Cone-Beam_CT_via_Compact_Attenuation_CVPR_2026_paper.html) [Project](https://vclab.kaist.ac.kr/cvpr2026p1/) [Video](https://www.youtube-nocookie.com/embed/eBYZAX7rQPw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38465.png" alt="Splat-Based Metal Artifact Reduction in Cone-Beam CT via Compact Attenuation Modeling poster" width="420">
  - Authors: Kiseok Choi, Jaemin Cho, Inchul Kim, Min H. Kim
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Segmentation`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38535) **Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_Ultrasound-CLIP_Semantic-Aware_Contrastive_Pre-training_for_Ultrasound_Image-Text_Understanding_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/p5AF42K_oz4) [arXiv](https://arxiv.org/abs/2604.01749) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38535.png" alt="Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding poster" width="420">
  - Authors: Jiayun Jin, Haolong Chai, Xueying Huang, Xiaoqing Guo, Zengwei Zheng, Zhan Zhou, Junmei Wang, Xinyu Wang, Jie Liu, Binbin Zhou
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39706) **Unsupervised Multi-Scale Segmentation of 3D Subcellular World with Stable Diffusion Foundation Model**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Uddin_Unsupervised_Multi-Scale_Segmentation_of_3D_Subcellular_World_with_Stable_Diffusion_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/XfIVZ06FeT8) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39706.png" alt="Unsupervised Multi-Scale Segmentation of 3D Subcellular World with Stable Diffusion Foundation Model poster" width="420">
  - Authors: Mostofa Uddin Uddin, HM Shadman Tabib, Thanh-Huy Nguyen, Kashish Gandhi, Min Xu
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `CT / Tomography`, `Segmentation`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38695) **VesMamba: 3D Pulmonary Vessel Segmentation from CT images via Mamba with Structural Perception and Scale-aware Filtering**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_VesMamba_3D_Pulmonary_Vessel_Segmentation_from_CT_images_via_Mamba_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/vtGF79QAQyM) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38695.png" alt="VesMamba: 3D Pulmonary Vessel Segmentation from CT images via Mamba with Structural Perception and Scale-aware Filtering poster" width="420">
  - Authors: Zhipeng Liu, Guilian Chen, Zheng Jiang, Huisi Wu, Jing Qin
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `CT / Tomography`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41024) **Vision-Language Models for Automated 3D PET/CT Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `PET / Nuclear Medicine`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37454) **VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rokuss_VoxTell_Free-Text_Promptable_Universal_3D_Medical_Image_Segmentation_CVPR_2026_paper.html) [GitHub](https://github.com/MIC-DKFZ/VoxTell) [Video](https://www.youtube-nocookie.com/embed/enF-YrdY-mI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37454.png" alt="VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation poster" width="420">
  - Authors: Maximilian Rokuss, Moritz Langenberg, Yannick Kirchhoff, Fabian Isensee, Benjamin Hamm, Constantin Ulrich, Sebastian Regnery, Lukas Bauer, Efthimios Katsigiannopulos, Tobias Norajitra, ... (+1 more)
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36840) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_X-WIN_Building_Chest_Radiograph_World_Model_via_Predictive_Sensing_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/ZzPPjRx9hDI) [arXiv](https://arxiv.org/abs/2511.14918) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36840.png" alt="X-WIN: Building Chest Radiograph World Model via Predictive Sensing poster" width="420">
  - Authors: Zefan Yang, Ge Wang, James Hendler, Mannudeep K. Kalra, Pingkun Yan
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`

<a id="pet-nuclear-medicine"></a>
### PET / Nuclear Medicine

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37720) **Beyond the Static-World: Lifelong Learning for All-in-One Medical Image Restoration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shan_Beyond_the_Static-World_Lifelong_Learning_for_All-in-One_Medical_Image_Restoration_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37720.png" alt="Beyond the Static-World: Lifelong Learning for All-in-One Medical Image Restoration poster" width="420">
  - Authors: Shihao Shan, Hongying Liu, Fanhua Shang, Liang Wan, Jingjing Deng
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `Medical AI / General`, `Restoration / Reconstruction`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39371) **Cross-domain Dual-stream Feature Disentanglement for Brain Disorder Prediction with Sparsely Labeled PET**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Cross-domain_Dual-stream_Feature_Disentanglement_for_Brain_Disorder_Prediction_with_Sparsely_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/OJvup4i7O50) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39371.png" alt="Cross-domain Dual-stream Feature Disentanglement for Brain Disorder Prediction with Sparsely Labeled PET poster" width="420">
  - Authors: Huabin Wang, Xinyu Chen, Yuan Zhou, Fei Liu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36666) **Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Learning_Generalizable_3D_Medical_Image_Representations_from_Mask-Guided_Self-Supervision_CVPR_2026_paper.html) [GitHub](https://github.com/Stanford-AIMI/MASS?tab=readme-ov-file) [arXiv](https://arxiv.org/abs/2603.13660) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36666.png" alt="Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision poster" width="420">
  - Authors: Yunhe Gao, Yabin Zhang, Chong Wang, Jiaming Liu, Maya Varma, Jean-Benoit Delbrouck, Akshay Chaudhari, Curtis Langlotz
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37473) **PET-DINO: Unifying Visual Cues into Grounding DINO with Prompt-Enriched Training**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Fu_PET-DINO_Unifying_Visual_Cues_into_Grounding_DINO_with_Prompt-Enriched_Training_CVPR_2026_paper.html) [Project](https://fuweifuvtoo.github.io/pet-dino) [Video](https://www.youtube-nocookie.com/embed/aTY34kY1wlc) [arXiv](https://arxiv.org/abs/2604.00503) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37473.png" alt="PET-DINO: Unifying Visual Cues into Grounding DINO with Prompt-Enriched Training poster" width="420">
  - Authors: Weifu Fu, Jinyang Li, Bin-Bin Gao, Jialin Li, Yuhuan Lin, Hanqiu Deng, Wenbing Tao, Yong Liu, Chengjie Wang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `PET / Nuclear Medicine`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39104) **PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Maqbool_PETAR_Localized_Findings_Generation_with_Mask-Aware_Vision-Language_Modeling_for_PET_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/vlHR_NcGlDs) [arXiv](https://arxiv.org/abs/2510.27680) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39104.png" alt="PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting poster" width="420">
  - Authors: Danyal Maqbool, Changhee Lee, Zachary Huemann, Samuel D. Church, Matthew E. Larson, Scott B. Perlman, Tomas A. Romero, Joshua D. Warner, Meghan Lubner, Xin Tie, ... (+4 more)
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41024) **Vision-Language Models for Automated 3D PET/CT Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `PET / Nuclear Medicine`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37454) **VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rokuss_VoxTell_Free-Text_Promptable_Universal_3D_Medical_Image_Segmentation_CVPR_2026_paper.html) [GitHub](https://github.com/MIC-DKFZ/VoxTell) [Video](https://www.youtube-nocookie.com/embed/enF-YrdY-mI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37454.png" alt="VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation poster" width="420">
  - Authors: Maximilian Rokuss, Moritz Langenberg, Yannick Kirchhoff, Fabian Isensee, Benjamin Hamm, Constantin Ulrich, Sebastian Regnery, Lukas Bauer, Efthimios Katsigiannopulos, Tobias Norajitra, ... (+1 more)
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`

<a id="oct-ophthalmology-retina"></a>
### OCT / Ophthalmology / Retina

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38658) **CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_CROWn_A_Unified_Framework_for_Anti-Aliased_Downsampling_and_Phase-Calibrated_Fusion_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38658.png" alt="CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation poster" width="420">
  - Authors: Xingru Huang, Shuanghua Ye, Zhao Huang, Wenwen Tang, Huiyu Zhou, Zhiwen Zheng, Jin Liu, Xiaoshuai Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `OCT / Ophthalmology / Retina`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39174) **D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_D-Convexity_A_Unified_Differentiable_Convex_Shape_Prior_via_Quasi-Concavity_for_CVPR_2026_paper.html) [Project](https://hyan46.github.io/chen-dconvexity-cvpr-2026/) [Video](https://www.youtube-nocookie.com/embed/psPB5l9wR-w) [arXiv](https://arxiv.org/abs/2605.19210) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39174.png" alt="D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation poster" width="420">
  - Authors: Shengzhe Chen, Hao Yan
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `OCT / Ophthalmology / Retina`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41036) **Gaze into the Details: Locality-Sensitive Enhancement for OCTA Retinal Vessel Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41014) **Generative Vision-Language Multiple Instance Learning for Weakly Supervised Neonatal Fundus Screening and Reporting**
  - Session: Findings Poster Session 2
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38440) **MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Deria_MedMO_Grounding_and_Understanding_Multimodal_Large_Language_Model_for_Medical_CVPR_2026_paper.html) [Project](https://genmilab.github.io/MedMO-Page) [Video](https://www.youtube-nocookie.com/embed/xax7e0fMMGI) [arXiv](https://arxiv.org/abs/2602.06965) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38440.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38440.png" alt="MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images poster" width="420">
  - Authors: Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre, Eran Segal, Salman Khan, Imran Razzak
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39276) **Post-training Feature Pruning for Fundus Images Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pham_Post-training_Feature_Pruning_for_Fundus_Images_Classification_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/qEEuHYZZbhk) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39276.png" alt="Post-training Feature Pruning for Fundus Images Classification poster" width="420">
  - Authors: Van-Nguyen Pham, Duc-Tai Le, Junghyun Bum, Hyunseung Choo
  - Session: Poster Session 6
  - Tags: `OCT / Ophthalmology / Retina`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36379) **Real2Sim2Real: RetinalDepth-64K for Depth Estimation in Posterior Segment Ophthalmic Surgery**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_Real2Sim2Real_RetinalDepth-64K_for_Depth_Estimation_in_Posterior_Segment_Ophthalmic_Surgery_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Bingwen Dong, Gan Liu, Xiaoxi Lu, Guangcheng Chen, Jialu ZHANG, Yan Hu, Xiaoqing Zhang, Jiang Liu
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `OCT / Ophthalmology / Retina`, `Surgery / Medical Video`, `Segmentation`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38227) **X-PCR: A Benchmark for Cross-modality Progressive Clinical Reasoning in Ophthalmic Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_X-PCR_A_Benchmark_for_Cross-modality_Progressive_Clinical_Reasoning_in_Ophthalmic_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/1g_Y7gnAYtU) [arXiv](https://arxiv.org/abs/2604.20350) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38227.png" alt="X-PCR: A Benchmark for Cross-modality Progressive Clinical Reasoning in Ophthalmic Diagnosis poster" width="420">
  - Authors: Gui Wang, Zehao Zhong, YongSong Zhou, Yudong Li, Ende Wu, Wooi Ping Cheah, Rong Qu, Jianfeng Ren, Linlin Shen
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `OCT / Ophthalmology / Retina`, `Medical AI / General`, `Detection / Diagnosis`

<a id="pathology-microscopy-cells"></a>
### Pathology / Microscopy / Cells

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40545) **3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction**
  - Session: Findings Poster Session 1
  - Tags: `CT / Tomography`, `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41049) **A Denoising-Enhanced Multimodal Learning Framework for Robust Nasal Endoscopy Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41020) **A Simple yet Effective Data Scaling Strategy for Semi-Supervised Medical Image Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41028) **AceMIL: Ordinal-Aware Multiple Instance Learning for Pathological Progression Analysis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36280) **Act Like a Pathologist: Tissue-Aware Whole Slide Image Reasoning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Act_Like_a_Pathologist_Tissue-Aware_Whole_Slide_Image_Reasoning_CVPR_2026_paper.html) [GitHub](https://github.com/winston52/HistoSelect) [Video](https://www.youtube-nocookie.com/embed/kr1NcK5NBxg) [arXiv](https://arxiv.org/abs/2603.00667) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/36280.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36280.png" alt="Act Like a Pathologist: Tissue-Aware Whole Slide Image Reasoning poster" width="420">
  - Authors: Wentao Huang, Weimin Lyu, Peiliang Lou, Qingqiao Hu, Xiaoling Hu, Shahira Abousamra, Wenchao Han, Ruifeng Guo, Jiawei Zhou, Chao Chen, ... (+1 more)
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39832) **Advancing Cancer Prognosis with Hierarchical Fusion of Genomic, Proteomic and Pathology Imaging Data from a Systems Biology Perspective**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Advancing_Cancer_Prognosis_with_Hierarchical_Fusion_of_Genomic_Proteomic_and_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.13787) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39832.png" alt="Advancing Cancer Prognosis with Hierarchical Fusion of Genomic, Proteomic and Pathology Imaging Data from a Systems Biology Perspective poster" width="420">
  - Authors: Junjie Zhou, Bao Xue, Meiling Wang, WEI SHAO, Daoqiang Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41056) **Anatomy-Aware Adaptive Feature Perturbation Framework for Semi-Supervised MRI Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41030) **Anatomy-CoT: Teaching MLLMs to Reason in Radiology**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37248) **Beyond Pixel Simulation: Pathology Image Generation via Diagnostic Semantic Tokens and Prototype Control**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Beyond_Pixel_Simulation_Pathology_Image_Generation_via_Diagnostic_Semantic_Tokens_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.21058) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37248.png" alt="Beyond Pixel Simulation: Pathology Image Generation via Diagnostic Semantic Tokens and Prototype Control poster" width="420">
  - Authors: Minghao Han, Yichen Liu, Yizhou Liu, Zizhi Chen, Jingqun Tang, Xuecheng Wu, Dingkang Yang, Lihua Zhang
  - Session: Poster Session 6
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41061) **BLEG: LLM Functions as Powerful fMRI Graph-Enhancer for Brain Network Analysis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36389) **Bridging RGB and Hematoxylin Components: An Interleaved Guidance and Fusion Framework for Point Supervised Nuclei Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huan_Bridging_RGB_and_Hematoxylin_Components_An_Interleaved_Guidance_and_Fusion_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/sSkEBEog0Ts) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36389.png" alt="Bridging RGB and Hematoxylin Components: An Interleaved Guidance and Fusion Framework for Point Supervised Nuclei Segmentation poster" width="420">
  - Authors: Zihan Huan, Xipeng Pan, Hualong Zhang, Siyang Feng, Rushi Lan, Huadeng Wang, Haoxiang Lu, Zhenbing Liu
  - Session: Poster Session 6
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39956) **Building Robust Vision Encoders for Cross-Dataset Evaluation in Immunofluorescent Microscopy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Marikkar_Building_Robust_Vision_Encoders_for_Cross-Dataset_Evaluation_in_Immunofluorescent_Microscopy_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39956.png" alt="Building Robust Vision Encoders for Cross-Dataset Evaluation in Immunofluorescent Microscopy poster" width="420">
  - Authors: Umar Marikkar, Syed Sameed Husain, Muhammad Awais, Sara Atito
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41041) **C3-Diff: Super-resolving Spatial Transcriptomics via Cross-modal Cross-content Contrastive Diffusion Modelling**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38354) **CARE: A Molecular-Guided Foundation Model with Adaptive Region Modeling for Whole Slide Image Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_CARE_A_Molecular-Guided_Foundation_Model_with_Adaptive_Region_Modeling_for_CVPR_2026_paper.html) [GitHub](https://github.com/zdipath/CARE) [arXiv](https://arxiv.org/abs/2602.21637) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38354.png" alt="CARE: A Molecular-Guided Foundation Model with Adaptive Region Modeling for Whole Slide Image Analysis poster" width="420">
  - Authors: Di Zhang, Zhangpeng Gong, Xiaobo Pang, Jiashuai Liu, Junbo Lu, Hao Cui, Jiusong Ge, Zhi Zeng, Kai Yi, Yinghua Li, ... (+7 more)
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37175) **Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Nishimura_Cell-Type_Prototype-Informed_Neural_Network_for_Gene_Expression_Estimation_from_Pathology_CVPR_2026_paper.html) [Project](https://naivete5656.github.io/CPNN/) [Video](https://www.youtube-nocookie.com/embed/_ak55qv_eO0) [arXiv](https://arxiv.org/abs/2603.18461) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/37175.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37175.png" alt="Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images poster" width="420">
  - Authors: Kazuya Nishimura, Ryoma Bise, Shinnosuke Matsuo, Haruka Hirose, Yasuhiro Kojima
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39693) **Clinically-Grounded Counterfactual Reasoning for Medical Video Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Clinically-Grounded_Counterfactual_Reasoning_for_Medical_Video_Diagnosis_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39693.png" alt="Clinically-Grounded Counterfactual Reasoning for Medical Video Diagnosis poster" width="420">
  - Authors: Jianzhe Gao, Churan Wang, Weiyi Zhang, Jianghua Li, Lian Li, Wenguan Wang, Yixin Zhu, Yizhou Wang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37150) **Contrastive Cross-Bag Augmentation for Multiple Instance Learning-based Whole Slide Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Contrastive_Cross-Bag_Augmentation_for_Multiple_Instance_Learning-based_Whole_Slide_Image_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/lRJE3Q40SKQ) [arXiv](https://arxiv.org/abs/2508.03081) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37150.png" alt="Contrastive Cross-Bag Augmentation for Multiple Instance Learning-based Whole Slide Image Classification poster" width="420">
  - Authors: Bo Zhang, Xu Xinan, Shuo Yan, Yu Bai, Zheng Zhang, Wufan Wang, Hui Gao, Wendong Wang
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Cancer / Tumor / Lesion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38037) **Cross-Slice Knowledge Transfer via Masked Multi-Modal Heterogeneous Graph Contrastive Learning for Spatial Gene Expression Inference**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Cross-Slice_Knowledge_Transfer_via_Masked_Multi-Modal_Heterogeneous_Graph_Contrastive_Learning_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.22821) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38037.png" alt="Cross-Slice Knowledge Transfer via Masked Multi-Modal Heterogeneous Graph Contrastive Learning for Spatial Gene Expression Inference poster" width="420">
  - Authors: Zhiceng Shi, Changmiao Wang, Jun Wan, Wenwen Min
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37706) **CryoHype: Reconstructing a thousand cryo-EM structures with transformer-based hypernetworks**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_CryoHype_Reconstructing_a_thousand_cryo-EM_structures_with_transformer-based_hypernetworks_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/zAtY-CtybbM) [arXiv](https://arxiv.org/abs/2512.06332) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37706.png" alt="CryoHype: Reconstructing a thousand cryo-EM structures with transformer-based hypernetworks poster" width="420">
  - Authors: Jeffrey Gu, Minkyu Jeon, Ambri Ma, Serena Yeung, Ellen D. Zhong
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39878) **CryoKRAQEN: Kernel-Regularized Annealing for Quantized Embedding Networks in Cryo-EM Heterogeneous Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_CryoKRAQEN_Kernel-Regularized_Annealing_for_Quantized_Embedding_Networks_in_Cryo-EM_Heterogeneous_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/rAibn18_RUE) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39878.png" alt="CryoKRAQEN: Kernel-Regularized Annealing for Quantized Embedding Networks in Cryo-EM Heterogeneous Reconstruction poster" width="420">
  - Authors: Wenyuan Gao, Yutan Wu, Xuming He
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37942) **cryoSENSE: Compressive Sensing Enables High-throughput Microscopy with Sparse and Generative Priors on the Protein Cryo-EM Image Manifold**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shabeeb_cryoSENSE_Compressive_Sensing_Enables_High-throughput_Microscopy_with_Sparse_and_Generative_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/_KH-q_lfvCI) [arXiv](https://arxiv.org/abs/2511.12931) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37942.png" alt="cryoSENSE: Compressive Sensing Enables High-throughput Microscopy with Sparse and Generative Priors on the Protein Cryo-EM Image Manifold poster" width="420">
  - Authors: Zain Shabeeb, Daniel Saeedi, Darin Tsui, Vida Jamali, Amirali Aghazadeh
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39283) **Deconstructing the Failure of Ideal Noise Correction: A Three-Pillar Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Deconstructing_the_Failure_of_Ideal_Noise_Correction_A_Three-Pillar_Diagnosis_CVPR_2026_paper.html) [Project](https://mrchenfeng.github.io) [arXiv](https://arxiv.org/abs/2603.12997) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39283.png" alt="Deconstructing the Failure of Ideal Noise Correction: A Three-Pillar Diagnosis poster" width="420">
  - Authors: Chen Feng, Zhuo ZHI, Zhao Huang, Jiawei Ge, Ling Xiao, Nicu Sebe, Georgios Tzimiropoulos, Ioannis Patras
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41011) **Deep-to-Shallow Knowledge Transfer:Multi-Scale Self-Distillation with Bidirectional Aware for 3D Brain Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41031) **DELRER: Disease Evolution-Informed Longitudinal Radiology Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41021) **DepthScopy: Decoupling Frequency for Endoscopic Depth Estimation in Sparsely-Textured Regions**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37060) **DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_DK-DDIL_Adaptive_Knowledge_Retention_for_Dynamic_Domain-Incremental_Learning_in_Medical_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37060.png" alt="DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging poster" width="420">
  - Authors: Yuxi Ma, Sujie Liu, Jing Yang, Jiacheng Wang, Yiping Chen, Baptiste Magnier, Liansheng Wang
  - Session: Poster Session 6 | Oral Session 6C: Medical Vision
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41046) **Do Vision Models Perceive Illusory Motion in Static Images Like Humans?**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39550) **Dual-Level Hypergraph Generation for Addressing Feature Scarcity in Whole-Slide Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yao_Dual-Level_Hypergraph_Generation_for_Addressing_Feature_Scarcity_in_Whole-Slide_Image_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39550.png" alt="Dual-Level Hypergraph Generation for Addressing Feature Scarcity in Whole-Slide Image Classification poster" width="420">
  - Authors: Shuilian Yao, Qi Jia, Qi Jia, Pengshuo Zhang, Lili Sun, Weimin Wang, Yanmei Zhu, Bo Zhang, Xin Fan
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39099) **Dynamics-Aware Preference Optimization for Vision-Language Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Dynamics-Aware_Preference_Optimization_for_Vision-Language_Models_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: jusheng zhang, Kaitong Cai, Jing Yang, Jian Wang, Keze Wang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41033) **DynaMind: Reconstructing Dynamic Visual Scenes from EEG by Aligning Temporal Dynamics and Multimodal Semantics to Guided Diffusion**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41057) **EI: Early Intervention for Multimodal Imaging Based Disease Recognition**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41055) **Elicit and Enhance: Advancing Multimodal Reasoning in Medical Scenarios**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39195) **EMGauss: Continuous Slice-to-3D Reconstruction via Dynamic Gaussian Modeling in Volume Electron Microscopy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/He_EMGauss_Continuous_Slice-to-3D_Reconstruction_via_Dynamic_Gaussian_Modeling_in_Volume_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.06684) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Yumeng He, Zanwei Zhou, Yekun Zheng, Chen Liang, Yunbo Wang, Xiaokang Yang
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37520) **Every Error has Its Magnitude: Asymmetric Mistake Severity Training for Multiclass Multiple Instance Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hong_Every_Error_has_Its_Magnitude_Asymmetric_Mistake_Severity_Training_for_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/MUjVlI-wZTI) [arXiv](https://arxiv.org/abs/2603.13682) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37520.png" alt="Every Error has Its Magnitude: Asymmetric Mistake Severity Training for Multiclass Multiple Instance Learning poster" width="420">
  - Authors: Sungrae Hong, Jiwon Jeong, Jisu Shin, Donghee Han, Sol Lee, Kyungeun Kim, Mun Yong Yi
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37778) **Factorized Context Aggregation for Robust Cancer Risk Estimation via Soft Re-Ranked Retrieval and Hierarchical Anchors**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Moghadam_Factorized_Context_Aggregation_for_Robust_Cancer_Risk_Estimation_via_Soft_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/0tQ3-O0yX44) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37778-thumb.png" alt="Factorized Context Aggregation for Robust Cancer Risk Estimation via Soft Re-Ranked Retrieval and Hierarchical Anchors poster" width="420">
  - Authors: Puria Azadi Moghadam, Ali Khajegili Mirabadi, Behnam Maneshgar, Hossein Farahani, Ali Bashashati
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39052) **FBTA: Enabling Single-GPU End-to-End Gigapixel WSI Classification with Feature Bridging and Translation Alignment**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_FBTA_Enabling_Single-GPU_End-to-End_Gigapixel_WSI_Classification_with_Feature_Bridging_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Jiuyang Dong, Jiahan Li, Junjun Jiang, Yongbing Zhang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40217) **FluoCLIP: Stain-Aware Focus Quality Assessment in Fluorescence Microscopy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Park_FluoCLIP_Stain-Aware_Focus_Quality_Assessment_in_Fluorescence_Microscopy_CVPR_2026_paper.html) [Project](https://fluoclip.github.io/) [Video](https://www.youtube-nocookie.com/embed/28aVZ3YTohU) [arXiv](https://arxiv.org/abs/2602.23791) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40217.png" alt="FluoCLIP: Stain-Aware Focus Quality Assessment in Fluorescence Microscopy poster" width="420">
  - Authors: Hyejin Park, Jiwon Yoon, Sumin Park, Suree Kim, Sinae Jang, Eunsoo Lee, Dongmin Kang, Dongbo Min
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical VLM / VQA / Reasoning`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41027) **From Adaptation to Generalization: Adaptive Visual Prompting for Medical Image Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41052) **Gated Differential Linear Attention: A Linear-Time Decoder for High-Fidelity Medical Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39074) **GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kong_GaussianPile_A_Unified_Sparse_Gaussian_Splatting_Framework_for_Slice-based_Volumetric_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/0UNUSuksZzY) [arXiv](https://arxiv.org/abs/2603.20611) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39074.png" alt="GaussianPile: A Unified Sparse Gaussian Splatting Framework for Slice-based Volumetric Reconstruction poster" width="420">
  - Authors: Di Kong, Yikai Wang, Wenjie Guo, Yifan Bu, Boya Zhang, Yuexin Duan, Xiawei Yue, Wenbiao Du, Yiman Zhong, Yuwen Chen, ... (+1 more)
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `Pathology / Microscopy / Cells`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41036) **Gaze into the Details: Locality-Sensitive Enhancement for OCTA Retinal Vessel Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41014) **Generative Vision-Language Multiple Instance Learning for Weakly Supervised Neonatal Fundus Screening and Reporting**
  - Session: Findings Poster Session 2
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38090) **GeneVAR: Causal MeanFlow for Autoregressive Gene-to-WSI Tile Synthesis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_GeneVAR_Causal_MeanFlow_for_Autoregressive_Gene-to-WSI_Tile_Synthesis_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/tbAYSmYHAhI) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38090_rjx4RQq.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38090.png" alt="GeneVAR: Causal MeanFlow for Autoregressive Gene-to-WSI Tile Synthesis poster" width="420">
  - Authors: Jianwei Zhao, Fan Yang, XIN LI, Qiang Zhai, Ao Luo, Ziqi Ren, Zhicheng Jiao, Hong Cheng
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36716) **H2-Surv: Hierarchical Hyperbolic Multimodal Representation Learning for Survival Prediction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_H2-Surv_Hierarchical_Hyperbolic_Multimodal_Representation_Learning_for_Survival_Prediction_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/hk2KEFuY-S8) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36716.png" alt="H2-Surv: Hierarchical Hyperbolic Multimodal Representation Learning for Survival Prediction poster" width="420">
  - Authors: Jiaqi Yang, Wenting Chen, Xiangjian He, Yuanbai Li, Sen Yang, Linlin Shen, Xiaohan Xing
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Cancer / Tumor / Lesion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41059) **HazeMatching: Dehazing Light Microscopy Images with Guided Conditional Flow Matching**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39159) **HyperST: Hierarchical Hyperbolic Learning for Spatial Transcriptomics Prediction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_HyperST_Hierarchical_Hyperbolic_Learning_for_Spatial_Transcriptomics_Prediction_CVPR_2026_paper.html) [GitHub](https://github.com/liesgame/HyperST) [Video](https://www.youtube-nocookie.com/embed/QLru19GiigM) [arXiv](https://arxiv.org/abs/2511.22107) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/39159.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39159.png" alt="HyperST: Hierarchical Hyperbolic Learning for Spatial Transcriptomics Prediction poster" width="420">
  - Authors: Chen Zhang, Yilu An, Ying Chen, Hao Li, Xitong Ling, Lihao Liu, Junjun He, Yuxiang Lin, Zihui Wang, Rongshan Yu
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38051) **Intervention-Aware Multiscale Representation Learning from Imaging Phenomics and Perturbation Transcriptomics**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Intervention-Aware_Multiscale_Representation_Learning_from_Imaging_Phenomics_and_Perturbation_Transcriptomics_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.22832) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38051.png" alt="Intervention-Aware Multiscale Representation Learning from Imaging Phenomics and Perturbation Transcriptomics poster" width="420">
  - Authors: Jiayuan Chen, Ruoqi Liu, Zishan Gu, Ping Zhang
  - Session: Poster Session 6
  - Tags: `Pathology / Microscopy / Cells`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37003) **IVAAN: Instance-level Vision-Language Alignment via Attribute-Guided Text Prompts Generation for Nuclei Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_IVAAN_Instance-level_Vision-Language_Alignment_via_Attribute-Guided_Text_Prompts_Generation_for_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/F6fSCuKL9Hs) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37003.png" alt="IVAAN: Instance-level Vision-Language Alignment via Attribute-Guided Text Prompts Generation for Nuclei Analysis poster" width="420">
  - Authors: Jaehoon Jeong, Yi Hu, Soopil Kim, Jongseong Jang, Soonyoung Lee, Sang Hyun Park
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38708) **KAMP: Knowledge-Anchored Multimodal Pretraining Framework for Medical Image Representation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_KAMP_Knowledge-Anchored_Multimodal_Pretraining_Framework_for_Medical_Image_Representation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/rU4ie5wfIVg) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38708.png" alt="KAMP: Knowledge-Anchored Multimodal Pretraining Framework for Medical Image Representation poster" width="420">
  - Authors: Feiyu Huang, Jia Li, Zhao CHEN, Yang WU, Caleb Chen Cao, Lei Chen
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41017) **Learning from Noisy Prompts: Saliency-Guided Prompt Distillation for Robust Segmentation with SAM**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41060) **Learning Priors via Hybrid Visual Autoregressive Modeling for Medical Image to Image Translation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41043) **Learning Spatial-Preserving Hierarchical Representations for Digital Pathology**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38951) **LUMINA: A Multi-Vendor Mammography Benchmark with Energy Harmonization Protocol**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_LUMINA_A_Multi-Vendor_Mammography_Benchmark_with_Energy_Harmonization_Protocol_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/rtUfsZegJCM) [arXiv](https://arxiv.org/abs/2603.14644) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38951.png" alt="LUMINA: A Multi-Vendor Mammography Benchmark with Energy Harmonization Protocol poster" width="420">
  - Authors: Hongyi Pan, Gorkem Durak, Halil Ertugrul Aktas, Andrea M. Bejar, Baver Tutun, Emre Uysal, Ezgi Bülbül, Mehmet Faith Dogan, Berrin Erok, Berna Yildirim, ... (+2 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Mammography / Breast`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41037) **M^3D-BFS: a Multi-Stage Dynamic Fusion Strategy for Sample-Adaptive Multi-Modal Brain Network Analysis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41032) **M^4Fuse: Lightweight State-Space MoE with a Cross-Scale Gating Bridge for Brain Tumor Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41034) **MAE-XNT: A Foundation Model for Segmenting Neuronal Tissue Volumes Generated with X-Ray Nanotomography**
  - Session: Findings Poster Session 2
  - Tags: `X-Ray / Radiography`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38829) **MDCS-MoAME: Multi-directional Composite Scanning with Mixture of Attention and Mamba Experts for Cancer Survival Prediction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Qu_MDCS-MoAME_Multi-directional_Composite_Scanning_with_Mixture_of_Attention_and_Mamba_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/3sLmvKC54OM) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38829.png" alt="MDCS-MoAME: Multi-directional Composite Scanning with Mixture of Attention and Mamba Experts for Cancer Survival Prediction poster" width="420">
  - Authors: Linjie Qu, Jin Xiao, Xiangrong Liu, Changming Sun, Hui Cui, Yuqi Fang, Ran Su, Qiangguo Jin, leyi wei
  - Session: Poster Session 3 & Exhibit Hall | Oral Session 3D: Multimodal Modeling
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38440) **MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Deria_MedMO_Grounding_and_Understanding_Multimodal_Large_Language_Model_for_Medical_CVPR_2026_paper.html) [Project](https://genmilab.github.io/MedMO-Page) [Video](https://www.youtube-nocookie.com/embed/xax7e0fMMGI) [arXiv](https://arxiv.org/abs/2602.06965) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38440.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38440.png" alt="MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images poster" width="420">
  - Authors: Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre, Eran Segal, Salman Khan, Imran Razzak
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41012) **MedSAD-CLIP: Supervised CLIP with Token-Patch Cross-Attention for Medical Anomaly Detection and Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41042) **MeMix: Multi-Encoder Mixture Framework for Medical Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41047) **Meta-CDMTransNet: Cross-Domain Multi-Scale Transformer Meta-Learning Framework for Few-Shot Breast Histopathological Image Classification**
  - Session: Findings Poster Session 2
  - Tags: `Mammography / Breast`, `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40244) **MicroFM: Physics-guided Flow Matching for Isotropic Microscopy Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhan_MicroFM_Physics-guided_Flow_Matching_for_Isotropic_Microscopy_Reconstruction_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/-e9MDaVTHUw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40244.png" alt="MicroFM: Physics-guided Flow Matching for Isotropic Microscopy Reconstruction poster" width="420">
  - Authors: Xingzu Zhan, Runmin Jiang, Vatsal Gupta, Tanush Swaminathan, Yanwen Wang, Genpei Zhang, Haili Wang, Min Xu
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41015) **Mitigating Batch Effects in Histopathology via Language-Mediated Robust Embedding Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36253) **MLLM-HWSI: A Multimodal Large Language Model for Hierarchical Whole Slide Image Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Alawode_MLLM-HWSI_A_Multimodal_Large_Language_Model_for_Hierarchical_Whole_Slide_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/7N0TG8naav0) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36253.png" alt="MLLM-HWSI: A Multimodal Large Language Model for Hierarchical Whole Slide Image Understanding poster" width="420">
  - Authors: Basit Alawode, Arif Mahmood, Muaz Radi, Shahad Albastaki, Asim Khan, Muhammad Bilal, Moshira Ali Abdalla, Mohammed Bennamoun, Sajid Javed
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38040) **Momentum Memory for Knowledge Distillation in Computational Pathology**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_Momentum_Memory_for_Knowledge_Distillation_in_Computational_Pathology_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/hO7-hZYK6rY) [arXiv](https://arxiv.org/abs/2602.21395) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38040.png" alt="Momentum Memory for Knowledge Distillation in Computational Pathology poster" width="420">
  - Authors: yongxin guo, Hao Lu, Onur C., Zhengjie Zhu, Muhammet F., Metin N.
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41038) **Multimodal Decoupled Dynamic Graph Learning for Brain Disease Diagnosis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39054) **MUSE: Harnessing Precise and Diverse Semantics for Few-Shot Whole Slide Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_MUSE_Harnessing_Precise_and_Diverse_Semantics_for_Few-Shot_Whole_Slide_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/3-OpdgsF0lM) [arXiv](https://arxiv.org/abs/2602.20873) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39054.png" alt="MUSE: Harnessing Precise and Diverse Semantics for Few-Shot Whole Slide Image Classification poster" width="420">
  - Authors: Jiahao Xu, Sheng Huang, Xin Zhang, Zhixiong Nan, Jiajun Dong, Nankun Mu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40051) **MUST: Modality-Specific Representation-Aware Transformer for Diffusion-Enhanced Survival Prediction with Missing Modality**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_MUST_Modality-Specific_Representation-Aware_Transformer_for_Diffusion-Enhanced_Survival_Prediction_with_Missing_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/GGQ1YFcJdzE) [arXiv](https://arxiv.org/abs/2603.26071) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Kyungwon Kim, Dosik Hwang
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37432) **MuViT: Multi-Resolution Vision Transformers for Learning Across Scales in Microscopy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mantes_MuViT_Multi-Resolution_Vision_Transformers_for_Learning_Across_Scales_in_Microscopy_CVPR_2026_paper.html) [GitHub](https://github.com/weigertlab/muvit) [Video](https://www.youtube-nocookie.com/embed/apFzMgmUUnM) [arXiv](https://arxiv.org/abs/2602.24222) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37432.png" alt="MuViT: Multi-Resolution Vision Transformers for Learning Across Scales in Microscopy poster" width="420">
  - Authors: Albert Dominguez Mantes, Gioele La Manno, Martin Weigert
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Organs / Anatomy`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41035) **NAKUL-Med: Spectral-Graph State Space Models with Dynamics Kernels for Medical Signals**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36381) **Neural Field-Based 3D Surface Reconstruction of Microstructures from Multi-Detector Signals in Scanning Electron Microscopy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Neural_Field-Based_3D_Surface_Reconstruction_of_Microstructures_from_Multi-Detector_Signals_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/ionPVaKpMvU) [arXiv](https://arxiv.org/abs/2508.04728) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36381.png" alt="Neural Field-Based 3D Surface Reconstruction of Microstructures from Multi-Detector Signals in Scanning Electron Microscopy poster" width="420">
  - Authors: Shuo Chen, Yijin Li, Xi Zheng, Guofeng Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break | Oral Session 2B: Materials & Lighting
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41044) **Open-Set Spatial Gene Expression Prediction from Histological Images via Retrieval-Augmented Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41025) **PaM-MIL: Proliferation and Metastasis Enhanced Localization for Multiple Instance Learning on Pathology Images**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41051) **PBSBench: A Multi-Level Vision-Language Framework and Benchmark for Hematopathology Whole Slide Image Interpretation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41045) **Personalized Functional Brain Network Modeling with Adaptive Auto-Weighted Learning for Automatic Brain Disorder Diagnosis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41054) **PGDM: Physics-Guided Noise-Free Diffusion Model Based on Point Spread Function for Light-Scattering Removal in Unpaired Biomedical Images**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41029) **PhySe-RPO: Physics and Semantics Guided Relative Policy Optimization for Diffusion-Based Surgical Smoke Removal**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Surgery / Medical Video`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38249) **Plant Taxonomy Meets Plant Counting: A Fine-Grained, Taxonomic Dataset for Counting Hundreds of Plant Species**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_Plant_Taxonomy_Meets_Plant_Counting_A_Fine-Grained_Taxonomic_Dataset_for_CVPR_2026_paper.html) [Project](https://tiny-smart.github.io/tpc268-project-page/) [Video](https://www.youtube-nocookie.com/embed/TYSOtMlA9yE) [arXiv](https://arxiv.org/abs/2603.21229) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38249.png" alt="Plant Taxonomy Meets Plant Counting: A Fine-Grained, Taxonomic Dataset for Counting Hundreds of Plant Species poster" width="420">
  - Authors: Jinyu Xu, Tianqi Hu, Xiaonan Hu, Letian Zhou, Songliang Cao, Meng Zhang, Hao Lu
  - Session: Poster Session 1 & Exhibit Hall | Oral Session 1C: Efficient Reasoning
  - Tags: `Pathology / Microscopy / Cells`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41048) **PLCReg: Correlation-Aware Polar-Linear Attention for Guiding Medical Image Registration**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Registration`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41016) **PTF-CT: Polar-Aware Temporal-Frequential Iterative Reconstruction for Sparse-View CT**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41022) **ReCliFF: Adaptive Orthogonal Decoupling for Federated Fine-tuning of Medical MLLMs**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41062) **RelativeFlow: Taming Medical Image Denoising Learning with Noisy Reference**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41058) **Rethinking Medical High-Modality Learning Under Missingness — A Long-Tailed Distribution Perspective**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41013) **Rethinking Whole-Body CT Image Interpretation: An Abnormality-Centric Approach**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41222) **SAGE: Shape-Adapting Gated Experts for Adaptive Histopathology Image Segmentation**
  - Session: Findings Poster Session 3
  - Tags: `Pathology / Microscopy / Cells`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37223) **SAR2Net: Learning Spatially Anchored Representations for Retrieval-Guided Cross-Stain Alignment**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_SAR2Net_Learning_Spatially_Anchored_Representations_for_Retrieval-Guided_Cross-Stain_Alignment_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/gIJKJp8QBg8) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37223.png" alt="SAR2Net: Learning Spatially Anchored Representations for Retrieval-Guided Cross-Stain Alignment poster" width="420">
  - Authors: Tianle Shen, Fang Yan, Xiaofan Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Registration`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37545) **SOTA: Self-adaptive Optimal Transport for Zero-Shot Classification with Multiple Foundation Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_SOTA_Self-adaptive_Optimal_Transport_for_Zero-Shot_Classification_with_Multiple_Foundation_CVPR_2026_paper.html) [GitHub](https://github.com/Afleve/self-adaptive-Optimal-Transport) [arXiv](https://arxiv.org/abs/2506.13723) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37545.png" alt="SOTA: Self-adaptive Optimal Transport for Zero-Shot Classification with Multiple Foundation Models poster" width="420">
  - Authors: Zhanxuan Hu, Qiyu Xu, Yu Duan, Yonghang Tai, Huafeng Li
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36727) **Sparse Task Vector Mixup with Hypernetworks for Efficient Knowledge Transfer in Whole-Slide Image Prognosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Sparse_Task_Vector_Mixup_with_Hypernetworks_for_Efficient_Knowledge_Transfer_CVPR_2026_paper.html) [GitHub](https://github.com/liupei101/STEPH) [arXiv](https://arxiv.org/abs/2603.10526) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/36727.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36727.png" alt="Sparse Task Vector Mixup with Hypernetworks for Efficient Knowledge Transfer in Whole-Slide Image Prognosis poster" width="420">
  - Authors: Pei Liu, xiangxiang Zeng, Tengfei Ma, Yucheng Xing, Xuanbai Ren, Yiping Liu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39564) **Spatial-SAM: Spatially Consistent 3D Electron Microscopy Segmentation with SDF Memory and Semi-Supervised Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Spatial-SAM_Spatially_Consistent_3D_Electron_Microscopy_Segmentation_with_SDF_Memory_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/nzZlJfRjT-w) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39564.png" alt="Spatial-SAM: Spatially Consistent 3D Electron Microscopy Segmentation with SDF Memory and Semi-Supervised Learning poster" width="420">
  - Authors: Yikai Huang, Renmin Han, Yuxuan Wang, Youcheng Cai, Ligang Liu
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36955) **Statistical Characteristic-Guided Denoising for Rapid High-Resolution Transmission Electron Microscopy Imaging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Statistical_Characteristic-Guided_Denoising_for_Rapid_High-Resolution_Transmission_Electron_Microscopy_Imaging_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.18834) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36955.png" alt="Statistical Characteristic-Guided Denoising for Rapid High-Resolution Transmission Electron Microscopy Imaging poster" width="420">
  - Authors: Hesong Li, Ziqi Wu, Ruiwen Shao, Ying Fu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41026) **Surgical Procedural Planning as 3D World Modelling: Towards Automated Pulmonary Resection**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Surgery / Medical Video`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40561) **Three-Step Conditional Diffusion 3D Reconstruction for Light-Field Microscopy**
  - Session: Findings Poster Session 1
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41039) **TICON: A Slide-Level Tile Contextualizer for Histopathology Representation Learning**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38759) **TIM: Temporal Decoupling with Iterative Mutual-Refinement Model for Longitudinal Radiology Report Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_TIM_Temporal_Decoupling_with_Iterative_Mutual-Refinement_Model_for_Longitudinal_Radiology_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38759.png" alt="TIM: Temporal Decoupling with Iterative Mutual-Refinement Model for Longitudinal Radiology Report Generation poster" width="420">
  - Authors: Yiheng Dong, Yi Lin, Shilong Huang, Xiyan Yang, Xin Yang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37998) **TopoSlide: Topologically-Informed Histopathology Whole Slide Image Representation Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Abousamra_TopoSlide_Topologically-Informed_Histopathology_Whole_Slide_Image_Representation_Learning_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/mHcOtbHK-Xc) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37998.png" alt="TopoSlide: Topologically-Informed Histopathology Whole Slide Image Representation Learning poster" width="420">
  - Authors: Shahira Abousamra, Asmita Sood, Sylvia Plevritis
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39944) **Toward Generalizable Whole Brain Representations with High-Resolution Light-Sheet Data**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Toward_Generalizable_Whole_Brain_Representations_with_High-Resolution_Light-Sheet_Data_CVPR_2026_paper.html) [Project](https://canvas.lightsheetdata.com/) [arXiv](https://arxiv.org/abs/2603.29842) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39944.png" alt="Toward Generalizable Whole Brain Representations with High-Resolution Light-Sheet Data poster" width="420">
  - Authors: Minyoung E. Kim, Dae Hee Yun, Aditi V. Patel, Madeline Hon, Webster Guan, Taegeon Lee, Brian Nguyen
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Organs / Anatomy`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41018) **Towards Noise-Robust Medical Segmentation via Chebyshev-Attention-Based Asymmetric UNet**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41040) **TP-Seg: Task-Prototype Framework for Unified Medical Lesion Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37583) **Turning Pre-Trained Vision Transformers into End-to-End Histopathology Whole Slide Image Models for Survival Prediction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Turning_Pre-Trained_Vision_Transformers_into_End-to-End_Histopathology_Whole_Slide_Image_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37583.png" alt="Turning Pre-Trained Vision Transformers into End-to-End Histopathology Whole Slide Image Models for Survival Prediction poster" width="420">
  - Authors: Jiawen Li, Jiali Hu, Xitong Ling, Renao Yan, Yuxuan Chen, Tian Guan, Yonghong He
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41019) **Two-Stage 3D Pulmonary Vessel Reconstruction via Trunk--Expansion Coupled Point Cloud Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38198) **Uni-Hema: Unified Model for Digital Hematopathology**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rehman_Uni-Hema_Unified_Model_for_Digital_Hematopathology_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/wbcD6R5AwwM) [arXiv](https://arxiv.org/abs/2511.13889) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38198.png" alt="Uni-Hema: Unified Model for Digital Hematopathology poster" width="420">
  - Authors: Abdul Rehman, Iqra Rasool, Ayisha Imran, Mohsen Ali, Waqas Sultani
  - Session: Poster Session 6
  - Tags: `Pathology / Microscopy / Cells`, `Cancer / Tumor / Lesion`, `Segmentation`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38290) **Universal-to-Specific: Dynamic Knowledge-Guided Multiple Instance Learning for Few-Shot Whole Slide Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Universal-to-Specific_Dynamic_Knowledge-Guided_Multiple_Instance_Learning_for_Few-Shot_Whole_Slide_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38290.png" alt="Universal-to-Specific: Dynamic Knowledge-Guided Multiple Instance Learning for Few-Shot Whole Slide Image Classification poster" width="420">
  - Authors: Junjian Li, Hulin Kuang, Jin Liu, Hailin Yue, Mengshen He, Jianxin Wang
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38244) **URICA: A Uniformity Region Affine Identifier Capture Algorithm for Arbitrary Region Retrieval in Pathology Images**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Su_URICA_A_Uniformity_Region_Affine_Identifier_Capture_Algorithm_for_Arbitrary_CVPR_2026_paper.html) [Project](https://mcaloma.github.io/URICA_page/) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38244.png" alt="URICA: A Uniformity Region Affine Identifier Capture Algorithm for Arbitrary Region Retrieval in Pathology Images poster" width="420">
  - Authors: Ri Su, Zhao CHEN, Caleb Chen Cao, Lei Chen
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38727) **VEMamba: Efficient Isotropic Reconstruction of Volume Electron Microscopy with Axial-Lateral Consistent Mamba**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_VEMamba_Efficient_Isotropic_Reconstruction_of_Volume_Electron_Microscopy_with_Axial-Lateral_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/0-TXFO1x46w) [arXiv](https://arxiv.org/abs/2603.00887) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38727.png" alt="VEMamba: Efficient Isotropic Reconstruction of Volume Electron Microscopy with Axial-Lateral Consistent Mamba poster" width="420">
  - Authors: Longmi Gao, Pan Gao
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41053) **Vision-Language Models Encode Clinical Guidelines for Concept-Based Medical Reasoning**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41024) **Vision-Language Models for Automated 3D PET/CT Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `PET / Nuclear Medicine`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41023) **Volumetrically Consistent Implicit Atlas Learning via Neural Diffeomorphic Flow for Placenta MRI**
  - Session: Findings Poster Session 2
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41050) **When Models Learn to Ask Why: Adaptive Causal Reasoning for Trustworthy Medical Vision–Language Models**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39039) **WonderZoom: Multi-Scale 3D World Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Cao_WonderZoom_Multi-Scale_3D_World_Generation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.09164) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Jin Cao, Hong-Xing Yu, Jiajun Wu
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Generative / Diffusion`

<a id="dermatology-skin"></a>
### Dermatology / Skin

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37123) **CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sultana_CoFiDA-M_Concept-Aware_Feature_Modulation_for_Cross-Domain_Adaptation_with_Image-Only_Inference_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/fD9SiGbGIxc) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37123.png" alt="CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference poster" width="420">
  - Authors: Nurjahan Sultana, Moi Hoon Yap, Xinqi Fan, Wenqi Lu
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Dermatology / Skin`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36828) **MambaLiteUNet: Cross-Gated Adaptive Feature Fusion for Robust Skin Lesion Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rahman_MambaLiteUNet_Cross-Gated_Adaptive_Feature_Fusion_for_Robust_Skin_Lesion_Segmentation_CVPR_2026_paper.html) [GitHub](https://github.com/maklachur/MambaLiteUNet) [Video](https://www.youtube-nocookie.com/embed/5n1VdmIjThQ) [arXiv](https://arxiv.org/abs/2604.20286) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/36828_2CEf7jM.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36828.png" alt="MambaLiteUNet: Cross-Gated Adaptive Feature Fusion for Robust Skin Lesion Segmentation poster" width="420">
  - Authors: Md Maklachur Rahman, Soon Ki Jung, Tracy Hammond
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Dermatology / Skin`, `Cancer / Tumor / Lesion`, `Segmentation`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36879) **The Invisible Gorilla Effect in Out-of-distribution Detection**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Anthony_The_Invisible_Gorilla_Effect_in_Out-of-distribution_Detection_CVPR_2026_paper.html) [GitHub](https://github.com/HarryAnthony/Invisible_Gorilla_Effect) [Video](https://www.youtube-nocookie.com/embed/_1yfErMh108) [arXiv](https://arxiv.org/abs/2602.20068) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/36879.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36879.png" alt="The Invisible Gorilla Effect in Out-of-distribution Detection poster" width="420">
  - Authors: Harry Anthony, Ziyun Liang, Hermione Warr, Konstantinos Kamnitsas
  - Session: Poster Session 6
  - Tags: `Dermatology / Skin`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Federated / Continual / Generalization`

<a id="endoscopy-colonoscopy-polyp"></a>
### Endoscopy / Colonoscopy / Polyp

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41049) **A Denoising-Enhanced Multimodal Learning Framework for Robust Nasal Endoscopy Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38518) **Benchmarking Endoscopic Surgical Image Restoration and Beyond**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pei_Benchmarking_Endoscopic_Surgical_Image_Restoration_and_Beyond_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/r8YhHYk-4Ng) [arXiv](https://arxiv.org/abs/2505.19161) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38518.png" alt="Benchmarking Endoscopic Surgical Image Restoration and Beyond poster" width="420">
  - Authors: Jialun Pei, Diandian Guo, Donghui Yang, Zhixi Li, Yuxin Feng, Long Ma, Bo Du, Pheng-Ann Heng
  - Session: Poster Session 6
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39693) **Clinically-Grounded Counterfactual Reasoning for Medical Video Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Clinically-Grounded_Counterfactual_Reasoning_for_Medical_Video_Diagnosis_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39693.png" alt="Clinically-Grounded Counterfactual Reasoning for Medical Video Diagnosis poster" width="420">
  - Authors: Jianzhe Gao, Churan Wang, Weiyi Zhang, Jianghua Li, Lian Li, Wenguan Wang, Yixin Zhu, Yizhou Wang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39733) **Depth Any Endoscopy: Towards Self-Supervised Generalizable Depth Estimation in Monocular Endoscopy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shao_Depth_Any_Endoscopy_Towards_Self-Supervised_Generalizable_Depth_Estimation_in_Monocular_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/S0FxVHv7ddg) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39733.png" alt="Depth Any Endoscopy: Towards Self-Supervised Generalizable Depth Estimation in Monocular Endoscopy poster" width="420">
  - Authors: Shuwei Shao, Kejin Zhu, Shixing Ma, Xinzhe Du, Baochang Zhang, Zhe Min
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41021) **DepthScopy: Decoupling Frequency for Endoscopic Depth Estimation in Sparsely-Textured Regions**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38989) **Focus-to-Perceive Representation Learning: A Cognition-Inspired Hierarchical Framework for Endoscopic Video Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Focus-to-Perceive_Representation_Learning_A_Cognition-Inspired_Hierarchical_Framework_for_Endoscopic_Video_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/Dbzi1GLUM5M) [arXiv](https://arxiv.org/abs/2603.25778) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38989.png" alt="Focus-to-Perceive Representation Learning: A Cognition-Inspired Hierarchical Framework for Endoscopic Video Analysis poster" width="420">
  - Authors: Yuan Zhang, Sihao Dou, Kai Hu, Shuhua Deng, Chunhong Cao, Fen Xiao, Xieping Gao
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36239) **From Infusion to Assimilation Distillation for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hong_From_Infusion_to_Assimilation_Distillation_for_Medical_Image_Segmentation_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36239.png" alt="From Infusion to Assimilation Distillation for Medical Image Segmentation poster" width="420">
  - Authors: Jiankang Hong, Ye Luo, Yinan Liu, Junsong Yuan
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Segmentation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37076) **Learning Surgical Robotic Manipulation with 3D Spatial Priors**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sheng_Learning_Surgical_Robotic_Manipulation_with_3D_Spatial_Priors_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.03798) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Yu Sheng, Lidian Wang, Xiaomeng Chu, Jiajun Deng, Min Cheng, Yanyong Zhang, Bei Hua, Houqiang Li, Jianmin Ji
  - Session: Poster Session 6
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39091) **LEMON: A Large Endoscopic MONocular Dataset and Foundation Model for Perception in Surgical Settings**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Che_LEMON_A_Large_Endoscopic_MONocular_Dataset_and_Foundation_Model_for_CVPR_2026_paper.html) [GitHub](https://github.com/visurg-ai/LEMON) [Video](https://www.youtube-nocookie.com/embed/6MZ0E9e17Qo) [arXiv](https://arxiv.org/abs/2503.19740) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39091.png" alt="LEMON: A Large Endoscopic MONocular Dataset and Foundation Model for Perception in Surgical Settings poster" width="420">
  - Authors: chengan che, Chao Wang, Tom Vercauteren, Sophia Tsoka, Luis Carlos Garcia Peraza Herrera
  - Session: Poster Session 6
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Segmentation`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36263) **SAMIX: Reinforcing SAM2 with Semantic Adapter and Reference Selecting Policy for Mix-Supervised Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_SAMIX_Reinforcing_SAM2_with_Semantic_Adapter_and_Reference_Selecting_Policy_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36263.png" alt="SAMIX: Reinforcing SAM2 with Semantic Adapter and Reference Selecting Policy for Mix-Supervised Segmentation poster" width="420">
  - Authors: Qiang Hu, Jiajie Wei, Zhenyu Yi, Zhifen Yan, Yingjie Guo, Hongkuan Shi, Ge-Peng Ji, Qiang Li, Zhiwei Wang
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36865) **Tell2Adapt: A Unified Framework for Source Free Unsupervised Domain Adaptation via Vision Foundation Model**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Tell2Adapt_A_Unified_Framework_for_Source_Free_Unsupervised_Domain_Adaptation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.05012) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36865.png" alt="Tell2Adapt: A Unified Framework for Source Free Unsupervised Domain Adaptation via Vision Foundation Model poster" width="420">
  - Authors: Yulong Shi, Shijie Li, Ziyi Li, Lin Qi
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`

<a id="surgery-medical-video"></a>
### Surgery / Medical Video

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39331) **A Stitch in Time: Learning Procedural Workflow via Self-Supervised Plackett–Luce Ranking**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Che_A_Stitch_in_Time_Learning_Procedural_Workflow_via_Self-Supervised_Plackett-Luce_CVPR_2026_paper.html) [GitHub](https://github.com/visurg-ai/PL-Stitch) [Video](https://www.youtube-nocookie.com/embed/4OBKnzvfNlg) [arXiv](https://arxiv.org/abs/2511.17805) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39331.png" alt="A Stitch in Time: Learning Procedural Workflow via Self-Supervised Plackett–Luce Ranking poster" width="420">
  - Authors: chengan che, Chao Wang, Xinyue Chen, Sophia Tsoka, Luis Carlos Garcia Peraza Herrera
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Surgery / Medical Video`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38518) **Benchmarking Endoscopic Surgical Image Restoration and Beyond**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pei_Benchmarking_Endoscopic_Surgical_Image_Restoration_and_Beyond_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/r8YhHYk-4Ng) [arXiv](https://arxiv.org/abs/2505.19161) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38518.png" alt="Benchmarking Endoscopic Surgical Image Restoration and Beyond poster" width="420">
  - Authors: Jialun Pei, Diandian Guo, Donghui Yang, Zhixi Li, Yuxin Feng, Long Ma, Bo Du, Pheng-Ann Heng
  - Session: Poster Session 6
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36246) **Boundary-Responsive Differentiable Gating for Superpixel-Based Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ahmed_Boundary-Responsive_Differentiable_Gating_for_Superpixel-Based_Segmentation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/CnQG5H667N4) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36246.png" alt="Boundary-Responsive Differentiable Gating for Superpixel-Based Segmentation poster" width="420">
  - Authors: Fatmaelzahraa Ali Ahmed, Zhihe Lu, Gianni Di, Diram Tabaa, Mohamed Hamdy, Muraam Abdel-Ghani, Abdulaziz Al-Ali, Muhammad Arsalan, Shidin Balakrishnan
  - Session: Poster Session 6
  - Tags: `Surgery / Medical Video`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39693) **Clinically-Grounded Counterfactual Reasoning for Medical Video Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Clinically-Grounded_Counterfactual_Reasoning_for_Medical_Video_Diagnosis_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39693.png" alt="Clinically-Grounded Counterfactual Reasoning for Medical Video Diagnosis poster" width="420">
  - Authors: Jianzhe Gao, Churan Wang, Weiyi Zhang, Jianghua Li, Lian Li, Wenguan Wang, Yixin Zhu, Yizhou Wang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39733) **Depth Any Endoscopy: Towards Self-Supervised Generalizable Depth Estimation in Monocular Endoscopy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shao_Depth_Any_Endoscopy_Towards_Self-Supervised_Generalizable_Depth_Estimation_in_Monocular_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/S0FxVHv7ddg) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39733.png" alt="Depth Any Endoscopy: Towards Self-Supervised Generalizable Depth Estimation in Monocular Endoscopy poster" width="420">
  - Authors: Shuwei Shao, Kejin Zhu, Shixing Ma, Xinzhe Du, Baochang Zhang, Zhe Min
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38089) **DSCA: Dynamic Subspace Concept Alignment for Lifelong VLM Editing**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Das_DSCA_Dynamic_Subspace_Concept_Alignment_for_Lifelong_VLM_Editing_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/RCpaQaN0yFk) [arXiv](https://arxiv.org/abs/2604.07965) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38089.png" alt="DSCA: Dynamic Subspace Concept Alignment for Lifelong VLM Editing poster" width="420">
  - Authors: Gyanendra Das, Sai Jena
  - Session: Poster Session 6
  - Tags: `Surgery / Medical Video`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37076) **Learning Surgical Robotic Manipulation with 3D Spatial Priors**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sheng_Learning_Surgical_Robotic_Manipulation_with_3D_Spatial_Priors_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.03798) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Yu Sheng, Lidian Wang, Xiaomeng Chu, Jiajun Deng, Min Cheng, Yanyong Zhang, Bei Hua, Houqiang Li, Jianmin Ji
  - Session: Poster Session 6
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39091) **LEMON: A Large Endoscopic MONocular Dataset and Foundation Model for Perception in Surgical Settings**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Che_LEMON_A_Large_Endoscopic_MONocular_Dataset_and_Foundation_Model_for_CVPR_2026_paper.html) [GitHub](https://github.com/visurg-ai/LEMON) [Video](https://www.youtube-nocookie.com/embed/6MZ0E9e17Qo) [arXiv](https://arxiv.org/abs/2503.19740) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39091.png" alt="LEMON: A Large Endoscopic MONocular Dataset and Foundation Model for Perception in Surgical Settings poster" width="420">
  - Authors: chengan che, Chao Wang, Tom Vercauteren, Sophia Tsoka, Luis Carlos Garcia Peraza Herrera
  - Session: Poster Session 6
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Segmentation`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40035) **MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Su_MedGRPO_Multi-Task_Reinforcement_Learning_for_Heterogeneous_Medical_Video_Understanding_CVPR_2026_paper.html) [Project](https://uii-america.github.io/MedGRPO/) [Video](https://www.youtube-nocookie.com/embed/RRS5O0BziDA) [arXiv](https://arxiv.org/abs/2512.06581) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40035.png" alt="MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding poster" width="420">
  - Authors: Yuhao Su, Anwesa Choudhuri, Zhongpai Gao, Benjamin Planche, Van Nguyen Nguyen, Meng Zheng, Yuhan Shen, Arun Innanje, Terrence Chen, Ehsan Elhamifar, ... (+1 more)
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Surgery / Medical Video`, `Medical AI / General`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41029) **PhySe-RPO: Physics and Semantics Guided Relative Policy Optimization for Diffusion-Based Surgical Smoke Removal**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Surgery / Medical Video`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36379) **Real2Sim2Real: RetinalDepth-64K for Depth Estimation in Posterior Segment Ophthalmic Surgery**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_Real2Sim2Real_RetinalDepth-64K_for_Depth_Estimation_in_Posterior_Segment_Ophthalmic_Surgery_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Bingwen Dong, Gan Liu, Xiaoxi Lu, Guangcheng Chen, Jialu ZHANG, Yan Hu, Xiaoqing Zhang, Jiang Liu
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `OCT / Ophthalmology / Retina`, `Surgery / Medical Video`, `Segmentation`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39890) **SHands: A Multi-View Dataset and Benchmark for Surgical Hand-Gesture and Error Recognition Toward Medical Training**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_SHands_A_Multi-View_Dataset_and_Benchmark_for_Surgical_Hand-Gesture_and_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/AS6p-tpArRw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39890.png" alt="SHands: A Multi-View Dataset and Benchmark for Surgical Hand-Gesture and Error Recognition Toward Medical Training poster" width="420">
  - Authors: Le Ma, Thiago Freitas dos Santos, Nadia Magnenat-Thalmann, Katarzyna Wac
  - Session: Poster Session 6
  - Tags: `Surgery / Medical Video`, `Medical AI / General`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36343) **SurgCoT: Advancing Spatiotemporal Reasoning in Surgical Videos through a Chain-of-Thought Benchmark**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_SurgCoT_Advancing_Spatiotemporal_Reasoning_in_Surgical_Videos_through_a_Chain-of-Thought_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/4KwhSQ2W0JI) [arXiv](https://arxiv.org/abs/2604.20319) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36343.png" alt="SurgCoT: Advancing Spatiotemporal Reasoning in Surgical Videos through a Chain-of-Thought Benchmark poster" width="420">
  - Authors: Gui Wang, YongSong Zhou, Kaijun Deng, Wooi Ping Cheah, Rong Qu, Jianfeng Ren, Linlin Shen
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Surgery / Medical Video`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41026) **Surgical Procedural Planning as 3D World Modelling: Towards Automated Pulmonary Resection**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Surgery / Medical Video`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37108) **Synergistic Bleeding Region and Point Detection in Laparoscopic Surgical Videos**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pei_Synergistic_Bleeding_Region_and_Point_Detection_in_Laparoscopic_Surgical_Videos_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/e6iM-7BHr14) [arXiv](https://arxiv.org/abs/2503.22174) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37108.png" alt="Synergistic Bleeding Region and Point Detection in Laparoscopic Surgical Videos poster" width="420">
  - Authors: Jialun Pei, Zhangjun Zhou, Diandian Guo, Zhixi Li, Jing Qin, Bo Du, Pheng-Ann Heng
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Surgery / Medical Video`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36677) **Unlocking Positive Transfer in Incrementally Learning Surgical Instruments: A Self-reflection Hierarchical Prompt Framework**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Unlocking_Positive_Transfer_in_Incrementally_Learning_Surgical_Instruments_A_Self-reflection_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/jkFq13ptUaQ) [arXiv](https://arxiv.org/abs/2604.02877) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36677.png" alt="Unlocking Positive Transfer in Incrementally Learning Surgical Instruments: A Self-reflection Hierarchical Prompt Framework poster" width="420">
  - Authors: Yu ZHU, Kang LI, Zheng Li, Pheng-Ann Heng
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Surgery / Medical Video`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40041) **UnReflectAnything: RGB-Only Highlight Removal by Rendering Synthetic Specular Supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rota_UnReflectAnything_RGB-Only_Highlight_Removal_by_Rendering_Synthetic_Specular_Supervision_CVPR_2026_paper.html) [Project](https://alberto-rota.github.io/UnReflectAnything/) [Video](https://www.youtube-nocookie.com/embed/vfBbGixu_4s) [arXiv](https://arxiv.org/abs/2512.09583) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/40041.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40041.png" alt="UnReflectAnything: RGB-Only Highlight Removal by Rendering Synthetic Specular Supervision poster" width="420">
  - Authors: Alberto Rota, Mert Kiray, Mert Asim Karaoglu, Patrick Ruhkamp, Elena De Momi, Nassir Navab, Benjamin Busam
  - Session: Poster Session 1 & Exhibit Hall | Oral Session 1D: Computational Imaging
  - Tags: `Surgery / Medical Video`, `Restoration / Reconstruction`, `Generative / Diffusion`

<a id="3d-volumetric-medical-imaging"></a>
### 3D / Volumetric Medical Imaging

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38658) **CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_CROWn_A_Unified_Framework_for_Anti-Aliased_Downsampling_and_Phase-Calibrated_Fusion_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38658.png" alt="CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation poster" width="420">
  - Authors: Xingru Huang, Shuanghua Ye, Zhao Huang, Wenwen Tang, Huiyu Zhou, Zhiwen Zheng, Jin Liu, Xiaoshuai Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `OCT / Ophthalmology / Retina`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37051) **Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Delving_Aleatoric_Uncertainty_in_Medical_Image_Segmentation_via_Vision_Foundation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.10963) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37051.png" alt="Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models poster" width="420">
  - Authors: Ruiyang Li, Fang Liu, Licheng Jiao, Xinglin Xie, Jiayao Hao, Shuo Li, Xu Liu, Jingyi yang, Lingling Li, Puhua Chen, ... (+1 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38134) **Divide, Conquer, and Aggregate: Asymmetric Experts for Class-Imbalanced Semi-Supervised Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Divide_Conquer_and_Aggregate_Asymmetric_Experts_for_Class-Imbalanced_Semi-Supervised_Medical_CVPR_2026_paper.html) [GitHub](https://github.com/PHPJava666/DCA) [Video](https://www.youtube-nocookie.com/embed/rUjLlvNsrDs) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38134.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38134.png" alt="Divide, Conquer, and Aggregate: Asymmetric Experts for Class-Imbalanced Semi-Supervised Medical Image Segmentation poster" width="420">
  - Authors: Yajun Liu
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37060) **DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_DK-DDIL_Adaptive_Knowledge_Retention_for_Dynamic_Domain-Incremental_Learning_in_Medical_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37060.png" alt="DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging poster" width="420">
  - Authors: Yuxi Ma, Sujie Liu, Jing Yang, Jiacheng Wang, Yiping Chen, Baptiste Magnier, Liansheng Wang
  - Session: Poster Session 6 | Oral Session 6C: Medical Vision
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36172) **F^2-Assist: Multi-Phase Fetal Growth Forecast and Report Generation from Ultrasound Examination**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pu_F2-Assist_Multi-Phase_Fetal_Growth_Forecast_and_Report_Generation_from_Ultrasound_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36172.png" alt="F^2-Assist: Multi-Phase Fetal Growth Forecast and Report Generation from Ultrasound Examination poster" width="420">
  - Authors: Bin Pu, XUSHENG LIANG, Xinpeng Ding, Jinlin Wu, Zhen Lei, Shengli Li, Kenli Li, Jiawei Ma
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36666) **Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Learning_Generalizable_3D_Medical_Image_Representations_from_Mask-Guided_Self-Supervision_CVPR_2026_paper.html) [GitHub](https://github.com/Stanford-AIMI/MASS?tab=readme-ov-file) [arXiv](https://arxiv.org/abs/2603.13660) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36666.png" alt="Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision poster" width="420">
  - Authors: Yunhe Gao, Yabin Zhang, Chong Wang, Jiaming Liu, Maya Varma, Jean-Benoit Delbrouck, Akshay Chaudhari, Curtis Langlotz
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39592) **Masked-Diffusion Autoencoders for 3D Medical Vision Representation Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Tu_Masked-Diffusion_Autoencoders_for_3D_Medical_Vision_Representation_Learning_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Jiachen Tu, Guanghui Qin, Theodore Zhengde Zhao, Jeya Maria Jose Valanarasu, Sheng Zhang, Tristan Naumann, Fan Lam, Sheng Wang, Hoifung Poon
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39104) **PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Maqbool_PETAR_Localized_Findings_Generation_with_Mask-Aware_Vision-Language_Modeling_for_PET_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/vlHR_NcGlDs) [arXiv](https://arxiv.org/abs/2510.27680) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39104.png" alt="PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting poster" width="420">
  - Authors: Danyal Maqbool, Changhee Lee, Zachary Huemann, Samuel D. Church, Matthew E. Larson, Scott B. Perlman, Tomas A. Romero, Joshua D. Warner, Meghan Lubner, Xin Tie, ... (+4 more)
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36808) **Revisiting 2D Foundation Models for Scalable 3D Medical Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Revisiting_2D_Foundation_Models_for_Scalable_3D_Medical_Image_Classification_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.12887) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36808.png" alt="Revisiting 2D Foundation Models for Scalable 3D Medical Image Classification poster" width="420">
  - Authors: Han Liu, Bogdan Georgescu, Yanbo Zhang, Youngjin Yoo, Michael Baumgartner, Riqiang Gao, Jianing Wang, Gengyan Zhao, Eli Gibson, Dorin Comaniciu, ... (+1 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36984) **Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Claessens_Scaling_Self-Supervised_and_Cross-Modal_Pretraining_for_Volumetric_CT_Transformers_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/tFdLkc0v998) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36984.png" alt="Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers poster" width="420">
  - Authors: Cris Claessens, Christiaan Viviers, Giacomo D&amp;#x27;Amicantonio, Egor Bondarev, Fons van der Sommen
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36477) **Sketch2CT: Multimodal Diffusion for Structure-Aware 3D Medical Volume Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/An_Sketch2CT_Multimodal_Diffusion_for_Structure-Aware_3D_Medical_Volume_Generation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/RiNNzMcykok) [arXiv](https://arxiv.org/abs/2603.22509) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36477.png" alt="Sketch2CT: Multimodal Diffusion for Structure-Aware 3D Medical Volume Generation poster" width="420">
  - Authors: Delin An, Chaoli Wang
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Segmentation`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37454) **VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rokuss_VoxTell_Free-Text_Promptable_Universal_3D_Medical_Image_Segmentation_CVPR_2026_paper.html) [GitHub](https://github.com/MIC-DKFZ/VoxTell) [Video](https://www.youtube-nocookie.com/embed/enF-YrdY-mI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37454.png" alt="VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation poster" width="420">
  - Authors: Maximilian Rokuss, Moritz Langenberg, Yannick Kirchhoff, Fabian Isensee, Benjamin Hamm, Constantin Ulrich, Sebastian Regnery, Lukas Bauer, Efthimios Katsigiannopulos, Tobias Norajitra, ... (+1 more)
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`

<a id="medical-ai-general"></a>
### Medical AI / General

- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41049) **A Denoising-Enhanced Multimodal Learning Framework for Robust Nasal Endoscopy Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41020) **A Simple yet Effective Data Scaling Strategy for Semi-Supervised Medical Image Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41242) **A Single Pixel is All You Need: Weakly Supervised Medical Image Segmentation using Discrete Denoising Diffusion Models**
  - Session: Findings Poster Session 3
  - Tags: `Medical AI / General`, `Segmentation`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41028) **AceMIL: Ordinal-Aware Multiple Instance Learning for Pathological Progression Analysis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36280) **Act Like a Pathologist: Tissue-Aware Whole Slide Image Reasoning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Act_Like_a_Pathologist_Tissue-Aware_Whole_Slide_Image_Reasoning_CVPR_2026_paper.html) [GitHub](https://github.com/winston52/HistoSelect) [Video](https://www.youtube-nocookie.com/embed/kr1NcK5NBxg) [arXiv](https://arxiv.org/abs/2603.00667) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/36280.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36280.png" alt="Act Like a Pathologist: Tissue-Aware Whole Slide Image Reasoning poster" width="420">
  - Authors: Wentao Huang, Weimin Lyu, Peiliang Lou, Qingqiao Hu, Xiaoling Hu, Shahira Abousamra, Wenchao Han, Ruifeng Guo, Jiawei Zhou, Chao Chen, ... (+1 more)
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39101) **AD-GBC: Anisotropic Granular-Ball Skip-Connection Refiner for UNet-Based Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_AD-GBC_Anisotropic_Granular-Ball_Skip-Connection_Refiner_for_UNet-Based_Medical_Image_Segmentation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/CJhTDcusilI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39101.png" alt="AD-GBC: Anisotropic Granular-Ball Skip-Connection Refiner for UNet-Based Medical Image Segmentation poster" width="420">
  - Authors: Xiya Shen, Qinglin Zhao, Li Feng
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41354) **Adaptive Reinforcement for Open-ended Medical Reasoning via Semantic-Guided Reward Collapse Mitigation**
  - Session: Findings Poster Session 3
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39832) **Advancing Cancer Prognosis with Hierarchical Fusion of Genomic, Proteomic and Pathology Imaging Data from a Systems Biology Perspective**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Advancing_Cancer_Prognosis_with_Hierarchical_Fusion_of_Genomic_Proteomic_and_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.13787) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39832.png" alt="Advancing Cancer Prognosis with Hierarchical Fusion of Genomic, Proteomic and Pathology Imaging Data from a Systems Biology Perspective poster" width="420">
  - Authors: Junjie Zhou, Bao Xue, Meiling Wang, WEI SHAO, Daoqiang Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41420) **Analyzing and Enhancing Visual Learning in LLM-based Radiology Report Generation**
  - Session: Findings Poster Session 3
  - Tags: `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41056) **Anatomy-Aware Adaptive Feature Perturbation Framework for Semi-Supervised MRI Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41030) **Anatomy-CoT: Teaching MLLMs to Reason in Radiology**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39058) **Annotation-Efficient Coreset Selection for Context-dependent Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Annotation-Efficient_Coreset_Selection_for_Context-dependent_Segmentation_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39058.png" alt="Annotation-Efficient Coreset Selection for Context-dependent Segmentation poster" width="420">
  - Authors: jin zhang, Zhe Cao, Biwen Yang, Ruiheng Zhang
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36230) **Any2Any 3D Diffusion Models with Knowledge Transfer: A Radiotherapy Planning Study**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Any2Any_3D_Diffusion_Models_with_Knowledge_Transfer_A_Radiotherapy_Planning_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/iWkIgkP-mtU) [arXiv](https://arxiv.org/abs/2605.09622) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36230.png" alt="Any2Any 3D Diffusion Models with Knowledge Transfer: A Radiotherapy Planning Study poster" width="420">
  - Authors: Yuhan Wang, Zihan Li, Han Liu, Simon Arberet, Martin F. Kraus, Yuyin Zhou, Florin-Cristian Ghesu, Dorin Comaniciu, Ali Kamen, Riqiang Gao
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38311) **BackSplit: The Importance of Sub-dividing the Background in Biomedical Lesion Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Saluja_BackSplit_The_Importance_of_Sub-dividing_the_Background_in_Biomedical_Lesion_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2511.19394) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38311.png" alt="BackSplit: The Importance of Sub-dividing the Background in Biomedical Lesion Segmentation poster" width="420">
  - Authors: Rachit Saluja, Asli Cihangir, Ruining Deng, Johannes C. Paetzold, Fengbei Liu, Mert Sabuncu
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38518) **Benchmarking Endoscopic Surgical Image Restoration and Beyond**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pei_Benchmarking_Endoscopic_Surgical_Image_Restoration_and_Beyond_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/r8YhHYk-4Ng) [arXiv](https://arxiv.org/abs/2505.19161) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38518.png" alt="Benchmarking Endoscopic Surgical Image Restoration and Beyond poster" width="420">
  - Authors: Jialun Pei, Diandian Guo, Donghui Yang, Zhixi Li, Yuxin Feng, Long Ma, Bo Du, Pheng-Ann Heng
  - Session: Poster Session 6
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37248) **Beyond Pixel Simulation: Pathology Image Generation via Diagnostic Semantic Tokens and Prototype Control**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Beyond_Pixel_Simulation_Pathology_Image_Generation_via_Diagnostic_Semantic_Tokens_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.21058) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37248.png" alt="Beyond Pixel Simulation: Pathology Image Generation via Diagnostic Semantic Tokens and Prototype Control poster" width="420">
  - Authors: Minghao Han, Yichen Liu, Yizhou Liu, Zizhi Chen, Jingqun Tang, Xuecheng Wu, Dingkang Yang, Lihua Zhang
  - Session: Poster Session 6
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37720) **Beyond the Static-World: Lifelong Learning for All-in-One Medical Image Restoration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shan_Beyond_the_Static-World_Lifelong_Learning_for_All-in-One_Medical_Image_Restoration_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37720.png" alt="Beyond the Static-World: Lifelong Learning for All-in-One Medical Image Restoration poster" width="420">
  - Authors: Shihao Shan, Hongying Liu, Fanhua Shang, Liang Wan, Jingjing Deng
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `Medical AI / General`, `Restoration / Reconstruction`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38292) **BiomedCCPL: Causal Conditional Prompt Learning for Biomedical Vision-Language Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Cui_BiomedCCPL_Causal_Conditional_Prompt_Learning_for_Biomedical_Vision-Language_Models_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/wiNrWi1InSs) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38292.png" alt="BiomedCCPL: Causal Conditional Prompt Learning for Biomedical Vision-Language Models poster" width="420">
  - Authors: Xueliang Cui, Juncai Zhang, Jiacheng Hou, Dan Lu, Hao Zhang, Ruxin Wang
  - Session: Poster Session 6
  - Tags: `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41196) **BiomedHELIX : HiErarchical-Local Interaction eXploration for Biomedical Vision-Language Models**
  - Session: Findings Poster Session 3
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38806) **BiOTPrompt: Bidirectional Optimal Transport Guided Prompting for Disease Evolution-aware Radiology Report Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_BiOTPrompt_Bidirectional_Optimal_Transport_Guided_Prompting_for_Disease_Evolution-aware_Radiology_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/zU8winZCkTk) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38806.png" alt="BiOTPrompt: Bidirectional Optimal Transport Guided Prompting for Disease Evolution-aware Radiology Report Generation poster" width="420">
  - Authors: Tengfei Liu, Yijian Fan, Boyue Wang, Yongli Hu, Mingjie Li, Jinghua Li, Junbin Gao, Xiaojun Chang, Zhihui Li, Baocai Yin
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41061) **BLEG: LLM Functions as Powerful fMRI Graph-Enhancer for Brain Network Analysis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36389) **Bridging RGB and Hematoxylin Components: An Interleaved Guidance and Fusion Framework for Point Supervised Nuclei Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huan_Bridging_RGB_and_Hematoxylin_Components_An_Interleaved_Guidance_and_Fusion_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/sSkEBEog0Ts) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36389.png" alt="Bridging RGB and Hematoxylin Components: An Interleaved Guidance and Fusion Framework for Point Supervised Nuclei Segmentation poster" width="420">
  - Authors: Zihan Huan, Xipeng Pan, Hualong Zhang, Siyang Feng, Rushi Lan, Huadeng Wang, Haoxiang Lu, Zhenbing Liu
  - Session: Poster Session 6
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39670) **Bulk RNA-seq Guided Multi-modal Detection of Anomalous Regions in Human Cancer via Spatial Transcriptomics**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Bulk_RNA-seq_Guided_Multi-modal_Detection_of_Anomalous_Regions_in_Human_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39670.png" alt="Bulk RNA-seq Guided Multi-modal Detection of Anomalous Regions in Human Cancer via Spatial Transcriptomics poster" width="420">
  - Authors: Hang Shi, Ruocheng Yang, Wenjie You, Zhilin Huang, Daoqiang Zhang, WEI SHAO
  - Session: Poster Session 6
  - Tags: `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41041) **C3-Diff: Super-resolving Spatial Transcriptomics via Cross-modal Cross-content Contrastive Diffusion Modelling**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38354) **CARE: A Molecular-Guided Foundation Model with Adaptive Region Modeling for Whole Slide Image Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_CARE_A_Molecular-Guided_Foundation_Model_with_Adaptive_Region_Modeling_for_CVPR_2026_paper.html) [GitHub](https://github.com/zdipath/CARE) [arXiv](https://arxiv.org/abs/2602.21637) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38354.png" alt="CARE: A Molecular-Guided Foundation Model with Adaptive Region Modeling for Whole Slide Image Analysis poster" width="420">
  - Authors: Di Zhang, Zhangpeng Gong, Xiaobo Pang, Jiashuai Liu, Junbo Lu, Hao Cui, Jiusong Ge, Zhi Zeng, Kai Yi, Yinghua Li, ... (+7 more)
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41454) **CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare**
  - Session: Findings Poster Session 3
  - Tags: `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37175) **Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Nishimura_Cell-Type_Prototype-Informed_Neural_Network_for_Gene_Expression_Estimation_from_Pathology_CVPR_2026_paper.html) [Project](https://naivete5656.github.io/CPNN/) [Video](https://www.youtube-nocookie.com/embed/_ak55qv_eO0) [arXiv](https://arxiv.org/abs/2603.18461) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/37175.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37175.png" alt="Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images poster" width="420">
  - Authors: Kazuya Nishimura, Ryoma Bise, Shinnosuke Matsuo, Haruka Hirose, Yasuhiro Kojima
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38006) **CG-Reasoner: Centroid-Guided Positional Reasoning Segmentation for Medical Imaging with a Robust Visual-Text Consistency Metric**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Polamreddy_CG-Reasoner_Centroid-Guided_Positional_Reasoning_Segmentation_for_Medical_Imaging_with_a_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/CSbdR7pXw0k) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38006.png" alt="CG-Reasoner: Centroid-Guided Positional Reasoning Segmentation for Medical Imaging with a Robust Visual-Text Consistency Metric poster" width="420">
  - Authors: Lakshmikar R., Ming Ma
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41433) **CheXmix: Unified Generative Pretraining for Vision Language Models in Medical Imaging**
  - Session: Findings Poster Session 3
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39693) **Clinically-Grounded Counterfactual Reasoning for Medical Video Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Clinically-Grounded_Counterfactual_Reasoning_for_Medical_Video_Diagnosis_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39693.png" alt="Clinically-Grounded Counterfactual Reasoning for Medical Video Diagnosis poster" width="420">
  - Authors: Jianzhe Gao, Churan Wang, Weiyi Zhang, Jianghua Li, Lian Li, Wenguan Wang, Yixin Zhu, Yizhou Wang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37941) **CMR-RD: Long-Tailed Adaptive VLM for Explainable CMR Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CMR-RD_Long-Tailed_Adaptive_VLM_for_Explainable_CMR_Diagnosis_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37941.png" alt="CMR-RD: Long-Tailed Adaptive VLM for Explainable CMR Diagnosis poster" width="420">
  - Authors: Yansong Li, Zhongxi Qiu, Yun Tian, Zheng jinyu, Shuo Li
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37123) **CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sultana_CoFiDA-M_Concept-Aware_Feature_Modulation_for_Cross-Domain_Adaptation_with_Image-Only_Inference_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/fD9SiGbGIxc) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37123.png" alt="CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference poster" width="420">
  - Authors: Nurjahan Sultana, Moi Hoon Yap, Xinqi Fan, Wenqi Lu
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Dermatology / Skin`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41240) **Continual Alignment for SAM:  Rethinking Foundation Models for Medical Image Segmentation in Continual Learning**
  - Session: Findings Poster Session 3
  - Tags: `Medical AI / General`, `Segmentation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36817) **Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Continual_Learning_for_fMRI-Based_Brain_Disorder_Diagnosis_via_Functional_Connectivity_CVPR_2026_paper.html) [GitHub](https://github.com/4me808/FORGE) [arXiv](https://arxiv.org/abs/2604.14259) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36817.png" alt="Continual Learning for fMRI-Based Brain Disorder Diagnosis via Functional Connectivity Matrices Generative Replay poster" width="420">
  - Authors: qianyu Chen, Shujian Yu
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39371) **Cross-domain Dual-stream Feature Disentanglement for Brain Disorder Prediction with Sparsely Labeled PET**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Cross-domain_Dual-stream_Feature_Disentanglement_for_Brain_Disorder_Prediction_with_Sparsely_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/OJvup4i7O50) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39371.png" alt="Cross-domain Dual-stream Feature Disentanglement for Brain Disorder Prediction with Sparsely Labeled PET poster" width="420">
  - Authors: Huabin Wang, Xinyu Chen, Yuan Zhou, Fei Liu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38037) **Cross-Slice Knowledge Transfer via Masked Multi-Modal Heterogeneous Graph Contrastive Learning for Spatial Gene Expression Inference**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Cross-Slice_Knowledge_Transfer_via_Masked_Multi-Modal_Heterogeneous_Graph_Contrastive_Learning_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.22821) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38037.png" alt="Cross-Slice Knowledge Transfer via Masked Multi-Modal Heterogeneous Graph Contrastive Learning for Spatial Gene Expression Inference poster" width="420">
  - Authors: Zhiceng Shi, Changmiao Wang, Jun Wan, Wenwen Min
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38658) **CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_CROWn_A_Unified_Framework_for_Anti-Aliased_Downsampling_and_Phase-Calibrated_Fusion_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38658.png" alt="CROWn: A Unified Framework for Anti‑Aliased Downsampling and Phase‑Calibrated Fusion in 3D Medical Segmentation poster" width="420">
  - Authors: Xingru Huang, Shuanghua Ye, Zhao Huang, Wenwen Tang, Huiyu Zhou, Zhiwen Zheng, Jin Liu, Xiaoshuai Zhang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `OCT / Ophthalmology / Retina`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37344) **D2T2 - Multimodal Automated Planning for Brachytherapy**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Moore_D2T2_-_Multimodal_Automated_Planning_for_Brachytherapy_CVPR_2026_paper.html) [GitHub](https://github.com/UCSD-Health-QUIVER/D2T2) [Video](https://www.youtube-nocookie.com/embed/TAcxI1204cw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37344.png" alt="D2T2 - Multimodal Automated Planning for Brachytherapy poster" width="420">
  - Authors: Lance C. Moore, Aranyo Mitra, Ryan Truong, Karoline Kallis, Kelly Kisling, Sandra M. Meyers, Nuno Vasconcelos
  - Session: Poster Session 6
  - Tags: `Mammography / Breast`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36514) **DARC: Dual Adjustment Reasoning with Counterfactuals for Trustworthy Chest X-ray Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_DARC_Dual_Adjustment_Reasoning_with_Counterfactuals_for_Trustworthy_Chest_X-ray_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/8AC2roAq1I8) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36514.png" alt="DARC: Dual Adjustment Reasoning with Counterfactuals for Trustworthy Chest X-ray Classification poster" width="420">
  - Authors: Zhifang Liao, Junhao Li, HaoKang Ding, Yucheng Song
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41011) **Deep-to-Shallow Knowledge Transfer:Multi-Scale Self-Distillation with Bidirectional Aware for 3D Brain Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41031) **DELRER: Disease Evolution-Informed Longitudinal Radiology Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37051) **Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Delving_Aleatoric_Uncertainty_in_Medical_Image_Segmentation_via_Vision_Foundation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.10963) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37051.png" alt="Delving Aleatoric Uncertainty in Medical Image Segmentation via Vision Foundation Models poster" width="420">
  - Authors: Ruiyang Li, Fang Liu, Licheng Jiao, Xinglin Xie, Jiayao Hao, Shuo Li, Xu Liu, Jingyi yang, Lingling Li, Puhua Chen, ... (+1 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41021) **DepthScopy: Decoupling Frequency for Endoscopic Depth Estimation in Sparsely-Textured Regions**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37988) **Diffusion MRI Transformer with a Diffusion Space Rotary Positional Embedding (D-RoPE)**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kung_Diffusion_MRI_Transformer_with_a_Diffusion_Space_Rotary_Positional_Embedding_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/B-JsuTK1luk) [arXiv](https://arxiv.org/abs/2603.25977) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37988.png" alt="Diffusion MRI Transformer with a Diffusion Space Rotary Positional Embedding (D-RoPE) poster" width="420">
  - Authors: Gustavo Chau Loo Kung, Mohammad H. Abbasi, Camila Blank, Juze Zhang, Alan Q. Wang, Sophie Ostmeier, Akshay Chaudhari, Kilian Pohl, Ehsan Adeli
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38059) **Diffusion-Based Native Adversarial Synthesis for Enhanced Medical Segmentation Generalization**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Diffusion-Based_Native_Adversarial_Synthesis_for_Enhanced_Medical_Segmentation_Generalization_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38059.png" alt="Diffusion-Based Native Adversarial Synthesis for Enhanced Medical Segmentation Generalization poster" width="420">
  - Authors: Hongyu Zhang, Haipeng Chen, Zhimin Xu, Chengxin Yang, Yingda Lyu
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Medical AI / General`, `Segmentation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38134) **Divide, Conquer, and Aggregate: Asymmetric Experts for Class-Imbalanced Semi-Supervised Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Divide_Conquer_and_Aggregate_Asymmetric_Experts_for_Class-Imbalanced_Semi-Supervised_Medical_CVPR_2026_paper.html) [GitHub](https://github.com/PHPJava666/DCA) [Video](https://www.youtube-nocookie.com/embed/rUjLlvNsrDs) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38134.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38134.png" alt="Divide, Conquer, and Aggregate: Asymmetric Experts for Class-Imbalanced Semi-Supervised Medical Image Segmentation poster" width="420">
  - Authors: Yajun Liu
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37060) **DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_DK-DDIL_Adaptive_Knowledge_Retention_for_Dynamic_Domain-Incremental_Learning_in_Medical_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37060.png" alt="DK-DDIL: Adaptive Knowledge Retention for Dynamic Domain-Incremental Learning in Medical Imaging poster" width="420">
  - Authors: Yuxi Ma, Sujie Liu, Jing Yang, Jiacheng Wang, Yiping Chen, Baptiste Magnier, Liansheng Wang
  - Session: Poster Session 6 | Oral Session 6C: Medical Vision
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41046) **Do Vision Models Perceive Illusory Motion in Static Images Like Humans?**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36918) **Dual-Level Confidence based Implicit Self-Refinement for Medical Visual Question Answering**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_Dual-Level_Confidence_based_Implicit_Self-Refinement_for_Medical_Visual_Question_Answering_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/AupEFPNUCwI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36918.png" alt="Dual-Level Confidence based Implicit Self-Refinement for Medical Visual Question Answering poster" width="420">
  - Authors: Meihong Pan, Yefeng Zheng
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39550) **Dual-Level Hypergraph Generation for Addressing Feature Scarcity in Whole-Slide Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yao_Dual-Level_Hypergraph_Generation_for_Addressing_Feature_Scarcity_in_Whole-Slide_Image_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39550.png" alt="Dual-Level Hypergraph Generation for Addressing Feature Scarcity in Whole-Slide Image Classification poster" width="420">
  - Authors: Shuilian Yao, Qi Jia, Qi Jia, Pengshuo Zhang, Lili Sun, Weimin Wang, Yanmei Zhu, Bo Zhang, Xin Fan
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36801) **Dynamic Stream Network for Combinatorial Explosion Problem in Deformable Medical Image Registration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Bi_Dynamic_Stream_Network_for_Combinatorial_Explosion_Problem_in_Deformable_Medical_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.19486) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36801.png" alt="Dynamic Stream Network for Combinatorial Explosion Problem in Deformable Medical Image Registration poster" width="420">
  - Authors: Shaochen Bi, Yuting He, Weiming Wang, Hao Chen
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Registration`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39099) **Dynamics-Aware Preference Optimization for Vision-Language Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Dynamics-Aware_Preference_Optimization_for_Vision-Language_Models_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: jusheng zhang, Kaitong Cai, Jing Yang, Jian Wang, Keze Wang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41033) **DynaMind: Reconstructing Dynamic Visual Scenes from EEG by Aligning Temporal Dynamics and Multimodal Semantics to Guided Diffusion**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39285) **EchoPOSE: 6D Pose Estimation of Sparse Echocardiograms for Left-Ventricular 3D Shape Reconstruction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Iijima_EchoPOSE_6D_Pose_Estimation_of_Sparse_Echocardiograms_for_Left-Ventricular_3D_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/VcV4cmd0RnI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39285.png" alt="EchoPOSE: 6D Pose Estimation of Sparse Echocardiograms for Left-Ventricular 3D Shape Reconstruction poster" width="420">
  - Authors: Lucas Iijima, Yihao Luo, Dario Sesia, Amit Kaura, Jamil Mayet, Choon Hwai Yap
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Ultrasound / Sonography`, `Medical AI / General`, `Organs / Anatomy`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41057) **EI: Early Intervention for Multimodal Imaging Based Disease Recognition**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41055) **Elicit and Enhance: Advancing Multimodal Reasoning in Medical Scenarios**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37063) **Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Qiu_Elucidating_the_Design_Space_of_Arbitrary-Noise-Based_Diffusion_Models_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2507.18534) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37063.png" alt="Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models poster" width="420">
  - Authors: Xingyu Qiu, Mengying Yang, Xinghua Ma, Dong Liang, Fanding Li, Gongning Luo, wei wang, Kuanquan Wang, Shuo Li
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Restoration / Reconstruction`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39300) **EMAD: Evidence-Centric Grounded Multimodal Diagnosis for Alzheimer’s Disease**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_EMAD_Evidence-Centric_Grounded_Multimodal_Diagnosis_for_Alzheimers_Disease_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Qiuhui Chen, Xuancheng Yao, Zhenglei Zhou, Xinyue Hu, Yi Hong
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37520) **Every Error has Its Magnitude: Asymmetric Mistake Severity Training for Multiclass Multiple Instance Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hong_Every_Error_has_Its_Magnitude_Asymmetric_Mistake_Severity_Training_for_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/MUjVlI-wZTI) [arXiv](https://arxiv.org/abs/2603.13682) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37520.png" alt="Every Error has Its Magnitude: Asymmetric Mistake Severity Training for Multiclass Multiple Instance Learning poster" width="420">
  - Authors: Sungrae Hong, Jiwon Jeong, Jisu Shin, Donghee Han, Sol Lee, Kyungeun Kim, Mun Yong Yi
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36172) **F^2-Assist: Multi-Phase Fetal Growth Forecast and Report Generation from Ultrasound Examination**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pu_F2-Assist_Multi-Phase_Fetal_Growth_Forecast_and_Report_Generation_from_Ultrasound_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36172.png" alt="F^2-Assist: Multi-Phase Fetal Growth Forecast and Report Generation from Ultrasound Examination poster" width="420">
  - Authors: Bin Pu, XUSHENG LIANG, Xinpeng Ding, Jinlin Wu, Zhen Lei, Shengli Li, Kenli Li, Jiawei Ma
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40901) **FA-MoE: Improving Medical Image Generation Through Frequency-Aware Mixture of Experts**
  - Session: Findings Poster Session 2
  - Tags: `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37778) **Factorized Context Aggregation for Robust Cancer Risk Estimation via Soft Re-Ranked Retrieval and Hierarchical Anchors**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Moghadam_Factorized_Context_Aggregation_for_Robust_Cancer_Risk_Estimation_via_Soft_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/0tQ3-O0yX44) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37778-thumb.png" alt="Factorized Context Aggregation for Robust Cancer Risk Estimation via Soft Re-Ranked Retrieval and Hierarchical Anchors poster" width="420">
  - Authors: Puria Azadi Moghadam, Ali Khajegili Mirabadi, Behnam Maneshgar, Hossein Farahani, Ali Bashashati
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39052) **FBTA: Enabling Single-GPU End-to-End Gigapixel WSI Classification with Feature Bridging and Translation Alignment**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_FBTA_Enabling_Single-GPU_End-to-End_Gigapixel_WSI_Classification_with_Feature_Bridging_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Jiuyang Dong, Jiahan Li, Junjun Jiang, Yongbing Zhang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38402) **Focus on Background: Exploring SAM's Potential in Few-shot Medical Image Segmentation with Background-centric Prompting**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Bo_Focus_on_Background_Exploring_SAMs_Potential_in_Few-shot_Medical_Image_CVPR_2026_paper.html) [GitHub](https://github.com/primebo1/FoB_SAM) [Video](https://www.youtube-nocookie.com/embed/ZjUE64YJZnU) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38402.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38402.png" alt="Focus on Background: Exploring SAM&#x27;s Potential in Few-shot Medical Image Segmentation with Background-centric Prompting poster" width="420">
  - Authors: Yuntian Bo, Yazhou Zhu, Piotr Koniusz, Haofeng Zhang
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38989) **Focus-to-Perceive Representation Learning: A Cognition-Inspired Hierarchical Framework for Endoscopic Video Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Focus-to-Perceive_Representation_Learning_A_Cognition-Inspired_Hierarchical_Framework_for_Endoscopic_Video_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/Dbzi1GLUM5M) [arXiv](https://arxiv.org/abs/2603.25778) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38989.png" alt="Focus-to-Perceive Representation Learning: A Cognition-Inspired Hierarchical Framework for Endoscopic Video Analysis poster" width="420">
  - Authors: Yuan Zhang, Sihao Dou, Kai Hu, Shuhua Deng, Chunhong Cao, Fen Xiao, Xieping Gao
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40245) **Forging a Dynamic Memory: Retrieval-Guided Continual Learning for Generalist Medical Foundation Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Forging_a_Dynamic_Memory_Retrieval-Guided_Continual_Learning_for_Generalist_Medical_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/MRwr-5ziOzg) [arXiv](https://arxiv.org/abs/2512.13072) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40245.png" alt="Forging a Dynamic Memory: Retrieval-Guided Continual Learning for Generalist Medical Foundation Models poster" width="420">
  - Authors: Zizhi Chen, Yizhen Gao, Minghao Han, Yizhou Liu, Zhaoyu Chen, Dingkang Yang, Lihua Zhang
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41027) **From Adaptation to Generalization: Adaptive Visual Prompting for Medical Image Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36239) **From Infusion to Assimilation Distillation for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hong_From_Infusion_to_Assimilation_Distillation_for_Medical_Image_Segmentation_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36239.png" alt="From Infusion to Assimilation Distillation for Medical Image Segmentation poster" width="420">
  - Authors: Jiankang Hong, Ye Luo, Yinan Liu, Junsong Yuan
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Segmentation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37012) **From Panel to Pixel: Zoom-In Vision–Language Pretraining from Biomedical Scientific Literature**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yuan_From_Panel_to_Pixel_Zoom-In_Vision-Language_Pretraining_from_Biomedical_Scientific_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/ajAY15bYzlA) [arXiv](https://arxiv.org/abs/2512.02566) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37012.png" alt="From Panel to Pixel: Zoom-In Vision–Language Pretraining from Biomedical Scientific Literature poster" width="420">
  - Authors: Kun yuan, Min Woo, Zhen Chen, Alejandro Lozano, Xiangteng He, Shi Li, Nassir Navab, Xiaoxiao Sun, Nicolas Padoy, Serena Yeung
  - Session: Poster Session 6
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38379) **Gastric-X: A Multimodal Multi-Phase Benchmark Dataset for Advancing Vision-Language Models in Gastric Cancer Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Gastric-X_A_Multimodal_Multi-Phase_Benchmark_Dataset_for_Advancing_Vision-Language_Models_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/u-wJG8A8JqY) [arXiv](https://arxiv.org/abs/2603.19516) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38379.png" alt="Gastric-X: A Multimodal Multi-Phase Benchmark Dataset for Advancing Vision-Language Models in Gastric Cancer Analysis poster" width="420">
  - Authors: Yuanzhe Li, Hao Chen, Rui Yin, Juyan Ba, Yu Zhang, Sheng Lu
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `CT / Tomography`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41052) **Gated Differential Linear Attention: A Linear-Time Decoder for High-Fidelity Medical Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41036) **Gaze into the Details: Locality-Sensitive Enhancement for OCTA Retinal Vessel Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41014) **Generative Vision-Language Multiple Instance Learning for Weakly Supervised Neonatal Fundus Screening and Reporting**
  - Session: Findings Poster Session 2
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38090) **GeneVAR: Causal MeanFlow for Autoregressive Gene-to-WSI Tile Synthesis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_GeneVAR_Causal_MeanFlow_for_Autoregressive_Gene-to-WSI_Tile_Synthesis_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/tbAYSmYHAhI) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38090_rjx4RQq.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38090.png" alt="GeneVAR: Causal MeanFlow for Autoregressive Gene-to-WSI Tile Synthesis poster" width="420">
  - Authors: Jianwei Zhao, Fan Yang, XIN LI, Qiang Zhai, Ao Luo, Ziqi Ren, Zhicheng Jiao, Hong Cheng
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36683) **GeoSemba: Reconstructing State Space Model for Cross Paradigm Representation in Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_GeoSemba_Reconstructing_State_Space_Model_for_Cross_Paradigm_Representation_in_CVPR_2026_paper.html) [GitHub](https://github.com/Mrliujunwen/GeoSemba) [Video](https://www.youtube-nocookie.com/embed/zS3L7cr9LQI) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/36683.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36683.png" alt="GeoSemba: Reconstructing State Space Model for Cross Paradigm Representation in Medical Image Segmentation poster" width="420">
  - Authors: Xutao Sun, Jiarui Li, Junwen Liu, Yonggong Ren
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40015) **GH-NAF: Grid-Adaptive Hash-Level–Attended Neural Attenuation Fields for Discrepancy-Aware CBCT**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Oh_GH-NAF_Grid-Adaptive_Hash-Level-Attended_Neural_Attenuation_Fields_for_Discrepancy-Aware_CBCT_CVPR_2026_paper.html) [Project](https://limchaeyeon1003.github.io/GH_NAF_CVPR/) [Video](https://www.youtube-nocookie.com/embed/iNo39VR-ieY) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/40015.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40015.png" alt="GH-NAF: Grid-Adaptive Hash-Level–Attended Neural Attenuation Fields for Discrepancy-Aware CBCT poster" width="420">
  - Authors: Seong Je Oh, Ju Hwan Lee, Chae Yeon Lim, Donghwan Lee, Myung Jin Ching, Kyungsu Kim
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39862) **HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_HalluGen_Synthesizing_Realistic_and_Controllable_Hallucinations_for_Evaluating_Image_Restoration_CVPR_2026_paper.html) [GitHub](https://github.com/edshkim98/HalluGen) [arXiv](https://arxiv.org/abs/2512.03345) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39862.png" alt="HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration poster" width="420">
  - Authors: Seunghoi Kim, Henry F. J. Tregidgo, Chen Jin, Matteo Figini, Daniel C. Alexander
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36764) **Harmonized Feature Conditioning and Frequency-Prompt Personalization for Multi-Rater Medical Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Karimijafarbigloo_Harmonized_Feature_Conditioning_and_Frequency-Prompt_Personalization_for_Multi-Rater_Medical_Segmentation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/f5ji6hDpHUQ) [arXiv](https://arxiv.org/abs/2605.08210) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36764.png" alt="Harmonized Feature Conditioning and Frequency-Prompt Personalization for Multi-Rater Medical Segmentation poster" width="420">
  - Authors: Sanaz Karimijafarbigloo, Armin Khosravi, Alireza Kheyrkhah, Reza Azad, Mauricio Reyes, Dorit Merhof
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41059) **HazeMatching: Dehazing Light Microscopy Images with Guided Conditional Flow Matching**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36890) **Hyperbolic Relational Prompts for Intersectional Fairness in Medical VLMs**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_Hyperbolic_Relational_Prompts_for_Intersectional_Fairness_in_Medical_VLMs_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36890.png" alt="Hyperbolic Relational Prompts for Intersectional Fairness in Medical VLMs poster" width="420">
  - Authors: Jiayu Qian, Zongxian Yang, Guanxing Chen, Pengwei Hu, KC Tan, Yan Wang, Yu-An Huang, Zhi-An Huang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39159) **HyperST: Hierarchical Hyperbolic Learning for Spatial Transcriptomics Prediction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_HyperST_Hierarchical_Hyperbolic_Learning_for_Spatial_Transcriptomics_Prediction_CVPR_2026_paper.html) [GitHub](https://github.com/liesgame/HyperST) [Video](https://www.youtube-nocookie.com/embed/QLru19GiigM) [arXiv](https://arxiv.org/abs/2511.22107) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/39159.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39159.png" alt="HyperST: Hierarchical Hyperbolic Learning for Spatial Transcriptomics Prediction poster" width="420">
  - Authors: Chen Zhang, Yilu An, Ying Chen, Hao Li, Xitong Ling, Lihao Liu, Junjun He, Yuxiang Lin, Zihui Wang, Rongshan Yu
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39581) **IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_IBISAgent_Reinforcing_Pixel-Level_Visual_Reasoning_in_MLLMs_for_Universal_Biomedical_CVPR_2026_paper.html) [GitHub](https://github.com/Yankai96/IBISAgent) [Video](https://www.youtube-nocookie.com/embed/dYr9jUxdgGE) [arXiv](https://arxiv.org/abs/2601.03054) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/39581_7XoRU9y.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39581.png" alt="IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation poster" width="420">
  - Authors: Yankai Jiang, Qiaoru Li, BinLu Xu, Haoran Sun, Chao Ding, Junting Dong, Yuxiang Cai, Xuhong Zhang, Jianwei Yin
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39258) **IEBGL:An Interpretability-Enhanced Brain Graph Learning Framework with LLM-Instructed Topology and Literature-Augmented Semantics**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Duan_IEBGLAn_Interpretability-Enhanced_Brain_Graph_Learning_Framework_with_LLM-Instructed_Topology_and_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39258.png" alt="IEBGL:An Interpretability-Enhanced Brain Graph Learning Framework with LLM-Instructed Topology and Literature-Augmented Semantics poster" width="420">
  - Authors: Yihang Duan, Shuo Huang, Lizhang Lizhang, Meiling Wang, Li Zhang
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37680) **InvCoSS: Inversion-driven Continual Self-supervised Learning in Medical Multi-modal Image Pre-training**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_InvCoSS_Inversion-driven_Continual_Self-supervised_Learning_in_Medical_Multi-modal_Image_Pre-training_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.19213) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Zihao Luo, Shaohao Rui, Zhenyu Tang, Guotai Wang, Xiaosong Wang
  - Session: Poster Session 6
  - Tags: `Medical AI / General`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37003) **IVAAN: Instance-level Vision-Language Alignment via Attribute-Guided Text Prompts Generation for Nuclei Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jeong_IVAAN_Instance-level_Vision-Language_Alignment_via_Attribute-Guided_Text_Prompts_Generation_for_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/F6fSCuKL9Hs) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37003.png" alt="IVAAN: Instance-level Vision-Language Alignment via Attribute-Guided Text Prompts Generation for Nuclei Analysis poster" width="420">
  - Authors: Jaehoon Jeong, Yi Hu, Soopil Kim, Jongseong Jang, Soonyoung Lee, Sang Hyun Park
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38708) **KAMP: Knowledge-Anchored Multimodal Pretraining Framework for Medical Image Representation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_KAMP_Knowledge-Anchored_Multimodal_Pretraining_Framework_for_Medical_Image_Representation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/rU4ie5wfIVg) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38708.png" alt="KAMP: Knowledge-Anchored Multimodal Pretraining Framework for Medical Image Representation poster" width="420">
  - Authors: Feiyu Huang, Jia Li, Zhao CHEN, Yang WU, Caleb Chen Cao, Lei Chen
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38145) **Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Khan_Keep_It_Frozen_Domain-Routed_Conditional_Residual_Modulation_for_Multi-Domain_Vision_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/q18ZYEyK7Tw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38145.png" alt="Keep It Frozen: Domain-Routed Conditional Residual Modulation for Multi-Domain Vision Transformers poster" width="420">
  - Authors: Ufaq Khan, Umair Nawaz, Massimo Caputo, Muhammad Bilal, Junaid Qadir, Muhammad Haris Khan
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36670) **LATA: Laplacian-Assisted Transductive Adaptation for Conformal Uncertainty in Medical VLMs**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Bozorgtabar_LATA_Laplacian-Assisted_Transductive_Adaptation_for_Conformal_Uncertainty_in_Medical_VLMs_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/Lspv-w6CXOU) [arXiv](https://arxiv.org/abs/2602.17535) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36670.png" alt="LATA: Laplacian-Assisted Transductive Adaptation for Conformal Uncertainty in Medical VLMs poster" width="420">
  - Authors: Behzad Bozorgtabar, Dwarikanath Mahapatra, Sudipta Roy, Muzammal Naseer, Imran Razzak, Zongyuan Ge
  - Session: Poster Session 6 | Oral Session 6C: Medical Vision
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36397) **Learning complete and explainable visual representations from itemized text supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_Learning_complete_and_explainable_visual_representations_from_itemized_text_supervision_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/X9lDEqtVGpo) [arXiv](https://arxiv.org/abs/2512.11141) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36397.png" alt="Learning complete and explainable visual representations from itemized text supervision poster" width="420">
  - Authors: Yiwei Lyu, Chenhui Zhao, Soumyanil Banerjee, Shixuan Liu, Akshay Rao, Akhil Kondepudi, Honglak Lee, Todd C. Hollon
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39688) **Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Matinkia_Learning_Diffeomorphism_for_Medical_Image_Registration_with_Time-Embedded_Architectures_Using_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/ss_GC9hi-7k) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39688.png" alt="Learning Diffeomorphism for Medical Image Registration with Time-Embedded Architectures Using Semigroup Regularization poster" width="420">
  - Authors: Mohammadjavad Matinkia, Nilanjan Ray
  - Session: Poster Session 5 & Exhibit Hall | Oral Session 5C: Geometry and Robotics
  - Tags: `CT / Tomography`, `Medical AI / General`, `Registration`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41017) **Learning from Noisy Prompts: Saliency-Guided Prompt Distillation for Robust Segmentation with SAM**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36666) **Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Learning_Generalizable_3D_Medical_Image_Representations_from_Mask-Guided_Self-Supervision_CVPR_2026_paper.html) [GitHub](https://github.com/Stanford-AIMI/MASS?tab=readme-ov-file) [arXiv](https://arxiv.org/abs/2603.13660) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36666.png" alt="Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision poster" width="420">
  - Authors: Yunhe Gao, Yabin Zhang, Chong Wang, Jiaming Liu, Maya Varma, Jean-Benoit Delbrouck, Akshay Chaudhari, Curtis Langlotz
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41060) **Learning Priors via Hybrid Visual Autoregressive Modeling for Medical Image to Image Translation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41043) **Learning Spatial-Preserving Hierarchical Representations for Digital Pathology**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37076) **Learning Surgical Robotic Manipulation with 3D Spatial Priors**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sheng_Learning_Surgical_Robotic_Manipulation_with_3D_Spatial_Priors_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.03798) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Yu Sheng, Lidian Wang, Xiaomeng Chu, Jiajun Deng, Min Cheng, Yanyong Zhang, Bei Hua, Houqiang Li, Jianmin Ji
  - Session: Poster Session 6
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Surgery / Medical Video`, `Medical AI / General`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38975) **LLaDA-MedV: Exploring Large Language Diffusion Models for Biomedical Image Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_LLaDA-MedV_Exploring_Large_Language_Diffusion_Models_for_Biomedical_Image_Understanding_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/qpNe3qugRMw) [arXiv](https://arxiv.org/abs/2508.01617) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38975.png" alt="LLaDA-MedV: Exploring Large Language Diffusion Models for Biomedical Image Understanding poster" width="420">
  - Authors: XUANZHAO DONG, Wenhui Zhu, Xiwen Chen, Zhipeng Wang, Peijie Qiu, Shao Tang, Xin Li, Yalin Wang
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41069) **LlamaRG: A Multi-View Large Language Model for Radiology Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38951) **LUMINA: A Multi-Vendor Mammography Benchmark with Energy Harmonization Protocol**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Pan_LUMINA_A_Multi-Vendor_Mammography_Benchmark_with_Energy_Harmonization_Protocol_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/rtUfsZegJCM) [arXiv](https://arxiv.org/abs/2603.14644) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38951.png" alt="LUMINA: A Multi-Vendor Mammography Benchmark with Energy Harmonization Protocol poster" width="420">
  - Authors: Hongyi Pan, Gorkem Durak, Halil Ertugrul Aktas, Andrea M. Bejar, Baver Tutun, Emre Uysal, Ezgi Bülbül, Mehmet Faith Dogan, Berrin Erok, Berna Yildirim, ... (+2 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Mammography / Breast`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41037) **M^3D-BFS: a Multi-Stage Dynamic Fusion Strategy for Sample-Adaptive Multi-Modal Brain Network Analysis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41032) **M^4Fuse: Lightweight State-Space MoE with a Cross-Scale Gating Bridge for Brain Tumor Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41034) **MAE-XNT: A Foundation Model for Segmenting Neuronal Tissue Volumes Generated with X-Ray Nanotomography**
  - Session: Findings Poster Session 2
  - Tags: `X-Ray / Radiography`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39592) **Masked-Diffusion Autoencoders for 3D Medical Vision Representation Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Tu_Masked-Diffusion_Autoencoders_for_3D_Medical_Vision_Representation_Learning_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Jiachen Tu, Guanghui Qin, Theodore Zhengde Zhao, Jeya Maria Jose Valanarasu, Sheng Zhang, Tristan Naumann, Fan Lam, Sheng Wang, Hoifung Poon
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`, `Restoration / Reconstruction`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38829) **MDCS-MoAME: Multi-directional Composite Scanning with Mixture of Attention and Mamba Experts for Cancer Survival Prediction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Qu_MDCS-MoAME_Multi-directional_Composite_Scanning_with_Mixture_of_Attention_and_Mamba_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/3sLmvKC54OM) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38829.png" alt="MDCS-MoAME: Multi-directional Composite Scanning with Mixture of Attention and Mamba Experts for Cancer Survival Prediction poster" width="420">
  - Authors: Linjie Qu, Jin Xiao, Xiangrong Liu, Changming Sun, Hui Cui, Yuqi Fang, Ran Su, Qiangguo Jin, leyi wei
  - Session: Poster Session 3 & Exhibit Hall | Oral Session 3D: Multimodal Modeling
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36693) **Med-CMR: A Fine-Grained Benchmark Integrating Visual Evidence and Clinical Logic for Medical Complex Multimodal Reasoning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Med-CMR_A_Fine-Grained_Benchmark_Integrating_Visual_Evidence_and_Clinical_Logic_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.00818) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36693.png" alt="Med-CMR: A Fine-Grained Benchmark Integrating Visual Evidence and Clinical Logic for Medical Complex Multimodal Reasoning poster" width="420">
  - Authors: Haozhen Gong, Xiaozhong Ji, Yuansen Liu, Wenbin Wu, Xiaoxiao Yan, jingjing liu, Kai WU, Jiazhen Pan, Bailiang Jian, Jiangning Zhang, ... (+2 more)
  - Session: Poster Session 6
  - Tags: `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36331) **MedCLIPSeg: Probabilistic Vision-Language Adaptation for Data-Efficient and Generalizable Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Koleilat_MedCLIPSeg_Probabilistic_Vision-Language_Adaptation_for_Data-Efficient_and_Generalizable_Medical_Image_CVPR_2026_paper.html) [Project](https://tahakoleilat.github.io/MedCLIPSeg/) [Video](https://www.youtube-nocookie.com/embed/1LFbNEXfsv0) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36331.png" alt="MedCLIPSeg: Probabilistic Vision-Language Adaptation for Data-Efficient and Generalizable Medical Image Segmentation poster" width="420">
  - Authors: Taha Koleilat, Hojat Asgariandehkordi, Omid Nejatimanzari, Berardino Barile, Yiming Xiao, Hassan Rivaz
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38268) **MedFG-VQA: Low-Frequency Memory and Graph Attention for Lightweight Medical VQA**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_MedFG-VQA_Low-Frequency_Memory_and_Graph_Attention_for_Lightweight_Medical_VQA_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38268.png" alt="MedFG-VQA: Low-Frequency Memory and Graph Attention for Lightweight Medical VQA poster" width="420">
  - Authors: haowen gu, Gensheng Pei, Zeren Sun, Mingwu Ren, Xiangbo Shu, Yazhou Yao, Fumin Shen
  - Session: Poster Session 6
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40035) **MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Su_MedGRPO_Multi-Task_Reinforcement_Learning_for_Heterogeneous_Medical_Video_Understanding_CVPR_2026_paper.html) [Project](https://uii-america.github.io/MedGRPO/) [Video](https://www.youtube-nocookie.com/embed/RRS5O0BziDA) [arXiv](https://arxiv.org/abs/2512.06581) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40035.png" alt="MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding poster" width="420">
  - Authors: Yuhao Su, Anwesa Choudhuri, Zhongpai Gao, Benjamin Planche, Van Nguyen Nguyen, Meng Zheng, Yuhan Shen, Arun Innanje, Terrence Chen, Ehsan Elhamifar, ... (+1 more)
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Surgery / Medical Video`, `Medical AI / General`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39445) **Medic-AD: Towards Medical Vision-Language Model's Clinical Intelligence**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Medic-AD_Towards_Medical_Vision-Language_Models_Clinical_Intelligence_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/OMB4pYja1Yw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39445.png" alt="Medic-AD: Towards Medical Vision-Language Model&#x27;s Clinical Intelligence poster" width="420">
  - Authors: Woohyeon Park, Jaeik Kim, Sunghwan Steve Cho, Pa Hong, Wookyoung Jeong, Yoojin Nam, Namjoon Kim, Ginny Y. Wong, Ka Chun Cheung, Jaeyoung Do
  - Session: Poster Session 6 | Oral Session 6C: Medical Vision
  - Tags: `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38769) **MedKCO: Medical Vision-Language Pretraining via Knowledge-Driven Cognitive Orchestration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_MedKCO_Medical_Vision-Language_Pretraining_via_Knowledge-Driven_Cognitive_Orchestration_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.09101) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38769.png" alt="MedKCO: Medical Vision-Language Pretraining via Knowledge-Driven Cognitive Orchestration poster" width="420">
  - Authors: Chenran Zhang, Ruiqi Wu, Tao Zhou, Yi Zhou
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37424) **MedLIME: A Distribution-Aligned and Evidence-Supported Framework for Medical Saliency Explanations**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Magazine_MedLIME_A_Distribution-Aligned_and_Evidence-Supported_Framework_for_Medical_Saliency_Explanations_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/MWSVnwGJfAA) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37424.png" alt="MedLIME: A Distribution-Aligned and Evidence-Supported Framework for Medical Saliency Explanations poster" width="420">
  - Authors: Raghav Magazine, Xingjian Li, Min Xu
  - Session: Poster Session 6
  - Tags: `Medical AI / General`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38343) **MedLoc-R1: Performance-Aware Curriculum Reward Scheduling for GRPO-Based Medical Visual Grounding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_MedLoc-R1_Performance-Aware_Curriculum_Reward_Scheduling_for_GRPO-Based_Medical_Visual_Grounding_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.28120) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38343.png" alt="MedLoc-R1: Performance-Aware Curriculum Reward Scheduling for GRPO-Based Medical Visual Grounding poster" width="420">
  - Authors: Yang Guangjing, Ziyuan Qin, Chaoran Zhang, Chenlin Du, Jinglin Wang, Wanran Sun, Zhenyu Zhang, Bing Ji, Qicheng Lao
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38440) **MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Deria_MedMO_Grounding_and_Understanding_Multimodal_Large_Language_Model_for_Medical_CVPR_2026_paper.html) [Project](https://genmilab.github.io/MedMO-Page) [Video](https://www.youtube-nocookie.com/embed/xax7e0fMMGI) [arXiv](https://arxiv.org/abs/2602.06965) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38440.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38440.png" alt="MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images poster" width="420">
  - Authors: Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre, Eran Segal, Salman Khan, Imran Razzak
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `OCT / Ophthalmology / Retina`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41012) **MedSAD-CLIP: Supervised CLIP with Token-Patch Cross-Attention for Medical Anomaly Detection and Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39591) **MedTVT-R1: A Multimodal LLM Empowering Medical Reasoning and Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_MedTVT-R1_A_Multimodal_LLM_Empowering_Medical_Reasoning_and_Diagnosis_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2506.18512) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39591.png" alt="MedTVT-R1: A Multimodal LLM Empowering Medical Reasoning and Diagnosis poster" width="420">
  - Authors: Yuting Zhang, Kaishen Yuan, Hao Lu, Yutao Yue, Jintai Chen, Kaishun Wu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41042) **MeMix: Multi-Encoder Mixture Framework for Medical Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41047) **Meta-CDMTransNet: Cross-Domain Multi-Scale Transformer Meta-Learning Framework for Few-Shot Breast Histopathological Image Classification**
  - Session: Findings Poster Session 2
  - Tags: `Mammography / Breast`, `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41227) **MHMamba: Multi-Head Mamba for 3D Brain Tumor Segmentation**
  - Session: Findings Poster Session 3
  - Tags: `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41015) **Mitigating Batch Effects in Histopathology via Language-Mediated Robust Embedding Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36253) **MLLM-HWSI: A Multimodal Large Language Model for Hierarchical Whole Slide Image Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Alawode_MLLM-HWSI_A_Multimodal_Large_Language_Model_for_Hierarchical_Whole_Slide_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/7N0TG8naav0) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36253.png" alt="MLLM-HWSI: A Multimodal Large Language Model for Hierarchical Whole Slide Image Understanding poster" width="420">
  - Authors: Basit Alawode, Arif Mahmood, Muaz Radi, Shahad Albastaki, Asim Khan, Muhammad Bilal, Moshira Ali Abdalla, Mohammed Bennamoun, Sajid Javed
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38040) **Momentum Memory for Knowledge Distillation in Computational Pathology**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_Momentum_Memory_for_Knowledge_Distillation_in_Computational_Pathology_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/hO7-hZYK6rY) [arXiv](https://arxiv.org/abs/2602.21395) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38040.png" alt="Momentum Memory for Knowledge Distillation in Computational Pathology poster" width="420">
  - Authors: yongxin guo, Hao Lu, Onur C., Zhengjie Zhu, Muhammet F., Metin N.
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37934) **MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_MorphSeek_Fine-grained_Latent_Representation-Level_Policy_Optimization_for_Deformable_Image_Registration_CVPR_2026_paper.html) [GitHub](https://github.com/cai114514/MorphSeek) [Video](https://www.youtube-nocookie.com/embed/DGljUXt-A_w) [arXiv](https://arxiv.org/abs/2511.17392) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37934.png" alt="MorphSeek: Fine-grained Latent Representation-Level Policy Optimization for Deformable Image Registration poster" width="420">
  - Authors: Runxun Zhang, Yizhou Liu, Dongrui Li, Bo XU, Jingwei Wei
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Registration`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36898) **MR-RAG: Multimodal Relevance-Aware Retrieval-Augmented Generation for Medical Visual Question Answering**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_MR-RAG_Multimodal_Relevance-Aware_Retrieval-Augmented_Generation_for_Medical_Visual_Question_Answering_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36898.png" alt="MR-RAG: Multimodal Relevance-Aware Retrieval-Augmented Generation for Medical Visual Question Answering poster" width="420">
  - Authors: Xuze Li, Haozhao Wang, Zhenyu Huang, Zhongxu Wang, Zhang Jinghua, Ruixuan Li
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37460) **MRI Contrast Enhancement Kinetics World Model**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kong_MRI_Contrast_Enhancement_Kinetics_World_Model_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2602.19285) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37460.png" alt="MRI Contrast Enhancement Kinetics World Model poster" width="420">
  - Authors: Jindi Kong, Yuting He, Cong Xia, Rongjun Ge, Shuo Li
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37734) **Multimodal Causality-Driven Representation Learning for Generalizable Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_Multimodal_Causality-Driven_Representation_Learning_for_Generalizable_Medical_Image_Segmentation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2508.05008) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37734.png" alt="Multimodal Causality-Driven Representation Learning for Generalizable Medical Image Segmentation poster" width="420">
  - Authors: XUSHENG LIANG, Lihua Zhou, Nianxin Li, miao xu, Ziyang Song, Dong Yi, Jinlin Wu, Jiawei Ma, Hongbin Liu, Zhen Lei, ... (+1 more)
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41038) **Multimodal Decoupled Dynamic Graph Learning for Brain Disease Diagnosis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39054) **MUSE: Harnessing Precise and Diverse Semantics for Few-Shot Whole Slide Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_MUSE_Harnessing_Precise_and_Diverse_Semantics_for_Few-Shot_Whole_Slide_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/3-OpdgsF0lM) [arXiv](https://arxiv.org/abs/2602.20873) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39054.png" alt="MUSE: Harnessing Precise and Diverse Semantics for Few-Shot Whole Slide Image Classification poster" width="420">
  - Authors: Jiahao Xu, Sheng Huang, Xin Zhang, Zhixiong Nan, Jiajun Dong, Nankun Mu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40051) **MUST: Modality-Specific Representation-Aware Transformer for Diffusion-Enhanced Survival Prediction with Missing Modality**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_MUST_Modality-Specific_Representation-Aware_Transformer_for_Diffusion-Enhanced_Survival_Prediction_with_Missing_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/GGQ1YFcJdzE) [arXiv](https://arxiv.org/abs/2603.26071) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Kyungwon Kim, Dosik Hwang
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41035) **NAKUL-Med: Spectral-Graph State Space Models with Dynamics Kernels for Medical Signals**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39801) **OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ossowski_OctoMed_Data_Recipes_for_State-of-the-Art_Multimodal_Medical_Reasoning_CVPR_2026_paper.html) [Project](https://valiant-helmet-a30.notion.site/OctoMed-Data-Recipes-for-State-of-the-art-Multimodal-Medical-Reasoning-2b21be22fc9580d6bcc0e418905eb3f6) [Video](https://www.youtube-nocookie.com/embed/BsfPDuHM2GA) [arXiv](https://arxiv.org/abs/2511.23269) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39801.png" alt="OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning poster" width="420">
  - Authors: Timothy Ossowski, Sheng Zhang, Qianchu Liu, Guanghui Qin, Reuben Tan, Tristan Naumann, Junjie Hu, Hoifung Poon
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36258) **OmniBrainBench: A Comprehensive Multimodal Benchmark for Brain Imaging Analysis Across Multi-stage Clinical Tasks**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_OmniBrainBench_A_Comprehensive_Multimodal_Benchmark_for_Brain_Imaging_Analysis_Across_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/FN2xlmlMQUs) [arXiv](https://arxiv.org/abs/2511.00846) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36258.png" alt="OmniBrainBench: A Comprehensive Multimodal Benchmark for Brain Imaging Analysis Across Multi-stage Clinical Tasks poster" width="420">
  - Authors: Zhihao Peng, Cheng Wang, Shengyuan Liu, Zhiying Liang, Zanting Ye, Min Jie Ju, Peter YM Woo, Yixuan Yuan
  - Session: Poster Session 6
  - Tags: `Medical AI / General`, `Organs / Anatomy`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38725) **OmniFM: Toward Modality-Robust and Task-Agnostic Federated Learning for Heterogeneous Medical Imaging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_OmniFM_Toward_Modality-Robust_and_Task-Agnostic_Federated_Learning_for_Heterogeneous_Medical_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.21660) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38725.png" alt="OmniFM: Toward Modality-Robust and Task-Agnostic Federated Learning for Heterogeneous Medical Imaging poster" width="420">
  - Authors: meilin liu, Jiaying Wang, Jing Shan
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41044) **Open-Set Spatial Gene Expression Prediction from Histological Images via Retrieval-Augmented Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40162) **OralGPT-Plus: Learning to Use Visual Tools via Reinforcement Learning for Panoramic X-ray Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Fan_OralGPT-Plus_Learning_to_Use_Visual_Tools_via_Reinforcement_Learning_for_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.06366) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40162.png" alt="OralGPT-Plus: Learning to Use Visual Tools via Reinforcement Learning for Panoramic X-ray Analysis poster" width="420">
  - Authors: Yuxuan Fan, JING HAO, Hong Chen, Jiahao Bao, Yihua Shao, Yuci Liang, Kuo Feng Hung, Hao Tang
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40112) **OraPO: Oracle-educated Reinforcement Learning for Data-efficient and Factual Radiology Report Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_OraPO_Oracle-educated_Reinforcement_Learning_for_Data-efficient_and_Factual_Radiology_Report_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/LyjMwISk-R0) [arXiv](https://arxiv.org/abs/2509.18600) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/40112.png" alt="OraPO: Oracle-educated Reinforcement Learning for Data-efficient and Factual Radiology Report Generation poster" width="420">
  - Authors: Zhuoxiao Chen, Hongyang Yu, Ying Xu, Yadan Luo, Long Duong, Yuan-Fang Li
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41025) **PaM-MIL: Proliferation and Metastasis Enhanced Localization for Multiple Instance Learning on Pathology Images**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41051) **PBSBench: A Multi-Level Vision-Language Framework and Benchmark for Hematopathology Whole Slide Image Interpretation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37009) **PDD: Manifold-Prior Diverse Distillation for Medical Anomaly Detection**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_PDD_Manifold-Prior_Diverse_Distillation_for_Medical_Anomaly_Detection_CVPR_2026_paper.html) [GitHub](https://github.com/OxygenLu/PDD) [arXiv](https://arxiv.org/abs/2603.07142) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37009.png" alt="PDD: Manifold-Prior Diverse Distillation for Medical Anomaly Detection poster" width="420">
  - Authors: Xijun Lu, Hongying Liu, Fanhua Shang, Yanming hui, Liang Wan
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41045) **Personalized Functional Brain Network Modeling with Adaptive Auto-Weighted Learning for Automatic Brain Disorder Diagnosis**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38827) **Personalized Longitudinal Medical Report Generation via Temporally-Aware Federated Adaptation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Personalized_Longitudinal_Medical_Report_Generation_via_Temporally-Aware_Federated_Adaptation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2602.19668) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: He Zhu, Ren Togo, Takahiro Ogawa, Kenji Hirata, Minghui Tang, Takaaki Yoshimura, Hiroyuki Sugimori, Noriko Nishioka, Yukie Shimizu, Kohsuke Kudo, ... (+1 more)
  - Session: Poster Session 6
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39104) **PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Maqbool_PETAR_Localized_Findings_Generation_with_Mask-Aware_Vision-Language_Modeling_for_PET_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/vlHR_NcGlDs) [arXiv](https://arxiv.org/abs/2510.27680) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39104.png" alt="PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting poster" width="420">
  - Authors: Danyal Maqbool, Changhee Lee, Zachary Huemann, Samuel D. Church, Matthew E. Larson, Scott B. Perlman, Tomas A. Romero, Joshua D. Warner, Meghan Lubner, Xin Tie, ... (+4 more)
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41054) **PGDM: Physics-Guided Noise-Free Diffusion Model Based on Point Spread Function for Light-Scattering Removal in Unpaired Biomedical Images**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38185) **PGR-Net: Prior-Guided ROI Reasoning Network for Brain Tumor MRI Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_PGR-Net_Prior-Guided_ROI_Reasoning_Network_for_Brain_Tumor_MRI_Segmentation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.21626) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38185.png" alt="PGR-Net: Prior-Guided ROI Reasoning Network for Brain Tumor MRI Segmentation poster" width="420">
  - Authors: Jiacheng Lu, Hui Ding, Shiyu Zhang, Guoping Huo
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `MRI / MR`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36623) **Phrase-grounded APO for Improving Chest X-ray Report Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Mahmood_Phrase-grounded_APO_for_Improving_Chest_X-ray_Report_Generation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/uDIE70Ei-vk) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Raziuddin Mahmood, Tanveer Syeda-Mahmood
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41029) **PhySe-RPO: Physics and Semantics Guided Relative Policy Optimization for Diffusion-Based Surgical Smoke Removal**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Surgery / Medical Video`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41048) **PLCReg: Correlation-Aware Polar-Linear Attention for Guiding Medical Image Registration**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Registration`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39370) **PMRNet: Physics-informed Multi-scale Refinement Network for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_PMRNet_Physics-informed_Multi-scale_Refinement_Network_for_Medical_Image_Segmentation_CVPR_2026_paper.html) [GitHub](https://github.com/KangBoce/PMRNet) [Video](https://www.youtube-nocookie.com/embed/oTDjNM_rgaQ) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/39370.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39370.png" alt="PMRNet: Physics-informed Multi-scale Refinement Network for Medical Image Segmentation poster" width="420">
  - Authors: Boce Kang
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Segmentation`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37228) **Prospective Dynamic 3D MRI Reconstruction via Latent-Space Motion Tracking from Single Measurement**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Prospective_Dynamic_3D_MRI_Reconstruction_via_Latent-Space_Motion_Tracking_from_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37228.png" alt="Prospective Dynamic 3D MRI Reconstruction via Latent-Space Motion Tracking from Single Measurement poster" width="420">
  - Authors: Lixuan Chen, Zhongnan Liu, Jesse Hamilton, James M. Balter, Jeong Joon Park, Liyue Shen
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Restoration / Reconstruction`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41016) **PTF-CT: Polar-Aware Temporal-Frequential Iterative Reconstruction for Sparse-View CT**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38409) **R^2-Seg: Training-Free OOD Medical Tumor Segmentation via Anatomical Reasoning and Statistical Rejection**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_R2-Seg_Training-Free_OOD_Medical_Tumor_Segmentation_via_Anatomical_Reasoning_and_CVPR_2026_paper.html) [Project](https://eurekashen.github.io/R2Seg/) [Video](https://www.youtube-nocookie.com/embed/rCS9Szgzdfk) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38409.png" alt="R^2-Seg: Training-Free OOD Medical Tumor Segmentation via Anatomical Reasoning and Statistical Rejection poster" width="420">
  - Authors: Shuaike Shen, Ke Liu, Jiaqing Xie, Shangde Gao, Chunhua Shen, Ge Liu, Mireia Crispin-Ortuzar, Shangqi Gao
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break | Oral Session 4D: Visual Segmentation
  - Tags: `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41022) **ReCliFF: Adaptive Orthogonal Decoupling for Federated Fine-tuning of Medical MLLMs**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41062) **RelativeFlow: Taming Medical Image Denoising Learning with Noisy Reference**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38820) **Rethinking Box Supervision: Bias-Free Weakly Supervised Medical Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_Rethinking_Box_Supervision_Bias-Free_Weakly_Supervised_Medical_Segmentation_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38820.png" alt="Rethinking Box Supervision: Bias-Free Weakly Supervised Medical Segmentation poster" width="420">
  - Authors: Jun Wei, Hui Huang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41058) **Rethinking Medical High-Modality Learning Under Missingness — A Long-Tailed Distribution Perspective**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41013) **Rethinking Whole-Body CT Image Interpretation: An Abnormality-Centric Approach**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36808) **Revisiting 2D Foundation Models for Scalable 3D Medical Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Revisiting_2D_Foundation_Models_for_Scalable_3D_Medical_Image_Classification_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2512.12887) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36808.png" alt="Revisiting 2D Foundation Models for Scalable 3D Medical Image Classification poster" width="420">
  - Authors: Han Liu, Bogdan Georgescu, Yanbo Zhang, Youngjin Yoo, Michael Baumgartner, Riqiang Gao, Jianing Wang, Gengyan Zhao, Eli Gibson, Dorin Comaniciu, ... (+1 more)
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Foundation / Adaptation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39405) **RNED: Rotary Number Encoding and Decoding for Quantitative Medical VLM Analysis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_RNED_Rotary_Number_Encoding_and_Decoding_for_Medical_VLMs_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Fengbei Liu, Sunwoo Kwak, Nusrat Binta Nizam, Ilan Richter, Ashley Beecy, Jayant Raikhelkar, Deborah Estrin, Mert Sabuncu
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Cancer / Tumor / Lesion`, `Medical VLM / VQA / Reasoning`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41072) **R²MoE: Representation and Expert Selection Dual-Regularized Mixture-of-Experts for Multimodal Clinical Data**
  - Session: Findings Poster Session 2
  - Tags: `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37552) **SAT-RRG: LLM-Guided Self-Adaptive Training for Radiology Report Generation with Token-Level Push–Pull Optimization**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_SAT-RRG_LLM-Guided_Self-Adaptive_Training_for_Radiology_Report_Generation_with_Token-Level_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/PJdtoAPCO64) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37552-thumb.png" alt="SAT-RRG: LLM-Guided Self-Adaptive Training for Radiology Report Generation with Token-Level Push–Pull Optimization poster" width="420">
  - Authors: YUNYI LIU, Yingshu Li, Tong Chen, Lingqiao Liu, Lei Wang, Luping Zhou
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36984) **Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Claessens_Scaling_Self-Supervised_and_Cross-Modal_Pretraining_for_Volumetric_CT_Transformers_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/tFdLkc0v998) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36984.png" alt="Scaling Self-Supervised and Cross-Modal Pretraining for Volumetric CT Transformers poster" width="420">
  - Authors: Cris Claessens, Christiaan Viviers, Giacomo D&amp;#x27;Amicantonio, Egor Bondarev, Fons van der Sommen
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36238) **SD-FSMIS: Adapting Stable Diffusion for Few-Shot Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SD-FSMIS_Adapting_Stable_Diffusion_for_Few-Shot_Medical_Image_Segmentation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.03134) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36238.png" alt="SD-FSMIS: Adapting Stable Diffusion for Few-Shot Medical Image Segmentation poster" width="420">
  - Authors: Meihua Li, Yang Zhang, Weizhao He, Hu Qu, Yisong Li
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Medical AI / General`, `Segmentation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36392) **SegMoTE: Token-Level Mixture of Experts for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_SegMoTE_Token-Level_Mixture_of_Experts_for_Medical_Image_Segmentation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2602.19213) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36392.png" alt="SegMoTE: Token-Level Mixture of Experts for Medical Image Segmentation poster" width="420">
  - Authors: Yujie Lu, Jingwen Li, Sibo Ju, Yanzhou Su, He Yao, Yisong Liu, Min Zhu, Junlong Cheng
  - Session: Poster Session 6 | Oral Session 6C: Medical Vision
  - Tags: `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37844) **Semi-supervised Echocardiography Video Segmentation via Anchor Semantic Awareness and Continuous Pseudo-label Reforging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Fang_Semi-supervised_Echocardiography_Video_Segmentation_via_Anchor_Semantic_Awareness_and_Continuous_CVPR_2026_paper.html) [GitHub](https://github.com/YunPeng-Fang/EchoForge) [Video](https://www.youtube-nocookie.com/embed/W6KlsEieXXc) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37844.png" alt="Semi-supervised Echocardiography Video Segmentation via Anchor Semantic Awareness and Continuous Pseudo-label Reforging poster" width="420">
  - Authors: Yunpeng Fang, Yimu Sun, Jingxing Guo, Huisi Wu, Jing Qin
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Ultrasound / Sonography`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36490) **SemiGDA: Generative Dual-distribution Alignment for Semi-Supervised Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_SemiGDA_Generative_Dual-distribution_Alignment_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.23274) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: kaiwen Huang, Yi Zhou, Yizhe Zhang, Jingxiong Li, Tao Zhou
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Medical AI / General`, `Segmentation`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39890) **SHands: A Multi-View Dataset and Benchmark for Surgical Hand-Gesture and Error Recognition Toward Medical Training**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_SHands_A_Multi-View_Dataset_and_Benchmark_for_Surgical_Hand-Gesture_and_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/AS6p-tpArRw) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39890.png" alt="SHands: A Multi-View Dataset and Benchmark for Surgical Hand-Gesture and Error Recognition Toward Medical Training poster" width="420">
  - Authors: Le Ma, Thiago Freitas dos Santos, Nadia Magnenat-Thalmann, Katarzyna Wac
  - Session: Poster Session 6
  - Tags: `Surgery / Medical Video`, `Medical AI / General`, `Detection / Diagnosis`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36495) **SHAPE: Structure-aware Hierarchical Unsupervised Domain Adaptation with Plausibility Evaluation for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_SHAPE_Structure-aware_Hierarchical_Unsupervised_Domain_Adaptation_with_Plausibility_Evaluation_for_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/4Y3OLaeNn0Y) [arXiv](https://arxiv.org/abs/2603.21904) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36495.png" alt="SHAPE: Structure-aware Hierarchical Unsupervised Domain Adaptation with Plausibility Evaluation for Medical Image Segmentation poster" width="420">
  - Authors: Linkuan Zhou, Yinghao Xia, Yufei Shen, Xiangyu Li, Wenjie Du, Cong Cong, leyi wei, Ran Su, Qiangguo Jin
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39472) **Similarity-as-Evidence: Calibrating Overconfident VLMs for Interpretable and Label-Efficient Medical Active Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_Similarity-as-Evidence_Calibrating_Overconfident_VLMs_for_Interpretable_and_Label-Efficient_Medical_Active_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/SGuLA9Qa1uI) [arXiv](https://arxiv.org/abs/2602.18867) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39472.png" alt="Similarity-as-Evidence: Calibrating Overconfident VLMs for Interpretable and Label-Efficient Medical Active Learning poster" width="420">
  - Authors: Zhuofan Xie, Zishan Lin, Jinliang Lin, Jie Qi, Shaohua Hong, Shuo Li
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39154) **Simple Agents Outperform Experts in Biomedical Imaging Workflow Optimization**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Simple_Agents_Outperform_Experts_in_Biomedical_Imaging_Workflow_Optimization_CVPR_2026_paper.html) [Project](https://xuefei-wang.github.io/simple-agent-opt/) [Video](https://www.youtube-nocookie.com/embed/1Q7TvvpnRw4) [arXiv](https://arxiv.org/abs/2512.06006) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/39154.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  - Authors: Xuefei Wang, Kai A. Horstmann, Ethan Lin, Jonathan Chen, Alexander Farhang, Sophia Stiles, Atharva Sehgal, Jonathan Light, David Valen, Yisong Yue, ... (+1 more)
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37453) **Simple-ViLMedSAM: Simple Text Prompts Meet Vision-Language Models for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_Simple-ViLMedSAM_Simple_Text_Prompts_Meet_Vision-Language_Models_for_Medical_Image_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37453.png" alt="Simple-ViLMedSAM: Simple Text Prompts Meet Vision-Language Models for Medical Image Segmentation poster" width="420">
  - Authors: Chengcan Qian, Dong Nie, Geng Chen, Daoqiang Zhang, Xuyun Wen
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36477) **Sketch2CT: Multimodal Diffusion for Structure-Aware 3D Medical Volume Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/An_Sketch2CT_Multimodal_Diffusion_for_Structure-Aware_3D_Medical_Volume_Generation_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/RiNNzMcykok) [arXiv](https://arxiv.org/abs/2603.22509) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36477.png" alt="Sketch2CT: Multimodal Diffusion for Structure-Aware 3D Medical Volume Generation poster" width="420">
  - Authors: Delin An, Chaoli Wang
  - Session: Poster Session 6
  - Tags: `CT / Tomography`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Segmentation`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37545) **SOTA: Self-adaptive Optimal Transport for Zero-Shot Classification with Multiple Foundation Models**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_SOTA_Self-adaptive_Optimal_Transport_for_Zero-Shot_Classification_with_Multiple_Foundation_CVPR_2026_paper.html) [GitHub](https://github.com/Afleve/self-adaptive-Optimal-Transport) [arXiv](https://arxiv.org/abs/2506.13723) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37545.png" alt="SOTA: Self-adaptive Optimal Transport for Zero-Shot Classification with Multiple Foundation Models poster" width="420">
  - Authors: Zhanxuan Hu, Qiyu Xu, Yu Duan, Yonghang Tai, Huafeng Li
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38642) **Sparse Spectral LoRA: Routed Experts for Medical VLMs**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Nejatimanzari_Sparse_Spectral_LoRA_Routed_Experts_for_Medical_VLMs_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/Ohj06KwiGRs) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38642.png" alt="Sparse Spectral LoRA: Routed Experts for Medical VLMs poster" width="420">
  - Authors: Omid Nejatimanzari, Hojat Asgariandehkordi, Taha Koleilat, Yiming Xiao, Hassan Rivaz
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36727) **Sparse Task Vector Mixup with Hypernetworks for Efficient Knowledge Transfer in Whole-Slide Image Prognosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Sparse_Task_Vector_Mixup_with_Hypernetworks_for_Efficient_Knowledge_Transfer_CVPR_2026_paper.html) [GitHub](https://github.com/liupei101/STEPH) [arXiv](https://arxiv.org/abs/2603.10526) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/36727.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36727.png" alt="Sparse Task Vector Mixup with Hypernetworks for Efficient Knowledge Transfer in Whole-Slide Image Prognosis poster" width="420">
  - Authors: Pei Liu, xiangxiang Zeng, Tengfei Ma, Yucheng Xing, Xuanbai Ren, Yiping Liu
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39564) **Spatial-SAM: Spatially Consistent 3D Electron Microscopy Segmentation with SDF Memory and Semi-Supervised Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_Spatial-SAM_Spatially_Consistent_3D_Electron_Microscopy_Segmentation_with_SDF_Memory_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/nzZlJfRjT-w) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39564.png" alt="Spatial-SAM: Spatially Consistent 3D Electron Microscopy Segmentation with SDF Memory and Semi-Supervised Learning poster" width="420">
  - Authors: Yikai Huang, Renmin Han, Yuxuan Wang, Youcheng Cai, Ligang Liu
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37682) **SPEGC: Continual Test-Time Adaptation via Semantic-Prompt-Enhanced Graph Clustering for Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Du_SPEGC_Continual_Test-Time_Adaptation_via_Semantic-Prompt-Enhanced_Graph_Clustering_for_Medical_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/taDONXqeLrY) [arXiv](https://arxiv.org/abs/2603.11492) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37682.png" alt="SPEGC: Continual Test-Time Adaptation via Semantic-Prompt-Enhanced Graph Clustering for Medical Image Segmentation poster" width="420">
  - Authors: Xiaogang Du, Jiawei Zhang, Tongfei Liu, Tao Lei, Yingbo Wang
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/40714) **Step-CoT: Stepwise Visual Chain-of-Thought for Medical Visual Question Answering**
  - Session: Findings Poster Session 1
  - Tags: `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36343) **SurgCoT: Advancing Spatiotemporal Reasoning in Surgical Videos through a Chain-of-Thought Benchmark**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_SurgCoT_Advancing_Spatiotemporal_Reasoning_in_Surgical_Videos_through_a_Chain-of-Thought_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/4KwhSQ2W0JI) [arXiv](https://arxiv.org/abs/2604.20319) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36343.png" alt="SurgCoT: Advancing Spatiotemporal Reasoning in Surgical Videos through a Chain-of-Thought Benchmark poster" width="420">
  - Authors: Gui Wang, YongSong Zhou, Kaijun Deng, Wooi Ping Cheah, Rong Qu, Jianfeng Ren, Linlin Shen
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Surgery / Medical Video`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41026) **Surgical Procedural Planning as 3D World Modelling: Towards Automated Pulmonary Resection**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Surgery / Medical Video`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37435) **TANGO: Learning Distribution-wise Foundation Prior Consistency and Instance-wise Style Calibration for Medical Image Generalization**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_TANGO_Learning_Distribution-wise_Foundation_Prior_Consistency_and_Instance-wise_Style_Calibration_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/qkLMYq942Ic) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/37435.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37435.png" alt="TANGO: Learning Distribution-wise Foundation Prior Consistency and Instance-wise Style Calibration for Medical Image Generalization poster" width="420">
  - Authors: Chuang Liu, Yichao Cao, Xiu Su, Haogang Zhu
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Medical AI / General`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36865) **Tell2Adapt: A Unified Framework for Source Free Unsupervised Domain Adaptation via Vision Foundation Model**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Tell2Adapt_A_Unified_Framework_for_Source_Free_Unsupervised_Domain_Adaptation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2603.05012) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36865.png" alt="Tell2Adapt: A Unified Framework for Source Free Unsupervised Domain Adaptation via Vision Foundation Model poster" width="420">
  - Authors: Yulong Shi, Shijie Li, Ziyi Li, Lin Qi
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Endoscopy / Colonoscopy / Polyp`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Foundation / Adaptation`, `Generative / Diffusion`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/39575) **Temporal Inversion for Learning Interval Change in Chest X-Rays**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ko_Temporal_Inversion_for_Learning_Interval_Change_in_Chest_X-Rays_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/hbrnlS8hkWU) [arXiv](https://arxiv.org/abs/2604.04563) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/39575.png" alt="Temporal Inversion for Learning Interval Change in Chest X-Rays poster" width="420">
  - Authors: Hanbin Ko, Kyungmin Jeon, Doowoong Choi, Chang Min Park
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `X-Ray / Radiography`, `Medical AI / General`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41039) **TICON: A Slide-Level Tile Contextualizer for Histopathology Representation Learning**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38759) **TIM: Temporal Decoupling with Iterative Mutual-Refinement Model for Longitudinal Radiology Report Generation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_TIM_Temporal_Decoupling_with_Iterative_Mutual-Refinement_Model_for_Longitudinal_Radiology_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38759.png" alt="TIM: Temporal Decoupling with Iterative Mutual-Refinement Model for Longitudinal Radiology Report Generation poster" width="420">
  - Authors: Yiheng Dong, Yi Lin, Shilong Huang, Xiyan Yang, Xin Yang
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Detection / Diagnosis`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36819) **TopoCL: Topological Contrastive Learning for Medical Imaging**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_TopoCL_Topological_Contrastive_Learning_for_Medical_Imaging_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/MSb4NjZjLQQ) [arXiv](https://arxiv.org/abs/2603.14647) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36819-thumb.png" alt="TopoCL: Topological Contrastive Learning for Medical Imaging poster" width="420">
  - Authors: Guangyu Meng, Pengfei Gu, Peixian Liang, John P. Lalor, Erin Wolf Chambers, Danny Z. Chen
  - Session: Poster Session 6
  - Tags: `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37998) **TopoSlide: Topologically-Informed Histopathology Whole Slide Image Representation Learning**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Abousamra_TopoSlide_Topologically-Informed_Histopathology_Whole_Slide_Image_Representation_Learning_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/mHcOtbHK-Xc) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37998.png" alt="TopoSlide: Topologically-Informed Histopathology Whole Slide Image Representation Learning poster" width="420">
  - Authors: Shahira Abousamra, Asmita Sood, Sylvia Plevritis
  - Session: Poster Session 2 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38223) **Towards Efficient Medical Reasoning with Minimal Fine-Tuning Data**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhuang_Towards_Efficient_Medical_Reasoning_with_Minimal_Fine-Tuning_Data_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2508.01450) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38223.png" alt="Towards Efficient Medical Reasoning with Minimal Fine-Tuning Data poster" width="420">
  - Authors: Xinlin Zhuang, feilong tang, Haolin Yang, Xiwei Liu, Ming Hu, Huifa Li, Haochen Xue, Junjun He, Zongyuan Ge, Yichen Li, ... (+2 more)
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Medical AI / General`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41018) **Towards Noise-Robust Medical Segmentation via Chebyshev-Attention-Based Asymmetric UNet**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41040) **TP-Seg: Task-Prototype Framework for Unified Medical Lesion Segmentation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37583) **Turning Pre-Trained Vision Transformers into End-to-End Histopathology Whole Slide Image Models for Survival Prediction**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Turning_Pre-Trained_Vision_Transformers_into_End-to-End_Histopathology_Whole_Slide_Image_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37583.png" alt="Turning Pre-Trained Vision Transformers into End-to-End Histopathology Whole Slide Image Models for Survival Prediction poster" width="420">
  - Authors: Jiawen Li, Jiali Hu, Xitong Ling, Renao Yan, Yuxuan Chen, Tian Guan, Yonghong He
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41019) **Two-Stage 3D Pulmonary Vessel Reconstruction via Trunk--Expansion Coupled Point Cloud Generation**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Restoration / Reconstruction`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38535) **Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_Ultrasound-CLIP_Semantic-Aware_Contrastive_Pre-training_for_Ultrasound_Image-Text_Understanding_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/p5AF42K_oz4) [arXiv](https://arxiv.org/abs/2604.01749) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38535.png" alt="Ultrasound-CLIP: Semantic-Aware Contrastive Pre-training for Ultrasound Image-Text Understanding poster" width="420">
  - Authors: Jiayun Jin, Haolong Chai, Xueying Huang, Xiaoqing Guo, Zengwei Zheng, Zhan Zhou, Junmei Wang, Xinyu Wang, Jie Liu, Binbin Zhou
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `Ultrasound / Sonography`, `MRI / MR`, `CT / Tomography`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36954) **Uni-Encoder Meets Multi-Encoders: Representation Before Fusion for Brain Tumor Segmentation with Missing Modalities**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Song_Uni-Encoder_Meets_Multi-Encoders_Representation_Before_Fusion_for_Brain_Tumor_Segmentation_CVPR_2026_paper.html) [arXiv](https://arxiv.org/abs/2604.22177) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36954.png" alt="Uni-Encoder Meets Multi-Encoders: Representation Before Fusion for Brain Tumor Segmentation with Missing Modalities poster" width="420">
  - Authors: Peibo Song, Xiaotian Xue, Jinshuo Zhang, zihao wang, Jinhua liu, Shujun Fu, Fangxun Bao, Si Yong Yeo
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Organs / Anatomy`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38290) **Universal-to-Specific: Dynamic Knowledge-Guided Multiple Instance Learning for Few-Shot Whole Slide Image Classification**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Universal-to-Specific_Dynamic_Knowledge-Guided_Multiple_Instance_Learning_for_Few-Shot_Whole_Slide_CVPR_2026_paper.html) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38290.png" alt="Universal-to-Specific: Dynamic Knowledge-Guided Multiple Instance Learning for Few-Shot Whole Slide Image Classification poster" width="420">
  - Authors: Junjian Li, Hulin Kuang, Jin Liu, Hailin Yue, Mengshen He, Jianxin Wang
  - Session: Poster Session 4 & Exhibit Hall w/ Coffee Break
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Cancer / Tumor / Lesion`, `Detection / Diagnosis`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38244) **URICA: A Uniformity Region Affine Identifier Capture Algorithm for Arbitrary Region Retrieval in Pathology Images**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Su_URICA_A_Uniformity_Region_Affine_Identifier_Capture_Algorithm_for_Arbitrary_CVPR_2026_paper.html) [Project](https://mcaloma.github.io/URICA_page/) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38244.png" alt="URICA: A Uniformity Region Affine Identifier Capture Algorithm for Arbitrary Region Retrieval in Pathology Images poster" width="420">
  - Authors: Ri Su, Zhao CHEN, Caleb Chen Cao, Lei Chen
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38695) **VesMamba: 3D Pulmonary Vessel Segmentation from CT images via Mamba with Structural Perception and Scale-aware Filtering**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_VesMamba_3D_Pulmonary_Vessel_Segmentation_from_CT_images_via_Mamba_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/vtGF79QAQyM) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38695.png" alt="VesMamba: 3D Pulmonary Vessel Segmentation from CT images via Mamba with Structural Perception and Scale-aware Filtering poster" width="420">
  - Authors: Zhipeng Liu, Guilian Chen, Zheng Jiang, Huisi Wu, Jing Qin
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `CT / Tomography`, `Medical AI / General`, `Segmentation`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38473) **Virtual Full-stack Scanning of Brain MRI via Imputing Any Quantised Code**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Virtual_Full-stack_Scanning_of_Brain_MRI_via_Imputing_Any_Quantised_CVPR_2026_paper.html) [GitHub](https://github.com/ycwu1997/CodeBrain) [Video](https://www.youtube-nocookie.com/embed/oHKOVApCouk) [arXiv](https://arxiv.org/abs/2501.18328) [Slides](https://cvpr.thecvf.com/media/cvpr-2026/Slides/38473_Bv2IkSb.pdf) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38473.png" alt="Virtual Full-stack Scanning of Brain MRI via Imputing Any Quantised Code poster" width="420">
  - Authors: Yicheng Wu, Tao Song, Zhonghua Wu, Jin Ye, Zongyuan Ge, Wenjia Bai, Zhaolin Chen, Jianfei Cai
  - Session: Poster Session 3 & Exhibit Hall
  - Tags: `MRI / MR`, `Medical AI / General`, `Organs / Anatomy`, `Restoration / Reconstruction`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41053) **Vision-Language Models Encode Clinical Guidelines for Concept-Based Medical Reasoning**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41024) **Vision-Language Models for Automated 3D PET/CT Report Generation**
  - Session: Findings Poster Session 2
  - Tags: `CT / Tomography`, `PET / Nuclear Medicine`, `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`, `Generative / Diffusion`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41023) **Volumetrically Consistent Implicit Atlas Learning via Neural Diffeomorphic Flow for Placenta MRI**
  - Session: Findings Poster Session 2
  - Tags: `MRI / MR`, `Pathology / Microscopy / Cells`, `Medical AI / General`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/37454) **VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Rokuss_VoxTell_Free-Text_Promptable_Universal_3D_Medical_Image_Segmentation_CVPR_2026_paper.html) [GitHub](https://github.com/MIC-DKFZ/VoxTell) [Video](https://www.youtube-nocookie.com/embed/enF-YrdY-mI) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/37454.png" alt="VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation poster" width="420">
  - Authors: Maximilian Rokuss, Moritz Langenberg, Yannick Kirchhoff, Fabian Isensee, Benjamin Hamm, Constantin Ulrich, Sebastian Regnery, Lukas Bauer, Efthimios Katsigiannopulos, Tobias Norajitra, ... (+1 more)
  - Session: Poster Session 6
  - Tags: `MRI / MR`, `CT / Tomography`, `PET / Nuclear Medicine`, `3D / Volumetric Medical Imaging`, `Medical AI / General`, `Organs / Anatomy`, `Segmentation`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41268) **Wake the Sleeping Weights: Sparsely-Activated Continual Test-Time Adaptation for Medical Image Segmentation**
  - Session: Findings Poster Session 3
  - Tags: `Medical AI / General`, `Segmentation`, `Foundation / Adaptation`, `Federated / Continual / Generalization`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/41050) **When Models Learn to Ask Why: Adaptive Causal Reasoning for Trustworthy Medical Vision–Language Models**
  - Session: Findings Poster Session 2
  - Tags: `Pathology / Microscopy / Cells`, `Medical AI / General`, `Medical VLM / VQA / Reasoning`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/38227) **X-PCR: A Benchmark for Cross-modality Progressive Clinical Reasoning in Ophthalmic Diagnosis**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_X-PCR_A_Benchmark_for_Cross-modality_Progressive_Clinical_Reasoning_in_Ophthalmic_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/1g_Y7gnAYtU) [arXiv](https://arxiv.org/abs/2604.20350) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/38227.png" alt="X-PCR: A Benchmark for Cross-modality Progressive Clinical Reasoning in Ophthalmic Diagnosis poster" width="420">
  - Authors: Gui Wang, Zehao Zhong, YongSong Zhou, Yudong Li, Ende Wu, Wooi Ping Cheah, Rong Qu, Jianfeng Ren, Linlin Shen
  - Session: Poster Session 5 & Exhibit Hall
  - Tags: `OCT / Ophthalmology / Retina`, `Medical AI / General`, `Detection / Diagnosis`
- [CVPR](https://cvpr.thecvf.com/virtual/2026/poster/36840) **X-WIN: Building Chest Radiograph World Model via Predictive Sensing**
  - [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_X-WIN_Building_Chest_Radiograph_World_Model_via_Predictive_Sensing_CVPR_2026_paper.html) [Video](https://www.youtube-nocookie.com/embed/ZzPPjRx9hDI) [arXiv](https://arxiv.org/abs/2511.14918) [Source](https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference)
  <img src="https://cvpr.thecvf.com/media/PosterPDFs/CVPR%202026/36840.png" alt="X-WIN: Building Chest Radiograph World Model via Predictive Sensing poster" width="420">
  - Authors: Zefan Yang, Ge Wang, James Hendler, Mannudeep K. Kalra, Pingkun Yan
  - Session: Poster Session 1 & Exhibit Hall
  - Tags: `X-Ray / Radiography`, `CT / Tomography`, `Medical AI / General`, `Organs / Anatomy`, `Detection / Diagnosis`, `Foundation / Adaptation`
