# ❖ Github API 访问次数限制

[参考官方说明](https://developer.github.com/v3/#rate-limiting)

如果没有任何授权直接访问的话，单IP限制每小时60次requests。如果有授权的话，每小时5000次。
![image](https://user-images.githubusercontent.com/14041622/36171363-5351c5a8-113d-11e8-9134-26f50844efd1.png)

通过官方介绍，我们可以在response返回的headers中获取`X-RateLimit-Remaining`和`X-RateLimit`来查看当前剩余的访问次数和当前的每小时限次。

![image](https://user-images.githubusercontent.com/14041622/36188652-53291c34-1188-11e8-89ec-6501c26c5563.png)


