+++
date = "2024-04-18T00:00:00+08:00"
draft = false
title = """nssm - Windows服务封装程序"""
tags = ["软件", "Windows"]
+++

**对于Windows平台来说，很多软件或系统的后台服务是基于windows服务的方式运行的，它的优势是稳定可靠，有进程保护**。

**NSSM是一个服务封装程序，它可以将普通exe程序或bat文件封装成服务，使之像windows服务一样运行**。
同类型的工具还有微软自己的srvany，不过nssm更加简单易用，并且功能强大。它的特点如下：

1. 支持普通exe程序（控制台程序或者带界面的Windows程序都可以）或bat文件
2. 安装简单又方便
3. 可以重定向输出（并且支持Rotation）
4. 可以自动守护封装了的服务，程序挂掉了后可以自动重启
5. 可以自定义环境变量
6. 可以自定义启动参数

NSSM的官网下载地址：http://nssm.cc/download

#### Latest release

[nssm 2.24](https://nssm.cc/release/nssm-2.24.zip) *(2014-08-31)*
[be7b3577c6e3a280e5106a9e9db5b3775931cefc]

#### Featured pre-release（winsows10之后建议用这个版本）

[nssm 2.24-101-g897c7ad](https://nssm.cc/ci/nssm-2.24-101-g897c7ad.zip) *(2017-04-26)*
[ca2f6782a05af85facf9b620e047b01271edd11d]

```powershell
nssm install 服务名称  #安装服务
nssm remove 服务名称  #删除服务
nssm remove 服务名称 confirm  #删除服务确定
nssm edit 服务名称  #修改服务（显示界面修改）
nssm start 服务名称  #启动服务
nssm stop 服务名名称  #停止服务
nssm restart <servicename> #重启服务
nssm pause <servicename> #暂停/继续服务
nssm continue <servicename> #暂停/继续服务
nssm status <servicename> #查看服务状态

```

