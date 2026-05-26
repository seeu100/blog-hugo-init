+++
date = "2024-04-19T00:00:00+08:00"
draft = false
title = """Windows Hugo 环境搭建"""
tags = ["Windows", "环境搭建"]
+++

天啊，我竟然在Windows上尝试搭建开发环境，这话放以前我绝不敢相信。然而，现在啥都看开了~~，区区Windows而已，我还要开始灌水式博客了呢:)

## 安装包管理器Chocolatey

安装方式不止两种，我选择通过`cmd.exe`安装，注意本文的命令貌似都需要管理员权限。

```powershell
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

## 安装hugo

```powershell
choco upgrade chocolatey
choco install hugo -confirm ## 尴尬的是从GitHub下载包的过程卡在3%不动了，于是我又试了一次，速度很慢，但总算成功了。
```

## 最后，开始你的hugo旅程吧！顺便说一句，Windows其实也还行（假装很正经）>>>逃~~

## 参考链接

*   https://chocolatey.org/install
*   https://gohugo.io/getting-started/installing/
<!-- ##{"timestamp":1650988800}## -->

