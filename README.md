# 咪咕爱看签到

一点小羊毛。**好哥哥们顺手点个 star 吧。**

通过 github action 来实现自动签到（每天 50M 流量，每隔 5 天 0.38 元话费）

## 步骤

### 1 fork 这个仓库

点击右上角的 fork。

### 2 获取 cookie

通过抓包咪咕爱看签到的请求，获取 cookie，其实只需要 cookie 中的 mToken 这个值就好了。

### 3 设置 cookie

在 fork 后**自己的**仓库中依次点击 `Settings` - `Secrets` - `New repository secret`，如下图所示：

![image-20210111220035535](README.assets/image-20210111220035535.png)

然后添加一个名为 `COOKIE` 的变量，内容为获取到的 cookie，类似于 `mToken=...`。

`COOKIE` 示例：

```text
1283: mToken=eyJ0aW1lc3RhbXAiOjE2NDY5OTg4NDQ0NTAsInJvd1Rva2VuIjoiNDgwOTA1NjZkMDE2ODA1MGQzMmM3MzcwZDAyNzg3NTEiLCJ1aWQiOjIzNDY4MjIsIm1vYmlsZSI6IjE4MzU4NTcxMjgzIiwiZXh0ZW5kIjoie1wibW9iaWxlVHlwZVwiOlwiMFwifSIsImRldmljZUlkIjoiMDUwNDMxODhkOTFiZGVkOCIsImNsaWVudFZlcnNpb24iOiI1LjMuMSIsImRldmljZU1vZGVsIjoiSE9OT1IiLCJndWVzdCI6ZmFsc2UsInNpZ24iOiIwNTFlN2IzMjdjNWYwZjk4OTM5ZDVhOTUwNGY1NGFkMiJ9; 
```

```text
0384: mToken=eyJ0aW1lc3RhbXAiOjE2NDY5OTk0NDY4ODEsInJvd1Rva2VuIjoiNWVkOWI0NDg5ZjRjNDNlNDZmMDEyNmIxYjJmNzUyYzYiLCJ1aWQiOjE2NTE2MjAwLCJtb2JpbGUiOiIxMzQ4NjU5MDM4NCIsImV4dGVuZCI6IntcIm1vYmlsZVR5cGVcIjpcIjBcIn0iLCJkZXZpY2VJZCI6IjA1MDQzMTg4ZDkxYmRlZDgiLCJjbGllbnRWZXJzaW9uIjoiNS4zLjEiLCJkZXZpY2VNb2RlbCI6IkhPTk9SIiwiZ3Vlc3QiOmZhbHNlLCJzaWduIjoiMTkzMTBkNmU5ODAyODdkMDA1Nzg2ZTg0M2QxNDRlNTMifQ;
```

```text
0402: mToken=eyJ0aW1lc3RhbXAiOjE2NDY5OTk2NDQ0MTQsInJvd1Rva2VuIjoiNzc0N2MzZmVkNTA1NjA1NTU2M2Y3ZmE2MDA0MDIxNDMiLCJ1aWQiOjM2MDU1ODYsIm1vYmlsZSI6IjEzOTY3NTMwNDAyIiwiZXh0ZW5kIjoie1wibW9iaWxlVHlwZVwiOlwiMFwifSIsImRldmljZUlkIjoiMDUwNDMxODhkOTFiZGVkOCIsImNsaWVudFZlcnNpb24iOiI1LjMuMSIsImRldmljZU1vZGVsIjoiSE9OT1IiLCJndWVzdCI6ZmFsc2UsInNpZ24iOiI0MzMyNGE3MzNkMjg0YjZmOGZlNTBjOTU2N2UzN2IxMyJ9; 
```

```text
树吉: mToken=eyJ0aW1lc3RhbXAiOjE2Mzc5MzAzMjA0NDksInJvd1Rva2VuIjoiOWYwN2MzNzE4MTAzZjU3YWFjODU4MTFiZjhkYThmMTEiLCJ1aWQiOjExODg5MzQ1LCJtb2JpbGUiOiIxMzU2NzU2MzI2OCIsImV4dGVuZCI6IntcIm1vYmlsZVR5cGVcIjpcIjBcIn0iLCJkZXZpY2VJZCI6ImVlY2QwZTg5NDBjMDY2YjIiLCJjbGllbnRWZXJzaW9uIjoiNS4yLjMiLCJkZXZpY2VNb2RlbCI6IlhpYW9taSIsImd1ZXN0IjpmYWxzZSwic2lnbiI6IjIyZWU5MzViZjJkODdiOTllYmIxMDc2MmZmNTU5YjRhIn0;
```

```text
1283: mToken=eyJ0aW1lc3RhbXAiOjE2MzYxMTEzMTA3NjcsInJvd1Rva2VuIjoiMTJlODkxZmNhZWI0ZjJjY2M5MWY2NDZiNTE5MmMzMDAiLCJ1aWQiOjIzNDY4MjIsIm1vYmlsZSI6IjE4MzU4NTcxMjgzIiwiZXh0ZW5kIjoie1wibW9iaWxlVHlwZVwiOlwiMFwifSIsImRldmljZUlkIjoiMDUwNDMxODhkOTFiZGVkOCIsImNsaWVudFZlcnNpb24iOiI1LjEuOSIsImRldmljZU1vZGVsIjoiSE9OT1IiLCJndWVzdCI6ZmFsc2UsInNpZ24iOiJhOTIzYTg5NjhjOWJkY2RmMGQ3NmQ1NTE1NjI1NWJlOCJ9;
```

```text
1283: mToken=eyJ0aW1lc3RhbXAiOjE2MzYxMTEzMTA3NjcsInJvd1Rva2VuIjoiMTJlODkxZmNhZWI0ZjJjY2M5MWY2NDZiNTE5MmMzMDAiLCJ1aWQiOjIzNDY4MjIsIm1vYmlsZSI6IjE4MzU4NTcxMjgzIiwiZXh0ZW5kIjoie1wibW9iaWxlVHlwZVwiOlwiMFwifSIsImRldmljZUlkIjoiMDUwNDMxODhkOTFiZGVkOCIsImNsaWVudFZlcnNpb24iOiI1LjEuOSIsImRldmljZU1vZGVsIjoiSE9OT1IiLCJndWVzdCI6ZmFsc2UsInNpZ24iOiJhOTIzYTg5NjhjOWJkY2RmMGQ3NmQ1NTE1NjI1NWJlOCJ9;
```

### 4 运行

随便发起一个 push 请求，可以修改一下 `README.md`，或者自己给自己点个 star，就可以开始。之后就会每小时进行一次签到（因为有时候签到会失败，好像是服务器不太好，就设置一下每小时签到一次保证成功吧）。

注意，在官方文档中有这么一段：

> To prevent unnecessary workflow runs, scheduled workflows may be disabled automatically. When a public repository is forked, scheduled workflows are disabled by default. In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days.

也就是说，**定时执行的任务需要每隔 60 天激活一次**。
