+++
date = "2024-06-01T00:00:00+08:00"
draft = false
title = """linux 合并PDF"""
tags = ["Linux", "软件"]
+++

```shell
pdftk input1.pdf input2.pdf input3.pdf cat output output.pdf

#提取1-15页为一个文件
$ pdftk input.pdf cat 1-15 output new.pdf

```

该命令行使用了`pdftk`工具，它是一个用于处理PDF文件的强大的命令行工具。这条命令的具体功能是将多个PDF文件合并成一个单一的PDF文件。下面是对该命令的详细解释：

- `pdftk`: 这是指令的开始，表示你正在调用`pdftk`这个程序来执行一个操作。

- `input1.pdf input2.pdf input3.pdf`: 这里列出了你要合并的输入PDF文件名。在这个例子中，有三个输入文件，分别是`input1.pdf`、`input2.pdf`和`input3.pdf`。你可以根据需要添加或减少输入文件的数量，只需用空格分隔每个文件名即可。

- `cat`: 这是`pdftk`中的一个操作指令，代表“concatenate”的简写，意为“连接”或“合并”。当你在`pdftk`命令中使用`cat`时，意味着你想把列出的PDF文件按顺序合并起来。

- `output output.pdf`: `output`后面跟着的是输出文件的名称，即合并后的新PDF文件名。在这个例子中，合并后的文件将被命名为`output.pdf`。

综上所述，整个命令的作用是将`input1.pdf`、`input2.pdf`和`input3.pdf`这三个PDF文件按照顺序合并成一个新的PDF文件，并将该合并后的文件保存为`output.pdf`。
