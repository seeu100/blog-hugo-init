+++
date = "2024-04-18T00:00:00+08:00"
draft = false
title = """迁移博客到 github issues"""
tags = ["记录"]
+++

[Gmeek](https://github.com/Meekdai/Gmeek) 一个博客框架，超轻量级个人博客模板，完全基于`Github Pages` 、 `Github Issues` 和 `Github Actions`，可以称作`All in Github`。不需要本地部署，从搭建到写作，只需要18秒，2步搭建好博客，第3步就是写作。

[Gmeek快速上手](https://blog.meekdai.com/post/Gmeek-kuai-su-shang-shou.html)
[Issues · Meekdai/Gmeek](https://github.com/Meekdai/Gmeek/issues)

### 如果要导入以前的文章，如何设置发布时间呢？

如需修改发布时间，可以在文章最后一行添加如下代码。里面的时间是采用时间戳的形式，可以用如下[网站](https://tool.lu/timestamp)转换。

```html
<!-- ##{"timestamp":1490764800}## -->
```
