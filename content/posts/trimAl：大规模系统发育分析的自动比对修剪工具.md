+++
date = "2024-04-19T00:00:00+08:00"
draft = false
title = """trimAl：大规模系统发育分析的自动比对修剪工具"""
tags = ["软件", "生物信息学"]
+++

| 软件名称 | 简介 | 教程 | 平台(PC) | tags |
| -------- | ---- | ---- | -------- | ---- |
| trimAl    | 大规模系统发育分析的自动比对修剪工具     | #40  | 跨平台(AUR)   | ![GitHub top language](https://img.shields.io/github/languages/top/inab/trimal) ![GitHub last commit](https://img.shields.io/github/last-commit/inab/trimal) ![GitHub issues](https://img.shields.io/github/issues/inab/trimal) ![GitHub stars](https://img.shields.io/github/stars/inab/trimal?style=flat) ![GitHub commit activity](https://img.shields.io/github/commit-activity/t/inab/trimal) ![GitHub contributors](https://img.shields.io/github/contributors/inab/trimal) ![GitHub Created At](https://img.shields.io/github/created-at/inab/trimal) ![GitHub forks](https://img.shields.io/github/forks/inab/trimal?style=flat) ![GitHub pull requests](https://img.shields.io/github/issues-pr/inab/trimal) ![GitHub license](https://img.shields.io/github/license/inab/trimal) ![GitHub release](https://img.shields.io/github/v/release/inab/trimal) ![GitHub language count](https://img.shields.io/github/languages/count/inab/trimal)   |

- [trimAl — trimAl](https://trimal.readthedocs.io/en/latest/)
- [inab/trimal: A tool for automated alignment trimming in large-scale phylogenetic analyses. Development version: 2.0](https://github.com/inab/trimal)
- [AUR (en) - trimal](https://aur.archlinux.org/packages/trimal)：![AUR 最后修改](https://img.shields.io/aur/last-modified/trimal) ![AUR 版本](https://img.shields.io/aur/version/trimal) ![AUR 许可证](https://img.shields.io/aur/license/trimal) ![AUR 维护者](https://img.shields.io/aur/maintainer/trimal) ![AUR 投票](https://img.shields.io/aur/votes/trimal) ![AUR 依赖](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Faur.archlinux.org%2Frpc%2Fv5%2Finfo%2Ftrimal&query=%24..Depends&label=Depends) ![AUR 编译依赖](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Faur.archlinux.org%2Frpc%2Fv5%2Finfo%2Ftrimal&query=%24..MakeDepends&label=MakeDepends)

## 简介

trimAl，全称为“trimAl”（Trimming Alignment with Logical Constraints），是一款生物信息学软件，专门用于优化多序列比对（Multiple Sequence Alignments，MSA）。它通过智能化筛选和修剪的方法，移除MSA中的低质量区域，包括不可靠的对齐位置和高度变异的序列片段，从而提高系统发育分析和进化分析的质量和可靠性。

trimAl采用了一系列算法来识别和排除不理想的对齐区域，这些区域可能由于噪音信号（如随机匹配、插入删除事件引起的偏差等）而降低了对齐的整体质量。它提供了多种策略和参数，允许用户根据需求选择合适的修剪模式，例如自动模式（automated1、automated2、automated3）以及其他手动设定阈值的方式，来保留高度保守的序列区块。

通过trimAl处理后的多序列比对，可以减少潜在的误差来源，有利于后续的分子进化分析，例如构建更准确的系统发育树、计算进化距离和检测选择压力等。由于trimAl在优化对齐方面的高效性与实用性，它已成为生物学研究中常用的预处理工具，尤其是在处理核苷酸或氨基酸序列数据时不可或缺。

```
❯ paru trimal
1 aur/trimal 1.4.1-1 [+0 ~0.00]
    A tool for automated alignment trimming in large-scale phylogenetic analyses
2 aur/python-pytrimal 0.7.0-1 [+0 ~0.00]
    Cython bindings and Python interface to trimAl, a tool for automated alignment trimming.
```

## 使用方法

trimAl的使用方法通常涉及命令行界面，通过指定不同的参数来达到修剪多序列比对的目的。以下是一些基本的使用方法和命令参数解释：

### 基本使用格式
```bash
trimal -in input_alignment.fasta -out trimmed_alignment.fasta [options]
```

- `-in` 参数：指定待修剪的输入多序列比对文件，通常是FASTA格式。
- `-out` 参数：指定修剪后输出的新比对文件的名称。

### 主要参数选项

1. `-gt` 或 `--gappyout`: 移除所有包含超过指定百分比（例如 `-gt 0.5` 表示超过50%）-gap的列。
2. `-consistency`：根据一致性得分修剪对齐，保留一致性高于指定阈值的列。
3. `-strict`：严格模式，移除任何包含gap的列。
4. `- automated1`：自动模式1，trimAl内部设定的一套规则，用于去除不保守的序列区域。
5. `-threshold`：基于相似度阈值，移除低于指定相似度的列。
6. `-fasta`：输出格式为FASTA，默认情况下也是这样。
7. `-no-gaps`：去除所有包含gap的序列。
8. `-cluster`：基于距离进行分群，然后仅保留每一群中最保守的部分。
9. `-discard`：丢弃指定百分比最低相似度的序列。
10. `-trim`：根据指定的修剪模式进行操作，例如 `-trim gappyout`。

在使用trimAl时，用户可以根据自己的具体需求选择相应的参数组合，以期得到最适合进一步分析的优化比对结果。具体的参数含义和用法可以通过查阅trimAl的帮助文档或参考软件作者提供的指南获取详细信息。由于trimAl的参数众多，以上只是列举了一些常见参数，实际使用时可能还有更多高级选项和组合。


## 文献阅读
[trimAl: a tool for automated alignment trimming in large-scale phylogenetic analyses | Bioinformatics | Oxford Academic](https://academic.oup.com/bioinformatics/article/25/15/1972/213148?login=true)
[10.1093/bioinformatics/btp348](https://doi.org/10.1093/bioinformatics/btp348)

### 摘要

Multiple sequence alignments are central to many areas of bioinformatics. It has been shown that the removal of poorly aligned regions from an alignment increases the quality of subsequent analyses. Such an alignment trimming phase is complicated in large-scale phylogenetic analyses that deal with thousands of alignments. Here, we present trimAl, a tool for automated alignment trimming, which is especially suited for large-scale phylogenetic analyses. trimAl can consider several parameters, alone or in multiple combinations, for selecting the most reliable positions in the alignment. These include the proportion of sequences with a gap, the level of amino acid similarity and, if several alignments for the same set of sequences are provided, the level of consistency across different alignments. Moreover, trimAl can automatically select the parameters to be used in each specific alignment so that the signal-to-noise ratio is optimized.
多序列比对是生物信息学许多领域的核心。
已经表明，从比对中去除对齐不良的区域提高了后续分析的质量。
在处理数千个比对的大规模系统发育分析中，这样的比对修剪阶段是复杂的。
在这里，我们提出了trimAl，自动对齐修剪，这是特别适合于大规模的系统发育分析的工具。
trimAl可以单独或以多种组合考虑若干参数，用于选择比对中最可靠的位置。
这些包括具有缺口的序列的比例、氨基酸相似性的水平，以及如果提供了同一组序列的几个比对，则不同比对之间的一致性水平。
此外，trimAl可以自动选择在每个特定比对中使用的参数，从而优化信噪比。

可用性：trimAl是用C++编写的，可以移植到所有平台。trimAl可[免费下载](http://trimal.cgenomics.org)，并可通过[Phylemon网络服务器](http://phylemon2.bioinfo.cipf.es/)在线使用。补充材料可在 http://trimal.cgenomics.org/publications 上获得。

联系人：[tgabaldon@crg.es](mailto:tgabaldon@crg.es)

Multiple sequence alignments (MSA) are central to many areas of bioinformatics, including phylogenetics, homology modeling, database searches and motif finding. Recently, such MSA-based techniques have been incorporated in high-throughput pipelines such as genome annotation and phylogenomics analyses. In all these applications, the reliability and accuracy of the analyses depend critically on the quality of the underlying alignments. A plethora of computer programs and algorithms for MSA are currently available (Notredame, [2007](javascript:;)), which implement different heuristics to find mathematically optimal solutions to the MSA problem. Accuracies of 80–90% have been reported for the best algorithms, but even the best scoring alignment algorithms may fail with certain protein families or at specific regions in the alignment. The situation worsens in large-scale analyses, where faster but less reliable algorithms and large numbers of automatically selected sequences are used. It is therefore generally assumed that trimming the alignment, so that poorly aligned regions are eliminated, increases the accuracy of the resulting MSA-based applications (Talavera and Castresana, [2007](javascript:;)). Some programs such as G-blocks (Castresana, [2000](javascript:;)) have been developed to assist in the MSA trimming phase by selecting blocks of conserved regions. They have become very popular and are extensively used, with good performance, in small-to-medium scale datasets, where several parameters can be tested manually (Talavera and Castresana, [2007](javascript:;)). However, their use over larger datasets is hampered by the need for defining, prior to the analysis, the set of parameters that will be used for all sequence families. Here, we present trimAl, a tool for automated alignment trimming. Its speed and the possibility for automatically adjusting the parameters to improve the phylogenetic signal-to-noise ratio, makes trimAl especially suited for large-scale phylogenomic analyses, involving thousands of large alignments.
多序列比对（MSA）是生物信息学许多领域的核心，包括遗传学、同源建模、数据库搜索和基序发现。最近，这种基于MSA的技术已被纳入高通量管道，如基因组注释和测序基因组学分析。在所有这些应用中，分析的可靠性和准确性关键取决于底层对齐的质量。目前有大量的MSA计算机程序和算法（Notredame，2007），它们实现了不同的算法来找到MSA问题的数学最优解。据报道，最好的算法的准确度为80-90%，但即使是最好的评分比对算法也可能在某些蛋白质家族或比对中的特定区域失败。这种情况在大规模分析中是不稳定的，在大规模分析中，使用更快但不太可靠的算法和大量自动选择的序列。 因此，通常认为，调整对齐，从而消除对齐不良的区域，可以提高基于MSA的应用程序的准确性（Talavera和Castresana，2007）。已经开发了一些程序，例如G-模块（Castresana，2000），以通过选择保守区域的模块来帮助MSA修剪阶段。它们已经变得非常流行，并在中小规模数据集中广泛使用，具有良好的性能，其中可以手动测试几个参数（Talavera和Castresana，2007）。然而，它们在较大数据集上的使用受到在分析之前定义将用于所有序列家族的参数集的需要的阻碍。在这里，我们提出了trimAl，一个自动对齐修剪工具。 它的速度和自动调整参数以提高系统发育信噪比的可能性，使得trimAl特别适合于大规模的基因组分析，涉及数千个大型比对。

trimAl has been developed in a GNU/Linux environment using C++ programming language and has been tested on various UNIX, Mac and Windows platforms. Moreover, we have developed a web server to run trimAl online (http://phylemon2.bioinfo.cipf.es/), which has been included in the Phylemon suite for phylogenetic and phylogenomic tools (Tarraga et al., [2007](javascript:;)). The documentation, source files and additional information for trimAl are available through a wiki page (http://trimal.cgenomics.org/).
trimAl是在GNU/Linux环境中使用C++编程语言开发的，并在各种UNIX、Mac和Windows平台上进行了测试。此外，我们已经开发了一个网络服务器来在线运行trimAl（http：//phylemon2.bioinfo.cipf.es/），其已经被包括在Phylemon套件中，用于系统发育和非系统发育基因组工具（Tarraga等人，2007年）。trimAl的文档、源文件和其他信息可通过wiki页面（http://trimal.cgenomics.org）获得。

trimAl reads and renders protein or nucleotide alignments in several standard formats. trimAl starts by reading all columns in an alignment and computes a score (Sx) for each of them. This score can be a gap score (Sg), a similarity score (Ss) or a consistency score (Sc). The score for each column can be computed based only on the information from that column or, if a window size of w is specified, it corresponds to the average value of w columns around the position considered.
trimAl以几种标准格式读取并呈现蛋白质或核苷酸比对。trimAl通过阅读比对中的所有列开始，并为它们中的每一个计算得分（S x ）。该分数可以是间隙分数（S g ）、相似性分数（S s ）或一致性分数（S c ）。每个列的得分可以仅基于来自该列的信息来计算，或者如果指定窗口大小为w，则它对应于所考虑的位置周围的w列的平均值。

The gap score (Sg) for a column is the fraction of sequences without a gap in that position. The residue similarity score (Ss) consists of mean distance (MD) scores as described in Thompson et al. ([2001](javascript:;)) and [Supplementary Material](https://academic.oup.com/bioinformatics/article/25/15/1972/213148?login=true#supplementary-data). This score uses the MD between pairs of residues, as defined by a given scoring matrix. Finally, the consistency score (Sc) can only be computed when more than one alignment for the same set of sequences is provided. Details on how these scores are computed are provided in the [Supplementary Material](https://academic.oup.com/bioinformatics/article/25/15/1972/213148?login=true#supplementary-data). In brief, Sc measures the level of consistency of all the residue pairs found in a column as compared with the other alignments. The alignment with the highest consistency is chosen and then trimmed to remove the columns that are less conserved, according to Sc or other thresholds set by the user.
一列差距分数（S g ）是在该位置没有缺口的序列的分数。残基相似性评分（S s ）由Thompson等人（2001）和补充材料中所述的平均距离（MD）评分组成。该评分使用残基对之间的MD，如给定评分矩阵所定义。最后，只有当提供了同一组序列的多于一个比对时，才能计算一致性得分（S c ）.关于如何计算这些分数的详细信息，请参见补充材料。简而言之，S c 测量了与其它比对相比，在一个柱中发现的所有残基对的一致性水平。根据S c 或用户设置的其他阈值，选择具有最高一致性的对齐，然后对其进行修整以移除较少保留的列。

Once all column scores have been computed trimAl can proceed in two ways. If both a score and a minimum conservation threshold are provided, trimAl renders a trimmed alignment in which only the columns with scores above the score threshold are included, as far as the number of selected columns is above a conservation threshold defined by the user. If this number is below the conservation threshold, trimAl will add more columns to the trimmed alignment in a decreasing order of scores until the conservation threshold is reached. The conservation threshold corresponds to the minimum percentage of columns, from the original alignment, which the user wants to include in the trimmed alignment.
一旦计算了所有列得分，trimAl可以以两种方式进行。如果提供了分数和最小保守阈值两者，则trimAl呈现修剪的比对，其中仅包括分数高于分数阈值的列，只要所选列的数量高于由用户定义的保守阈值。如果该数量低于保守阈值，则trimAl将以分数的降序向修剪的比对添加更多列，直到达到保守阈值。保留阈值对应于原始路线中用户希望包含在修剪路线中的列的最小百分比。

Alternatively, if the automatic selection of parameters options is selected, trimAl will compute specific score thresholds depending on the inherent characteristics of each alignment. So far, trimAl incorporates three modes for the automated selection of parameters, gappyout, strict and strictplus, which are based on the different use of gap and similarity scores. Moreover, the option automated1 implements a heuristic to decide the most appropriate mode depending on the alignment characteristics. The heuristics to define such parameters have been designed based on the results of a benchmark. Details on the heuristics and the benchmark can be found in the online documentation of the program. In brief, the automatic selection of parameters approximate optimal cutoffs by plotting, internally, the cumulative graphs of gap and similarity scores of the columns in the alignment (see online documentation).
或者，如果选择了参数选项的自动选择，则trimAl将根据每个比对的固有特性计算特定的分数阈值。到目前为止，trimAl集成了三种自动选择参数的模式，gappyout，strict和strictplus，它们基于gap和相似性分数的不同使用。此外，选项automated1实现了一种启发式方法，以根据对齐特性决定最合适的模式。基于基准测试的结果设计了定义这些参数的算法。有关算法和基准的详细信息可以在该程序的在线文档中找到。简而言之，参数的自动选择通过在内部绘制比对中列的间隙和相似性得分的累积图来近似最佳截止值（参见在线文档）。

We expanded, using ROSE simulations (Stoye et al., [1998](javascript:;)) a benchmark set that has been used previously to test the improvement in phylogenetic performance after an alignment trimming phase (Talavera and Castresana, [2007](javascript:;)). This dataset simulates several evolutionary scenarios varying in the number and length of the sequences, the topology of the underlying tree and the level of sequence divergence considered. We compared the results obtained from MUSCLE alignments before and after trimming with trimAl using automated selection of parameters. The accuracy of the resulting trees was measured by comparing them with the original trees used to generate the sequence sets, and measuring the Robinson Foulds distance (Robinson and Foulds, [1981](javascript:;)). We observed an overall improvement of the phylogenetic accuracy after trimming. Using -automated1 option of trimAl, the trimmed alignment always produced Maximum Likelihood trees that were of equal (36%) or significantly better (64%) quality as compared with the tree derived from the complete alignment. For Neighbor Joining reconstruction the -strictplus option of trimAl worked best, improving the phylogenetic accuracy in 89% of the scenarios. In most scenarios (90%), trimAl outperformed Gblocks v0.91b with default parameters. Most importantly, the use of Gblocks default parameters diminished the accuracy of the subsequent tree reconstruction in half of the scenarios considered. In contrast, the use of trimAl automated methods rarely (1.5%) undermined the topological accuracy of the resulting phylogenetic tree (see [Supplementary Material](https://academic.oup.com/bioinformatics/article/25/15/1972/213148?login=true#supplementary-data) for more details).
我们扩展，使用ROSE模拟（Stoye等人，1998），这是一个基准集，以前曾用于测试比对修剪阶段后系统发育性能的改善（Talavera和Castresana，2007）。该数据集模拟了几种进化场景，这些场景在序列的数量和长度、底层树的拓扑结构和所考虑的序列分歧水平方面有所不同。我们使用自动选择的参数比较了在用trimAl修剪之前和之后从肌肉比对获得的结果。通过将所得树与用于生成序列集的原始树进行比较，并测量罗宾逊福尔德距离（罗宾逊和福尔德，1981），来测量所得树的准确性。我们观察到修剪后的系统发育准确性的整体改善。 使用trimAl的-automated 1选项，修剪的比对总是产生最大似然树，与从完全比对中得到的树相比，其质量相等（36%）或显著更好（64%）。对于相邻连接重建，trimAl的-strictplus选项工作得最好，在89%的场景中提高了系统发育的准确性。在大多数情况下（90%），trimAl优于默认参数的Gblocks v0.91b。最重要的是，在所考虑的一半场景中，使用Gblocks默认参数降低了后续树重建的准确性。相比之下，使用trimAl自动化方法很少（1.5%）破坏所得到的系统发育树的拓扑准确性（更多细节见补充材料）。

To test the applicability of trimAl on real datasets as well as its suitability for large-scale phylogenetic datasets, we ran trimAl on the complete set of MUSCLE alignments generated for the Human Phylome project (Huerta-Cepas et al., [2007](javascript:;)). This includes a total of 31 182 alignments, containing, on average, 67 sequences of 1472 positions of length. Trimming these alignments using the -gappyout and automated1 options used 5 min 45 s and 125 min, 2 s, respectively, on a computer with an Intel QuadCore XEON E5410 processors and 8 GB of RAM.
为了测试trimAl在真实的数据集上的适用性以及其对大规模系统发育数据集的适用性，我们在为人类Phylome项目生成的完整的肌肉比对集上运行trimAl（Huerta—Cepas等人，2007年）。这包括总共31182个比对，平均包含67个序列，长度为1472个位置。在配备英特尔四核至强E5410处理器和8 GB RAM的计算机上，使用—gappyout和automated1选项修剪这些比对分别需要5 min 45 s和125 min 2 s。

trimAl has been used previously in a pipeline to reconstruct complete collections of gene trees. In this case, the parameter sets used were a minimum conservation threshold of 60% and a gap threshold of 90% (-cons 60 -gt 0.9). Complete and trimmed alignments used to generate the phylomes included in PhylomeDB (Huerta-Cepas et al., [2008](javascript:;)) can be viewed through this database.
trimAl先前已经在管道中用于重建基因树的完整集合。在这种情况下，使用的参数集是60%的最小保守阈值和90%的间隙阈值（-cons 60 -gt 0.9）。用于生成PhylomeDB中包括的系统发育组的完整和修剪的比对（Huerta-Cepas等人，2008年，可以通过这个数据库。
