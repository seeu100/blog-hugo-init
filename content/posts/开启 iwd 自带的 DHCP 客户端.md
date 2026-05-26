+++
date = "2023-04-27T00:00:00+08:00"
draft = false
title = """开启 iwd 自带的 DHCP 客户端"""
tags = ["Linux", "环境搭建"]
+++

在 `/etc/iwd/main.conf` 添加：
```shell
[General]
EnableNetworkConfiguration=true

```
<!-- ##{"timestamp":1682524800}## -->
