# Ebbinghaus' Forgetting Curve 艾宾浩斯遗忘曲线
> 主要做为日常Reminder工具：根据遗忘曲线将笔记定期发邮件给自己。

[Wiki: Forgetting Curve](https://en.wikipedia.org/wiki/Forgetting_curve)

实现：
通过在这个issue里添加comment，每个comment算一篇笔记。
根据每个comment里写的时间设定，将笔记发送到邮箱里。

技巧：
- comment里面加上`<data><!-- {"time": xxx, "updated_time": xxx} --></data>`这样的隐形标签，保存json数据，达到传达指令和记录更新数据的功能。
- 遗忘曲线的起点设定为该comment的`created_time`。
- 

隐形标签JSON数据：
```html
<data><!-- 
{
    "time": "2018-05-03",
    "updated": "2018-05-10",
    "reviewed_count": 3
}
--></data>
```


