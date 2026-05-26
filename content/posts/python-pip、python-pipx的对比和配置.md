+++
date = "2024-04-20T00:00:00+08:00"
draft = false
title = """python-pip、python-pipx的对比和配置"""
tags = ["Linux", "摘录"]
+++

pipx只能使用二进制作为全局工具，不适合作为库来调用。因此，还是要安装pip。

- **pip**: 主要设计用于安装Python包（包括库和应用程序），并且可以在项目级别的虚拟环境中进行隔离式安装，以避免不同项目之间的依赖冲突。当你需要在代码中导入某个库并在程序内部调用其功能时，应该使用`pip`将库安装到项目的虚拟环境中。

- **pipx**: 则专注于将独立的、可执行的Python应用安装到用户的全局环境中，使其能够在任何地方作为命令行工具使用，而不受特定项目或虚拟环境的影响。由于这些工具通常是独立运行且不涉及与其他库或项目集成，所以它们适合通过`pipx`全局安装。

## 安装
```shell
# 使用pacman（Arch Linux的包管理器）安装Python的pip和pipx工具
sudo pacman -S python-pip python-pipx

# 配置pip以使用国内镜像源加速包下载
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 创建并激活虚拟环境
```shell
# 使用Python内置模块venv创建一个名为envname的虚拟环境
python -m venv envname

# 激活刚刚创建的虚拟环境，使得在这个终端会话中所有pip安装的库只在这个环境中可见和可用
source envname/bin/activate
```

通过以上步骤，在全局环境中使用`pipx`安装命令行工具的同时，我们仍然依赖于常规的`pip`来在特定的虚拟环境中安装库文件。这是因为虚拟环境提供了隔离性，使得每个项目拥有独立的Python环境和依赖版本，这对于开发和维护多个项目至关重要。而在虚拟环境之外，通过`pipx`安装的工具则可以在任何环境下跨项目共享和使用。

## 参考

- [Python/Virtual environment - ArchWiki](https://wiki.archlinux.org/title/Python/Virtual_environment)
