+++
date = "2024-05-29T00:00:00+08:00"
draft = false
title = """wget爬取网站为本地镜像"""
tags = ["Linux", "软件"]
+++


```shell
wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains example.org --no-parent http://example.org/some-directory/
```

    --recursive：启用递归下载。
    --no-clobber：如果文件已存在，不会被覆盖。
    --page-requisites：下载构成页面的所有文件，如图片和样式表。
    --html-extension：强制保存网页文件的后缀为.html。
    --convert-links：将下载后的HTML文件中的链接转换为本地链接。
    --restrict-file-names=windows：限制文件名字符，以兼容Windows和其他系统。
    --domains example.org：限定下载的文件只能来自example.org这个域名，避免跨越到其他域。
    --no-parent：不追溯到上一级目录。

请将上述命令中的`example.org`和`http://example.org/some-directory/`替换为您实际要下载的镜像网站地址和目录。

使用wget命令行工具爬取镜像网站时，需要谨慎操作，确保行为符合网站的使用条款和robots.txt规则，不违反版权法律。通常，镜像网站是为了分发开源软件、操作系统镜像等合法资源而设立的，但直接全面镜像一个网站的内容（尤其是包含大量版权材料的网站）很可能会触及法律和道德边界。

再次强调，在执行任何下载任务前，请确保合法并尊重网站规定。对于大规模或全站下载，最好直接联系网站管理员获取明确许可。
