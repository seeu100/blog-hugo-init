+++
date = "2025-04-18T00:00:00+08:00"
draft = false
title = """Linux账户过期"""
tags = ["Linux"]
+++

## 报错信息
```sh
❯ git push
Your account has expired; please contact your system administrator.
Connection closed by 127.0.0.1 port 22
致命错误：无法读取远程仓库。

请确认您有正确的访问权限并且仓库存在。


❯ ssh gitea@127.0.0.1 -p 22
Your account has expired; please contact your system administrator.
Connection closed by 127.0.0.1 port 22
```

## 查看账户过期时间
```sh
# 查看当前有效期
❯ sudo chage -l gitea
最近一次密码修改时间                                    ：4月 15, 2025
密码过期时间                                    ：从不
密码失效时间                                    ：从不
帐户过期时间                                            ：1月 02, 1970
两次改变密码之间相距的最小天数          ：-1
两次改变密码之间相距的最大天数          ：-1
在密码过期之前警告的天数        ：-1
```


## 延长有效期

```sh
# 设置新过期时间（例如设为2030年）
sudo chage -E "2030-01-01" gitea

# 或直接清除过期状态
sudo chage -E -1 gitea
```
