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

## [`Wappalyzer`](https://chrome.google.com/webstore/detail/wappalyzer/gppongmhjkpfnbhagpmjfkannfbllamg?hl=en)
> 分类显示清晰好看，速度快（与网页一起加载）。但是长期占用200M以上内存。

![image](https://user-images.githubusercontent.com/14041622/39408505-ed637716-4c09-11e8-8a9e-ab9d5f4abfa4.png)

## [`WhatRuns`](https://chrome.google.com/webstore/detail/whatruns/cmkdbmfndkfgebldhnkbfhlneefdaaip?hl=en)
> 占用内存小，但是需要临时检测，所以要等待出结果。界面好看。

![image](https://user-images.githubusercontent.com/14041622/39425552-94f9aef6-4cae-11e8-848b-fbe5a6910c35.png)


## [`SimilarTech Prospecting`](https://chrome.google.com/webstore/detail/similartech-prospecting/jiabgmelnfhgjkfdaoiccfcbaedjfcnm/related?hl=fil)
> 临时加载，但是信息非常非常全面。非弹出窗口，而是在网页中加载一个竖条，失去焦点后不会消失，很方便。比较慢，但是信息全，分类方便看。

![image](https://user-images.githubusercontent.com/14041622/39425662-0d8ee75a-4caf-11e8-8fe0-7ef8b85518ee.png)


## [`BuiltWith Technology Profiler`](https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en)
> 速度慢，css样式还经常加载不出来。还显示好多不太用得到的东西和连接，把内容弄的很长让你去翻页看。

![image](https://user-images.githubusercontent.com/14041622/39408442-da1ac7b4-4c08-11e8-9f25-168b53397887.png)

## [`CSSViewer`](https://chrome.google.com/webstore/detail/cssviewer/ggfgijbpiheegefliciemofobhmofgce)

鼠标放在哪，就显示哪的css样式。按ESC取消。

![image](https://user-images.githubusercontent.com/14041622/39408554-c6bd0428-4c0a-11e8-9a3a-421ec1a665a7.png)


## [`Lighthouse` ](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)
> Reports on how the webpage loaded.
用时长，检测单个网页，然后单独弹出一个网页显示报告结果。显示清晰，结果分类详细
展示很容易看。信息很有价值。

![image](https://user-images.githubusercontent.com/14041622/39408796-6fa39bc6-4c0e-11e8-9ef9-d3690115ec32.png)

## [`SimilarWeb`](https://chrome.google.com/webstore/detail/similarweb-traffic-rank-w/hoklmmgfnpapgjgcpechhaamimifchmp)
> 超详细检测当前网站的类似网站、被引用情况、SEO信息、用户分类统计等。超详细超有料！


![image](https://user-images.githubusercontent.com/14041622/39408826-16a3a40c-4c0f-11e8-90a7-f96b1e3a4d91.png)


## [`YSlow`](https://chrome.google.com/webstore/detail/yslow/ninejjcohidippngpapiilnmkgllmakh) - 网页加载检测报告
> YSlow analyzes web pages and suggests ways to improve their performance based on a set of rules for high performance web pages.
网页加载检测报告。非常详细，但是报告排版不是很容易看懂。比Lighthouse快

![image](https://user-images.githubusercontent.com/14041622/39408906-5a607ebc-4c10-11e8-8bec-bb246a927eda.png)



# 插件合集：网页加载优化

## [`Decentraleyes`](https://chrome.google.com/webstore/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj)

> 通过加载本地其事先加载好的资源，并拦截其他第三方的资源请求来加快网页加载速度，该插件还能在加快网页加载速度的同时还能减少一些跟踪脚本的跟踪功能以使得你的网络环境更加安全。

[参考文章](http://chromecj.com/productivity/2017-12/854.html)

![image](https://user-images.githubusercontent.com/14041622/39408585-3f3649c8-4c0b-11e8-9043-4f4834de86a3.png)


## [`Gooreplacer`](https://chrome.google.com/webstore/detail/gooreplacer/jnlkjeecojckkigmchmfoigphmgkgbip)

> 重定向/屏蔽 URL，修改/删除 headers. gooreplacer 最初为解决国内无法访问 Google 资源（Ajax、API等）导致页面加载速度巨慢而生，新版在此基础上，增加了更多实用功能，可以方便用户屏蔽某些请求，修改 HTTP 请求/响应 的 headers。

[中文官方介绍](https://github.com/jiacai2050/gooreplacer)
[使用语法指南](https://github.com/jiacai2050/gooreplacer/blob/master/doc/guides.md)

![image](https://user-images.githubusercontent.com/14041622/39408814-bce94480-4c0e-11e8-81f9-df25d0415ec7.png)

## [`AdBlock`](https://chrome.google.com/webstore/detail/adblock/gighmmpiobklfepjocnamgkkbiglidom)
> The most popular Chrome extension, with over 40 million users! Blocks ads all over the web.

ABP 不管是什么网页都会插入 14000 多条元素隐藏规则，所以占用内存很大.

![image](https://user-images.githubusercontent.com/14041622/39409037-601b1446-4c12-11e8-8dc2-21b84232a3fa.png)


## [`uBlock Origin`](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)

> uBlock Origin对比ABP有性能上的优势，其最为突然的性能优势就是其占用极低的内存和 CPU。有分析说adp主要靠的是屏蔽，而ublock Origin主要靠的是阻断，ABP的工作需要在所有网页插入屏蔽脚本和css，而uBlock Origin直接阻止需要屏蔽的内容进入当前网页。一般的拦截请求的规则大家都差不多，关键的是元素隐藏规则，uBlock 把它叫做修饰规则 cosmetic filters，ABP 不管是什么网页都会插入 14000 多条元素隐藏规则，所以占用内存很大，uBlock 插入的很少，因为他是在网页开始加载以后才判断需要用到哪些元素隐藏规则。所以才在性能上面要更加优越。

[AdBlock 对比 uBlock Origin](https://zhuanlan.zhihu.com/p/23188485)
[参考使用方法文章](https://www.jianshu.com/p/22a73602c2ed)

- (1)巨大的电源按钮：用于打开和关闭uBlock Origin按钮，蓝色开启/灰色关闭 。
点击巨大的电源按钮可以针对当前站点关闭 uBlock Origin，也就是将当前站点添加为 白名单，在你下次访问时仍会保留此状态。相对地，按住 Ctrl 并点击按钮只针对当前页面关闭 uBlock Origin（在 Mac下是按住command ⌘ 点击）
- (2)`闪电图标`：去除当前页面的元素。点击闪电图标可以进入元素去除器模式，在此你可以交互式地移除当前页面的一个或多个元素。不过这里移除元素始终是临时性的，也就是说页面重新载入后所移除的元素又将重新显示出来。
- (3)`元素吸管图标`：点击滴管图标可以进入`元素选择器模式`，在这里你可以交互地从页面选择元素并创建过滤规则来`永久移除该元素`。屏蔽元素按钮(用过ABP的都知道)
- (4)列表图标：网络请求日志(个人理解:网络请求记录监控中心)：可以按照网络资源查看/屏蔽的控制系统 。网络请求日志与开发工具的网络 不同之处在于，不单单可以查看网络资源，还可以屏蔽不想要的脚本等等之流 。你可以在浏览器里实时查看网络通信情况。提示：点击图标的同时按住 Shift 键可以切换选择是在新窗口还是新标签页中打开记录台。uBO 会在你未按 Shift 键打开记录台时记住你的选择。
- (5）禁止网页弹窗按钮，开启后，该网页永久无法弹窗 。默认情况下弹出窗口是允许显示的，除非有相应的过滤规则屏蔽。但如果开启该选项，不管规则如何，当前站点的所有弹出窗口都会被屏蔽：


![image](https://user-images.githubusercontent.com/14041622/39424881-526a465c-4cab-11e8-9c77-0eadd954ff91.png)


## [`Ghostery`](https://chrome.google.com/webstore/detail/ghostery-%E2%80%93-privacy-ad-blo/mlomiejdfkolichcflejclcbmpeaniij) - Privacy Ad Blocker

> Ghostery’s built-in ad blocker removes advertisements from a webpage to eliminate clutter so you can focus on the content you want.
Protect your privacy
Ghostery allows you to view and block trackers on websites you browse to control who collects your data. Enhanced Anti Tracking also anonymizes your data to further protect your privacy.
Browse faster
Ghostery’s Smart Blocking feature speeds up page loads and optimizes page performance by automatically blocking and unblocking trackers to meet page quality criteria.
Customize your display
Ghostery offers multiple displays and insights dashboards so you can see the information that’s relevant to you.

![image](https://user-images.githubusercontent.com/14041622/39408766-dd438cbe-4c0d-11e8-8f36-1ef6957bc9a6.png)


