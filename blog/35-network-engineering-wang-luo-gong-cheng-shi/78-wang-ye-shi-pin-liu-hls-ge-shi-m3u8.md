# ❖ 网页视频流HLS 格式(m3u8/ts)视频下载

现在很多视频网站播放流视频，都不是采用mp4／flv文件直接播放，而是采用`HLS`(m3u8/ts)这种方式播放。

简单说就是，网站后台把视频切片成成百上千个`xx.ts`文件，一般10秒一个，每个都几百kb很小。然后通过`xx.m3u8`播放列表把这些文件连接起来。

通过Chrome DevTool的Network栏，我们可以清楚的看到加载过程：

![image](https://user-images.githubusercontent.com/14041622/52861210-bede9d00-316c-11e9-92e3-d7537ab980b2.png)

我们直接点击这个`playlist.m3u8`播放列表文件，在旁边的`preview`栏中查看内容，可以看到：
```m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-ALLOW-CACHE:YES
#EXT-X-TARGETDURATION:11
#EXTINF:5.250000,
out000.ts
#EXTINF:9.500000,
out001.ts
#EXTINF:8.375000,
out002.ts
#EXTINF:5.375000,
out003.ts
#EXTINF:9.000000,
out004.ts
...........
```


那我们怎么下载呢？

## 下载视频所有的ts切片文件

一般的思路是，想办法把所有的ts切片文件下载下来，然后合成一个完整的视频。
然而，配合`xx.m3u8`播放列表文件，我们可以直接用`ffmpeg`在线下载播放列表中所有的视频，然后直接用ffmpeg合并为一个视频。

我们就直接执行这一句命令即可：
```sh
$ ffmpeg -i <m3u8-path> -c copy OUTPUT.mp4
$ ffmpeg -i <m3u8-path> -vcodec copy -acodec copy OUTPUT.mp4

# 例如：
ffmpeg -i https://v6.438vip.com/2018/10/17/3JAHPTdvPhQb9LrE/playlist.m3u8 -c copy  OUTPUT.mp4
```

然后就会看到这样的下载过程：

![image](https://user-images.githubusercontent.com/14041622/52861582-e1bd8100-316d-11e9-8153-69a20665155d.png)


为什么下载播放列表就能下载所有的切片文件？
因为播放列表里的都是相对路径，既然我们有了播放列表的绝对路径，那么其它所有文件的绝对路径也就不难获取了。
好在ffmpeg直接实现了这种播放列表一键下载的方式。


## 必须登录的视频下载

`ffmpeg`不支持cookies，所以如果视频网站需要登录才能看，那么ffmpeg就无能为力了。
这种时候，有两种解决思路：
- HLS视频流捕获的Chrome插件
- 根据播放列表手动整理所有ts文件的下载连接，用wget/curl加cookies下载。


### Chrome插件下载HLS流视频

目前推荐的Chrome插件有：
- [Stream Recorder](https://chrome.google.com/webstore/detail/stream-recorder-download/iogidnfllpdhagebkblkgbfijkbkjdmm)
- [Stream Video Downloader](https://chrome.google.com/webstore/detail/stream-video-downloader/imkngaibigegepnlckfcbecjoilcjbhf?hl=en)

Chrome插件因为是在浏览器里的，所以直接可以获取cookies和user-agent，只要自己能看，插件就能下载。


### Wget／Curl下载HLS流视频

简单来说，就是把`xx.m3u8`播放列表下载，然后从里面抽取所有的文件名称，并在前缀加上完整的URL链接，然后用wget/curl以下载文件列表的方式批量下载。最后用ffmpeg合并所有视频文件。
