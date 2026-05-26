+++
date = "2024-04-20T00:00:00+08:00"
draft = false
title = """MIKE：构建系统发育树的超快、无组装和无干扰方法"""
tags = ["软件", "知识", "转载", "待完善", "生物信息学"]
+++

| 软件名称 | 简介 | 教程 | 平台(PC) | tags |
| -------- | ---- | ---- | -------- | ---- |
| MIKE      | 构建系统发育树的超快、无组装和无干扰方法 | #47  | 跨平台   | ![GitHub top language](https://img.shields.io/github/languages/top/Argonum-Clever2/mike) ![GitHub last commit](https://img.shields.io/github/last-commit/Argonum-Clever2/mike) ![GitHub issues](https://img.shields.io/github/issues/Argonum-Clever2/mike) ![GitHub stars](https://img.shields.io/github/stars/Argonum-Clever2/mike?style=flat) ![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Argonum-Clever2/mike) ![GitHub contributors](https://img.shields.io/github/contributors/Argonum-Clever2/mike) ![GitHub Created At](https://img.shields.io/github/created-at/Argonum-Clever2/mike) ![GitHub forks](https://img.shields.io/github/forks/Argonum-Clever2/mike?style=flat) ![GitHub pull requests](https://img.shields.io/github/issues-pr/Argonum-Clever2/mike) ![GitHub license](https://img.shields.io/github/license/Argonum-Clever2/mike) ![GitHub release](https://img.shields.io/github/v/release/Argonum-Clever2/mike) ![GitHub language count](https://img.shields.io/github/languages/count/Argonum-Clever2/mike) |

```bibtex
@article{10.1093/bioinformatics/btae154,
    author = {Wang, Fang and Wang, Yibin and Zeng, Xiaofei and Zhang, Shengcheng and Yu, Jiaxin and Li, Dongxi and Zhang, Xingtan},
    title = "{MIKE: an ultrafast, assembly-, and alignment-free approach for phylogenetic tree construction}",
    journal = {Bioinformatics},
    volume = {40},
    number = {4},
    pages = {btae154},
    year = {2024},
    month = {03},
    abstract = "{Constructing a phylogenetic tree requires calculating the evolutionary distance between samples or species via large-scale resequencing data, a process that is both time-consuming and computationally demanding. Striking the right balance between accuracy and efficiency is a significant challenge.To address this, we introduce a new algorithm, MIKE (MinHash-based k-mer algorithm). This algorithm is designed for the swift calculation of the Jaccard coefficient directly from raw sequencing reads and enables the construction of phylogenetic trees based on the resultant Jaccard coefficient. Simulation results highlight the superior speed of MIKE compared to existing state-of-the-art methods. We used MIKE to reconstruct a phylogenetic tree, incorporating 238 yeast, 303 Zea, 141 Ficus, 67 Oryza, and 43 Saccharum spontaneum samples. MIKE demonstrated accurate performance across varying evolutionary scales, reproductive modes, and ploidy levels, proving itself as a powerful tool for phylogenetic tree construction.MIKE is publicly available on Github at https://github.com/Argonum-Clever2/mike.git.}",
    issn = {1367-4811},
    doi = {10.1093/bioinformatics/btae154},
    url = {https://doi.org/10.1093/bioinformatics/btae154},
    eprint = {https://academic.oup.com/bioinformatics/article-pdf/40/4/btae154/57149237/btae154.pdf},
}
```



```math
J\left( {S_{1},\, S_{2}} \right) = \frac{\left| S_{1} \cap S_{2} \right|}{\left. \left| S \right._{1} \cup S_{2} \right|}
```


- [MIKE: an ultrafast, assembly-, and alignment-free approach for phylogenetic tree construction | Bioinformatics | Oxford Academic](https://academic.oup.com/bioinformatics/article/40/4/btae154/7636962)
- [Mike试用-免组装、免比对，快速从fastq到nwk - 哔哩哔哩](https://www.bilibili.com/read/cv33571829/?spm_id_from=333.999.0.0)
- [Argonum-Clever2/mike](https://github.com/Argonum-Clever2/mike)
