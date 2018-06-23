# CSS 外观经验
> 主要记录点css的语法和技巧


## CSS 选择器
参考这篇: [https://www.w3schools.com/cssref/css_selectors.asp](https://www.w3schools.com/cssref/css_selectors.asp)
基本的有：
- `.class` 选择所有这个类
- `#id` 选择该ID
- `tag` 选择所有该标签
- `tag, tag` 选择该标签和同级标签
- `tag tag` 选择该标签下的某标签


## 元素独占一行
一般`div`是默认独占一行的，如果想要让`label`, 'span`等非默认独占一行的元素也达到效果，就需要改其css的`display`属性为`block`。
详解display的各项值区别和原理，参考这篇文章：[https://segmentfault.com/a/1190000000654770](https://segmentfault.com/a/1190000000654770),
常用的display值有：常用的display属性值有：
- `inline` 与其它元素同行显示
- `block` 独占一行
- `inline-block` 不独占一行且可以设置宽高
- `none` 不保留元素本该显示的空间
