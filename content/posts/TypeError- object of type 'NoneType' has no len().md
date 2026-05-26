+++
date = "2024-01-01T00:00:00+08:00"
draft = false
title = """TypeError- object of type 'NoneType' has no len()"""
+++

实例脚本：https://github.com/Meekdai/Gmeek/blob/main/Gmeek.py

错误信息：
```python
TypeError: object of type 'NoneType' has no len()
```

错误代码定位：
```python
self.blogBase[listJsonName][postNum]["wordCount"]=len(issue.body)
```

尝试获取 `issue.body` 的长度，但 `issue.body` 的值是 `None` 类型，而在 Python 中对 `None` 类型对象调用 `len()` 函数是不合法的，因为 `None` 表示没有值或空值。

即将某个 GitHub issue 的正文内容（即 `issue.body`）的长度赋值给博客基础数据结构（`self.blogBase[listJsonName][postNum]["wordCount"]`）。当遇到无法获取到 issue 正文或者正文为空时，会引发 TypeError。


解决这个问题的办法是在执行 `len(issue.body)` 之前，先检查 `issue.body` 是否非空：

```python
if issue.body is not None:
    self.blogBase[listJsonName][postNum]["wordCount"] = len(issue.body)
else:
    # 处理 body 为空的情况，可以设置默认值或者跳过
    pass
```

