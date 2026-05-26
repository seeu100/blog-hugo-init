+++
date = "2024-04-19T00:00:00+08:00"
draft = false
title = """ArchLinux 生物学软件"""
tags = ["Linux", "软件", "生物信息学"]
+++

Arch Linux 庞大的的AUR软件库对于装软件的人来说是一种福音。

利用`paru`、`yay`等AUR helper 可以直接安装。

## 目前ArchLinux官方库和AUR里有的软件

下面是对列出的生物信息学软件按照其主要作用分类和简要说明，并非严格意义上的排序，因为这些软件服务于不同的生物信息学任务，无法直接进行顺序排列：

1. **序列比对工具**
   - **MAFFT**：快速、灵活的多重序列比对工具，适合处理大规模的蛋白质或核酸序列集。
   - **ClustalW**：经典的多序列比对软件，常用于小到中规模序列的比对分析。
   - **muscle**：高效、准确的多序列比对程序，能够快速产生高质量的比对结果。

2. **序列修剪**
   - **Gblocks**：从DNA或蛋白质序列比对中移除对齐质量差的位置和高度变异区域。
   - **trimal**：
3. **进化模型选择**
   - **jModelTest** / **modeltest-ng** / **mrmodeltest**：用于选择最优的分子进化模型，对序列数据集的进化速率、替换类型等参数进行估计。

4. **系统发育重建与进化树构建**
   - **mrbayes**：基于贝叶斯方法进行系统发育推断，可以生成概率型系统发育树。
   - **mrbayes-mpi**：mrbayes的并行版本，用于加速大规模数据分析。
   - **iqtree** / **iqtree-mpi**：高性能的系统发育树构建程序，采用集成似然方法。
   - **raxml** / **raxml-ng**：快速的最大似然法系统发育树构建软件。
   - **paup***：广泛应用于系统发育、生物地理学和分子进化分析的软件包。
   - **phylip**：一套历史悠久的系统发育和分子进化分析软件集合。
   - **FastTree**：快速构建大规模进化树的程序，特别是对于超大数据集。
   - **phyml**：基于最大似然、贝叶斯和邻接法的系统发育树构建工具。
   - **BEAST** / **BEAST2**：贝叶斯进化分析套件，用于估算物种分化时间、种群动态参数等，并构建带时间尺度的系统发育树。
   - **paml (PAML)**: 全称“Phylogenetic Analysis by Maximum Likelihood”，基于最大似然法进行分子进化分析的软件包，特别用于研究基因或蛋白质序列的系统发育和自然选择压力。它包含多个模块，其中最著名的可能是codeml，该模块用来检测正选择（positive selection），通过比较不同基因模型下的似然率，计算ω值（非同义替代速率与同义替代速率的比值），从而推断蛋白质编码基因是否经历过适应性进化。
   - **pamlX**: PAML的图形用户界面版本。
   - **~~bali-phy~~**: 基于贝叶斯框架进行序列比对和系统发育分析的软件。它能同时估计序列比对和系统发育树，尤其擅长处理高噪声序列数据和具有插入删除事件的数据集。

5. **系统发育图形可视化**
   - **figtree**：绘制系统发育树的图形界面软件，易于阅读和修改。
   - **TreeViewX**：显示和打印系统发育树，提供了对系统发育树分支的排序功能，并且支持导出SVG矢量图像格式的树状图。

6. **数据分析与辅助工具**
   - **tracer**：贝叶斯分析结果后处理工具，主要用于检查MCMC模拟的收敛性和有效性。
   - **seqencematrix**：用于生成序列差异矩阵的工具。
   - **seaview**：交互式多序列比对和系统发育分析软件。
   - **MEGA**：分子进化遗传分析软件，可进行多种序列分析和系统发育工作。
   - **mesquite**：整合了多种演化分析方法的交互式软件包。

7. **其他特定用途软件**
   - **popart**：用于展示和分析种群遗传数据的软件。
   - **MorphoJ**：形态学数据分析工具，适用于形态学特征的系统发育分析。
   - **Open DELTA**：用于描述分类单元和分析形态数据的软件。
   - **QGIS**：地理信息系统软件，可用于生态学和地理分布相关的数据分析。
   - **RStudio**：集成开发环境，支持使用R语言进行广泛的统计分析，包括生物信息学分析。
   - **python**：编程语言，可通过各种第三方库（如biopython等）进行生物信息学数据处理和分析。



## AUR 包名和简介

可在AUR官网查询上游等信息：https://aur.archlinux.org

- aur/mafft 7.525-1 [+14 ~0.00] 
Multiple alignment program for amino acid or nucleotide sequences. 
https://doi.org/10.1093/molbev/mst010
- aur/mafft-extensions 7.525-1 [+14 ~0.00]
MAFFT extensions
- aur/mafft-mpi 7.525-1 [+14 ~0.00]
MAFFT MPI support
- aur/mafft-desktop 1.0-1 [+1 ~0.00]
Desktop File For MAFFT
- aur/clustal-omega 1.2.4-1 [+12 ~0.00]
Protein sequence alignment program
- aur/clustalw 2.1-4 [+4 ~0.00]
Clustal W multiple sequence alignment program, version 2.0
- aur/clustalx 2.1-6 [+3 ~0.00]
Multiple alignment of nucleic acid and protein sequences
- aur/muscle 5.1-1 [+11 ~0.00]
Multiple sequence comparison by log-expectation
- aur/r-airway 1.22.0-1 [+0 ~0.00]
RangedSummarizedExperiment for RNA-Seq in airway smooth muscle cells, by Himes et al PLoS 
One 2014
- aur/r-hsmmsinglecell 1.22.0-2 [+0 ~0.00]
Single-cell RNA-Seq for differentiating human skeletal muscle myoblasts (HSMM)
- aur/r-meat 1.14.0-1 [+0 ~0.00]
Muscle Epigenetic Age Test
- aur/r-muscle 3.44.0-1 [+0 ~0.00]
Multiple Sequence Alignment with MUSCLE
- aur/gblocks 0.91b-7 [+1 ~0.00]
A program written in ANSI C language that eliminates poorly aligned positions and divergent
regions of an alignment of DNA or protein sequences. 
https://doi.org/10.1093/oxfordjournals.molbev.a026334
- aur/phyml 1:3.3.20220408-1 [+6 ~0.00]
Builds phylogenies from DNA or protein sequences using a maximum likelihood approach
- aur/staden-io_lib 1.15.0-1 [+6 ~0.00]
DNA sequence assembly (Gap4) and editing and analysis tools (Spin)
- aur/tcoffee 13.46.0.919e8c6b-1 [+6 ~0.00]
An alignment tool for Protein, DNA and RNA sequences
- aur/escribe-suite-bin 2_SP55-1 [+5 ~0.00]
Evolv eScribe Suite - DNA Management Suite and Ecigstats - INTL Version
- aur/jellyfish 2.3.1-1 [+5 ~0.00]
A tool for fast, memory-efficient counting of k-mers in DNA
- aur/diamond 2.1.9-1 [+3 ~0.00]
High performance sequence aligner for protein and translated DNA searches with big sequence
data. https://doi.org/10.1038/s41592-021-01101-x
- aur/oxdna-cuda 3.6.0-1 [+1 ~0.19] [过时：2024-03-23]
DNA/RNA/etc simulator, with CUDA support and analysis tools.
- aur/phyml-mpi 1:3.3.20220408-1 [+1 ~0.00]
Builds phylogenies from DNA or protein sequences using a maximum likelihood approach, using
multiple processors
- aur/r-minfi 1.48.0-1 [+1 ~0.18]
Analyze Illumina Infinium DNA methylation arrays
- aur/sequencematrix 1.9-6 [+1 ~0.00]
Taxonomy-aware DNA sequence processing toolkit
- aur/speciesidentifier 1.9-6 [+1 ~0.00]
Taxonomy-aware DNA sequence processing toolkit
- aur/genbankexplorer 1.9-6 [+1 ~0.00]
Taxonomy-aware DNA sequence processing toolkit
- aur/infernal 1.1.5-1 [+1 ~0.00]
Search DNA sequence databases for RNA structure and sequence similarities using covariance
models (CMs)
- aur/jmodeltest 2.1.10r20160303-7 [+1 ~0.00]
Phylogenetic Model Averaging, more models, new heuristics and high-performance computing. 
https://doi.org/10.1093/molbev/msn083
- aur/raxmlgui 2.0.10-2 [+1 ~0.00]
A new user-friendly program integrating RAxML-NG and ModelTest-NG for cutting-edge 
phylogenetic analysis. https://doi.org/10.1111/2041-210X.13512
- aur/modeltest-gui 0.1.7-8 [+0 ~0.00]
A New and Scalable Tool for the Selection of DNA and Protein Evolutionary Models. 
https://doi.org/10.1093/molbev/msz189
- aur/modeltest-ng 0.1.7-6 [+0 ~0.00]
A New and Scalable Tool for the Selection of DNA and Protein Evolutionary Models. 
https://doi.org/10.1093/molbev/msz189
- aur/modeltest-ng-mpi 0.1.7-7 [+0 ~0.00]
A New and Scalable Tool for the Selection of DNA and Protein Evolutionary Models. 
https://doi.org/10.1093/molbev/msz189
- aur/mrmodeltest 2.4-1 [+0 ~0.00]
C program for selecting DNA substitution models using PAUP*
- aur/paml 4.10.7-1 [+0 ~0.00]
Phylogenetic analysis by maximum likelihood. https://doi.org/10.1093/molbev/msm088
- aur/pamlx 1.3.1-4 [+0 ~0.00]
A Graphical User Interface for PAML https://doi.org/10.1093/molbev/mst179
- aur/treeviewx 0.5.0-1 [+0 ~0.00]
Program to display phylogenetic trees
- aur/ugene 50.0-1 [+1 ~0.00]
A free open-source cross-platform bioinformatics software
- aur/menugenerator 1.1-1 [+5 ~0.00]
A simple menu generator for fluxbox openbox jwm that uses xdg-menu.
- aur/ugene-bin 49.1-1 [+4 ~0.00]
A free cross-platform genome analysis suite (binary release)
- aur/ugene-git 38.1.r485.g113d9908d0-1 [+2 ~0.00]
A free cross-platform genome analysis suite.
- aur/ugene-cuda 50.0-1 [+1 ~0.00]
A free open-source cross-platform bioinformatics software (with CUDA)
- aur/r-occugene 1.62.0-2 [+0 ~0.00]
Functions for Multinomial Occupancy Distribution
- aur/trimal 1.4.1-1 [+0 ~0.00]
A tool for automated alignment trimming in large-scale phylogenetic analyses
- aur/python-pytrimal 0.7.0-1 [+0 ~0.00]
Cython bindings and Python interface to trimAl, a tool for automated alignment trimming.


* MAFFT（序列比对）
* ClustalW（序列比对）
* muscle
* gblocks
* jmodeltest
* ~~modeltest~~
* modeltest-ng
* ~~mrmodeltest~~
* mrbayes（贝叶斯建树）
* mrbayes-mpi
* paup*
* raxml
* raxml-ng
* FastTree
* phyml
* BEAST
* BEAST2
* iqtree
* phylobayes
* phylobayes-mpi
* figtree
* ~~treeviewx~~
* tracer
* seqencematrix
* phylip
* ugene
* seaview
* MEGA
* mesquite
* ~~paml~~
* ~~pamlX~~
* ~~bali-phy~~
* phylonium
* popart
* MorphoJ
* Open DELTA
* QGIS
* RStudio
* python

