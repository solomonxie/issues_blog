# Chrome浏览器疑难杂症
主要在这里记录Chrome为首的一些浏览器操作日常中的问题和经验


## Chrome无法访问某特定网页 但是Safari和其它浏览器能正常访问
> 实际上这个“疑难杂症”系列的开启，就是源于今天近一个小时解决Chrome无法访问Github.io的问题。
由于现在在国内，所以装了各种Shadowsocks和Chrome切换代理插件，甚至还修改了本地的Hosts文件。所以一旦遇到无法访问网页，真是要伸手到很多地方去开启、关闭、各种调试。不过最终终于在chrome的插件管理里面找到了问题。
### 尝试方法
**由于之前安装了`AdBlock`插件，删除它**
实际上我装了以后一直没有使用这个插件，因为会被很多网站检测到并提示这个做法不道德。所以我就长期将这个插件放在不启动模式。但是没想到即便不启动，它仍然有屏蔽一些网站的功能。导致我无法访问github.io的各种个人主页。

### 解决方案后记
删除adblock插件后没多久就又无法访问了，所以再想别的问题。不断尝试后发现，只要把所有的url地址都强制改为`https://`安全链接，就能访问。


# 插件合集：网站技术栈检测

类别：`Web Dev Tools`
作用：显示当前网站的技术栈组成

## Overview
- `Wappalyzer`分类显示清晰好看，速度快。
- `BuiltWith Technology Profiler`速度慢，css样式还经常加载不出来。还显示好多不太用得到的东西和连接，把内容弄的很长让你去翻页看。
- `Lighthouse` 用时长，检测单个网页，然后单独弹出一个网页显示报告结果。显示清晰，结果分类详细展示很容易看。信息很有价值。
- `SimilarWeb` 超详细检测当前网站的类似网站、被引用情况、SEO信息、用户分类统计等。超详细超有料！
- `YSlow` 网页加载检测报告。非常详细，但是报告排版不是很容易看懂。比Lighthouse快

## [`Wappalyzer`](https://chrome.google.com/webstore/detail/wappalyzer/gppongmhjkpfnbhagpmjfkannfbllamg?hl=en)

![image](https://user-images.githubusercontent.com/14041622/39408505-ed637716-4c09-11e8-8a9e-ab9d5f4abfa4.png)


## [`BuiltWith Technology Profiler`](https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en)

![image](https://user-images.githubusercontent.com/14041622/39408442-da1ac7b4-4c08-11e8-9f25-168b53397887.png)

## [`CSSViewer`](https://chrome.google.com/webstore/detail/cssviewer/ggfgijbpiheegefliciemofobhmofgce)

鼠标放在哪，就显示哪的css样式。按ESC取消。

![image](https://user-images.githubusercontent.com/14041622/39408554-c6bd0428-4c0a-11e8-9a3a-421ec1a665a7.png)


## [`Lighthouse` ](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)
> Reports on how the webpage loaded.

![image](https://user-images.githubusercontent.com/14041622/39408796-6fa39bc6-4c0e-11e8-9ef9-d3690115ec32.png)

## [`SimilarWeb`](https://chrome.google.com/webstore/detail/similarweb-traffic-rank-w/hoklmmgfnpapgjgcpechhaamimifchmp)

> 超详细检测当前网站的类似网站、被引用情况、SEO信息、用户分类统计等。超详细超有料！

![image](https://user-images.githubusercontent.com/14041622/39408826-16a3a40c-4c0f-11e8-90a7-f96b1e3a4d91.png)


## [`YSlow`](https://chrome.google.com/webstore/detail/yslow/ninejjcohidippngpapiilnmkgllmakh) - 网页加载检测报告
> YSlow analyzes web pages and suggests ways to improve their performance based on a set of rules for high performance web pages.

![image](https://user-images.githubusercontent.com/14041622/39408906-5a607ebc-4c10-11e8-8bec-bb246a927eda.png)



# 插件合集：网页加载优化

## [`Decentraleyes`](https://chrome.google.com/webstore/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj)

> 通过加载本地其事先加载好的资源，并拦截其他第三方的资源请求来加快网页加载速度，该插件还能在加快网页加载速度的同时还能减少一些跟踪脚本的跟踪功能以使得你的网络环境更加安全。

[参考文章](http://chromecj.com/productivity/2017-12/854.html)

![image](https://user-images.githubusercontent.com/14041622/39408585-3f3649c8-4c0b-11e8-9043-4f4834de86a3.png)


## [`Ghostery`](https://chrome.google.com/webstore/detail/ghostery-%E2%80%93-privacy-ad-blo/mlomiejdfkolichcflejclcbmpeaniij) - Privacy Ad Blocker

> Ghostery’s built-in ad blocker removes advertisements from a webpage to eliminate clutter so you can focus on the content you want.
Protect your privacy
Ghostery allows you to view and block trackers on websites you browse to control who collects your data. Enhanced Anti Tracking also anonymizes your data to further protect your privacy.
Browse faster
Ghostery’s Smart Blocking feature speeds up page loads and optimizes page performance by automatically blocking and unblocking trackers to meet page quality criteria.
Customize your display
Ghostery offers multiple displays and insights dashboards so you can see the information that’s relevant to you.

![image](https://user-images.githubusercontent.com/14041622/39408766-dd438cbe-4c0d-11e8-8f36-1ef6957bc9a6.png)


## [`Gooreplacer`](https://chrome.google.com/webstore/detail/gooreplacer/jnlkjeecojckkigmchmfoigphmgkgbip)

> 重定向/屏蔽 URL，修改/删除 headers. gooreplacer 最初为解决国内无法访问 Google 资源（Ajax、API等）导致页面加载速度巨慢而生，新版在此基础上，增加了更多实用功能，可以方便用户屏蔽某些请求，修改 HTTP 请求/响应 的 headers。

[中文官方介绍](https://github.com/jiacai2050/gooreplacer)
[使用语法指南](https://github.com/jiacai2050/gooreplacer/blob/master/doc/guides.md)

![image](https://user-images.githubusercontent.com/14041622/39408814-bce94480-4c0e-11e8-81f9-df25d0415ec7.png)

## [`AdBlock`](https://chrome.google.com/webstore/detail/adblock/gighmmpiobklfepjocnamgkkbiglidom)
> The most popular Chrome extension, with over 40 million users! Blocks ads all over the web.

![image](https://user-images.githubusercontent.com/14041622/39409037-601b1446-4c12-11e8-8dc2-21b84232a3fa.png)


