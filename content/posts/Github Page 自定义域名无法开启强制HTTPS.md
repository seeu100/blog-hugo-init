+++
date = "2024-04-20T00:00:00+08:00"
draft = false
title = """Github Page 自定义域名无法开启强制HTTPS"""
tags = ["记录", "bug", "网络"]
+++

报错如下：
Enforce HTTPS — Unavailable for your site because your domain is not properly configured to support HTTPS ([`00002000.xyz`](http://00002000.xyz/)) — [Troubleshooting custom domains](https://docs.github.com/articles/troubleshooting-custom-domains/#https-errors)

HTTPS provides a layer of encryption that prevents others from snooping on or tampering with traffic to your site.
When HTTPS is enforced, your site will only be served over HTTPS. [Learn more about securing your GitHub Pages site with HTTPS](https://docs.github.com/articles/securing-your-github-pages-site-with-https).

原因：用cloudflare解析DNS记录并开启了代理（Proxy），先**取消代理**即可。
运行命令：`dig blog.00002000.xyz +noall +answer -t A`

开启代理时：
```
blog.00002000.xyz.      600     IN      A       104.21.82.3
blog.00002000.xyz.      600     IN      A       172.67.167.86
```

关闭代理时：
```
blog.00002000.xyz.      300     IN      CNAME   seeu100.github.io.
seeu100.github.io.      3600    IN      A       185.199.108.153
seeu100.github.io.      3600    IN      A       185.199.109.153
seeu100.github.io.      3600    IN      A       185.199.110.153
seeu100.github.io.      3600    IN      A       185.199.111.153
```

使用Cloudflare的DNS解析服务时，如果启用了代理，那么原本直接指向GitHub Pages服务器的DNS解析记录将被替换为指向Cloudflare的CDN节点。这样虽然可以实现SSL/TLS加密，但由于Cloudflare与GitHub Pages之间没有建立正确的HTTPS连接配置，可能会导致GitHub Pages无法正确识别并强制启用HTTPS。

GitHub Pages仅能识别那些直接指向其IP地址或者经过正确CNAME映射的域名，而无法识别通过Cloudflare代理后的DNS记录，因此会出现“Enforce HTTPS — Unavailable for your site”的错误提示。

总的来说，使用Cloudflare的DNS解析服务时，要使GitHub Pages上的自定义域名支持HTTPS，请按照以下步骤操作：
1. 登录Cloudflare账户并前往相应域名的DNS设置页面。
2. 将该域名或子域名的DNS记录从"Proxy (橙色云朵)"模式切换至"DNS only (灰色云朵)"模式，以禁用Cloudflare的代理功能。
3. 确保CNAME或A记录指向[GitHub Pages的指定地址](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https#verifying-the-dns-configuration)。
4. 在GitHub Pages的设置中添加或确认你的自定义域名，并等待DNS更改在全球范围内传播生效。
5. 在GitHub Pages中验证并启用HTTPS服务。
