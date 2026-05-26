+++
date = "2023-04-27T00:00:00+08:00"
draft = false
title = """docker 镜像"""
tags = ["Linux", "环境搭建"]
+++

```shell
sudo pacman -S docker #安装docker（archlinux为例）
sudo usermod -aG docker username #添加用户到docker组，否则要root权限才能运行
newgrp docker
sudo mkdir /etc/docker
#添加镜像：
MIRROR=http://hub-mirror.c.163.com
cat <<EOF | sudo tee /etc/docker/daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "registry-mirrors": ["$MIRROR"]
}
EOF

sudo systemctl enable docker #开机自启docker服务
```

<!-- ##{"timestamp":1682524800}## -->
