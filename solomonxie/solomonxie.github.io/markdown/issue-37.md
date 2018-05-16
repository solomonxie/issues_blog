# Javascript 编码细节技巧
> 记录Javascript的基本语法和常用技巧，以及扩展库等等。


## 瞬间回想JS语法篇
> 有时候在各种语言间穿梭，时时会忘了这个东西的最基本语法区别，比如声明变量、循环、条件判断等。所以就需要在这里立个篇章专门说。

```javascript
// 注释单条语句
/* 注释块语句 */

// 声明变量
var a = 1;
var b = "hello", c = [];
var c = {}; // Object

// Json变量
var json = {
    "name": "jason",
    "skills": ["programming", "swimming"]
};

// 变量操作
[1,2,3] + "hello" == "1,2,3hello";

// 条件判断
if (true && true) { }
else if (1==1 || 2!=3) {}
else {}

// for循环
for (var i=0; i<arr.length; i++) {
    // 停止循环
    break;
    // 继续循环并跳过本次
    continue;
}
```


# 用过一些JS-Tree控件之后的总结 2007-12-14

[原文在此。](http://www.iteye.com/topic/148372)

    最近用了不少的javascript做的树控件，感受颇深啊，有些累了真的。可能是我的需求太多了吧，导致一些树控件根本无法满足要求……下面就简要的说一些树吧（作者：Zexombie,地址：zexombie.javaeye.com）
大概在google里搜了国内外的以下这些树（太次的不包括）：（作者：Zexombie,地址：zexombie.javaeye.com）
tmlx-Tree（作者：Zexombie,地址：zexombie.javaeye.com）
xytree（作者：Zexombie,地址：zexombie.javaeye.com）
mktree（作者：Zexombie,地址：zexombie.javaeye.com）
dtree（作者：Zexombie,地址：zexombie.javaeye.com）
MzTreeView1.0
Gurt Tree （作者：Zexombie,地址：zexombie.javaeye.com）
SilverStripe Tree Control（作者：Zexombie,地址：zexombie.javaeye.com）
Morten's JavaScript Tree Menu（作者：Zexombie,地址：zexombie.javaeye.com）
          dhtmlx-tree,鼎鼎大名，这就不用说了。功能巨全应有尽有(不过高级更能要付费滴)，API文档巨清楚。常用的比如“动态添加“、“xml读取”、“展开事件”、“用户自定义属性”等。但是缺点也是最让人不爽的——巨慢！我才从数据库里动态加载了一两百个节点，竟然要了我56秒！天啊快一分钟了！生成慢，就连你点击节点展开的响应速度也慢了，用习惯了dhtmlx-tree后，感觉别的什么速度都快了……（作者：Zexombie,地址：zexombie.javaeye.com）
      xytree,国内人做的，很精巧的几个文件，源代码及其清晰注释及其详细，用起来及其方便以及速度及其快，我从数据库中取出几百个几点只要16毫秒左右……呃，xytree不支持xml好像，只能“addNode()”，可以“动态添加”，还可以“自定义节点属性”。缺点呢，就是“不支持递归”和“展开事件”。“不支持递归”的意思就是在一般你从数据库中数据，在递归读取的过程中，你不能够一边读一边添加。这个原因呢不好解释，貌似一个bug，牵扯到你父子addNode()顺序的问题。呵呵不过逼于无奈我想了一招儿也能代替这个bug——像生成xml一样把所有代码都变成字符串形式，集合起来后统一进行eval()执行……（作者：Zexombie,地址：zexombie.javaeye.com）
      mktree呢，也叫dhtml-tree，相当爽相当简单！不用这个那个的，只要你有一定结构的这样的列表，只需赋予一个class名称，这个列表就变成一棵树了！mktree优点呢就是使用巨简单，速度巨快(因为简单没有一切乱七八糟的功能)。你可以看看那少得可怜的几行css代码还有那根手指头一样多的js函数，就知道这是一个多么纯粹的树了……缺点呢也是因为简单，样式上这棵树只有+/-这样的东西而没有我们常见的那种+/-旁边还有的文件夹icon，文字样式也只是普通文字形式。功能上呢除非你大动干戈去改代码，否则你无法“动态添加节点”，也没有“展开事件”，事实上如果你动动脑子钻个空子在某个tag上加一个onclick事件，你连点击事件都没有，树的链接可能也不好弄……呵呵不过这棵树还是配置了几个方法滴，比如展开/合并所有节点或单一节点，单一节点展开关闭你得自己找咯可没有文档给你啊……（作者：Zexombie,地址：zexombie.javaeye.com）
      Gurt Tree 样子上很一般，但是呢用起来相当奇怪！加载几千个节点只需十几毫秒（不从数据库取），样式上也还过得去。支持“多树”、“动态添加”等功能。但没发现“xml读取”或者“展开节点”功能。但是呢用法很奇怪代码不太好理解，主要定制的东西全部用一种奇怪的语法在一个tree_cfg.js里面自己去写，唉我还得现去分析，不爽……（作者：Zexombie,地址：zexombie.javaeye.com）
      dtree呢就没有上面那么极端了,是个不错的tree，中等。样式上还行用户自由度很大，可以轻松得改写css代码，js代码也可以轻松根据自己需要改写，不算太复杂。支持“动态添加”，“间接xml读取”，以及“点击事件”等，呵呵反正我觉得好多东西都得自己改源码才实现。因为这棵树是公司用的所以我也没太多计较。文档也还凑合吧。（作者：Zexombie,地址：zexombie.javaeye.com）
MzTreeView1.0。哇说起这个就比较厉害了！真的！强烈推荐这个。梅花雪大人也是“阅树无数”阿，然后吸取了经验，在速度算法和开发人员使用上都做了极大的改进啊！在他的api文档里面还提到了他制作这个tree的思想精髓部分，比如巧妙利用字符串与正则表达式的搭配来代替对象或数组，比如你生成一个节点只需这样写：tree.nodes["父节点id_本节点id"] = "text: 标题; url: #;"; 就这样一个完整的节点就生成了，一句话包括了添加节点、定义属性等所有事情，最适合从数据库中取出数据然后动态生成，因为你只需如上指明父节点和这个节点的id即可，而不用像其他tree那样还要层层嵌套递归循环来添加……样式上呢直接在你引用tree的页面中写style就可以了具体看文档吧。不好的地方可能是样式上自由度还不算太高因为接口不够全，xml数据形式好像还不支持，我想梅花雪大人会改进的。总结起来：简单易用、速度快、好看（至少不难看）、思路清晰、五脏俱全。（作者：Zexombie,地址：zexombie.javaeye.com）
      SilverStripe Tree Control也是一种像mktree那样读取的树，但是呢用起来就麻烦点了还需要定义很多的class名，我渴望从它这儿得到只要比mktree多点功能就好了，可是结果不尽人意，连个能看的文档都没有，一个页面写几句介绍的话就算混过去了，失败……顺便说一下，SilverStripe好像主要是做blog程序的，像wordpress一样的也是php的……      Morten's JavaScript Tree Menu，没得说了(因为也不知道说什么),看样子功能挺全的最起码不多不少，速度也挺快的。打开index.html就知道了，文档巨x全，半颗树都是API文档，只是看了那么一下，翻了一下它引用的文件，我到现在还没数清楚我一共需要引用多少个文件，一个节点需要写多少个参数才能生成……还不够累的呢，唉……（作者：Zexombie,地址：zexombie.javaeye.com）
     唉，也说了不少了，都是牢骚的话，希望有心人能吸取教训看到这些了，就别再走弯路了，看看自己的需求看看这些树的支持度，量力而行。注：这里面没有提及一个或两个著名的树控件以及著名的公司的树控件(比如ext、yui等巨慢语法巨罗嗦引用文件超多超大我就不说了)，我觉得没那么大必要，省了……（作者：Zexombie,地址：zexombie.javaeye.com）
    下面附件包括截图，以及控件文件。希望大家交流……（作者：Zexombie,地址：zexombie.javaeye.com）
