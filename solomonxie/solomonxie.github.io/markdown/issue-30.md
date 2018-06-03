# IDE Hubs 各种IDE使用技巧
> 如果涉及一些前端如HTML, css的话，说实话vim真的心有余力不足。\
就算有人说vim也可以做到而且可以做到更快，但是那就像用千斤重大刀去削苹果皮一样，可以做到，练到出神入化的地步也可以做到更好，
但是——没必要！明明有个超好用的小刀，焉用牛刀呢？

## 已收集IDE
- [x] Sublime Text
- [x] VScode


# Sublime Text 开启vim模式
在软件菜单里找到设置，会弹出Json格式的文件，也就是Sublime Text的配置文件。
对，Sublime任性，设置页坚决不用GUI显示，只用配置文件。
很简单，找到User 配置（`Preferences.sublime-settings`)这个文件，然后将`ignored_packages`数组中的`Vintage`数值删除即可，然后就变为Vim和Sublime模式通用了。如果再屏蔽vim模式，只要再将`Vintage`加回去该数组即可。
![image](https://user-images.githubusercontent.com/14041622/35902193-41f8dbe8-0c15-11e8-8834-34a0ec1f78e8.png)





# Sublime 安装插件方法
> 长期不用的话还真能忘，这里记一下吧。

### 安装包管理器 Package Control
要装插件的话，必须从`包管理器`中才行，所以要安装它。
网上到[`Package Control`官网](https://packagecontrol.io/installation)，复制一下最新的安装命令（很长很长很长的一句命令）：
```
import urllib2,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')
```
然后回到Sublime里面，从菜单里`view-show console`，打开终端，输入官网那句话回车，等一等，就安装成功了。
![image](https://user-images.githubusercontent.com/14041622/35406332-8df2f294-0243-11e8-8167-6d0a2bffe1dc.png)

安装成功后，按`Ctrl+Shift+P`就会弹出快捷命令菜单，然后输入`package control`搜索找到`Package Control: Install package`，回车，等一等，就会加载出一个最新的插件列表。
![image](https://user-images.githubusercontent.com/14041622/35406512-0ffc0794-0244-11e8-88c8-62117f81b0a3.png)
然后输入自己喜欢的插件就会安装好了，非常傻瓜式。


# Sublime 常用插件列表
可以直接参考几个文章链接。[15 Awesome Sublime Text Plugins For Web Development](https://tutorialzine.com/2016/10/15-awesome-sublime-text-plugins-for-web-development)。
- **Emmet** 用独特的输入方式超快生成批量的html和css语句,如图：
![sublime-text-3-the-git](https://user-images.githubusercontent.com/14041622/35424823-46abef32-0291-11e8-83b9-1fae77458472.gif)
- **SublimeRepl** 编辑器内置程序编译器，直接显示Python等程序结果。(说实话不是很好用，稍微复杂点就显示不好了）
- **SidebarEnhancements** 稍稍增强ST的侧边栏的功能
- **SublimeTmpl** 快速HTMl/CSS/JS/Python等模板
- **SublimeCodeIntel** 鼠标点到函数上，自动提供该函数的文件所在位置，可以点击进行跳转
![11-codeintel](https://user-images.githubusercontent.com/14041622/35424496-00f75eec-028f-11e8-9d9a-31d7f63d1edb.gif)
- **Minify** 将各种代码压缩并生成`.min`文件，包括js，python等多种
- **Placeholders** 为HTML快速生成"伪图片"
![9-placeholder](https://user-images.githubusercontent.com/14041622/35424546-656253d2-028f-11e8-8f42-8d39714cae36.gif)
- **TernJS** 自动补全变量、属性等。
![image](https://user-images.githubusercontent.com/14041622/35469295-10cfc51e-036d-11e8-8996-a282c86a9715.png)



## Emmet语法
> 能力强到细思极恐的地步。不光适配Sublime，还可以应用到Vim等各种编辑器中。它不光是一个插件，而是一种语法，一种思路。它能把复杂的事、重复性的事简单化。简单一句话，按下Tab键，就可以生成一段高度订制的代码，而且还保留源语句为参考，可读性可复用性强。

先看这段Emmet语句:
```html
label[for="参数a"]{ 显示标签 }>input[type="checkbox"][id="参数a"]+input[type="text"][for="参数a"]
# 按一下Tab键，就会生成:
<label for="参数a"> 
    显示标签 
    <input type="checkbox" id="参数a">
    <input type="text" for="参数a">
</label>
```

然后简单说下语法吧：
- `label>input` 生成label嵌套input的结构
- `label[属性1=值][属性2=值]` 生成带有属性和值的结构，属性名直接写，值要用引号
- `label{内容}` 生成标签中间的文字内容
- `input+input` 会生成两个同级的input标签
比较详尽的用法看这个链接：
[使用Emmet加速Web前端开发](https://www.w3cplus.com/tools/using-emmet-speed-front-end-web-development.html)
看这个动图：
![element-1](https://user-images.githubusercontent.com/14041622/35469207-a525be46-036b-11e8-9e30-f1219598eed2.gif)





# Sublime 的 Snippets 快捷片段
> Sublime等编辑器等Snippets是个利器，输入自定义的一个词，按一下Tab，立刻调出来一大片段准备好的内容。尤其是HTML等Web编程，非常好用。

[官网说明链接。](http://sublimetext.info/docs/en/extensibility/snippets.html)
方法如下：
1. 打开Sublime菜单Tool -> New Snippets. 最新Mac版的，是在Tool -> Developer -> New Snippets.
![image](https://user-images.githubusercontent.com/14041622/35609203-5e10550a-0697-11e8-9857-8a856833a09f.png)
2. 在弹出的XML格式文档中，找到<content>标签下的<![CDATA[...]]>标签中，把要生成的内容粘贴进来，比如一段HTML代码。
3. 解除下面的<tabTrigger>标签注释，在里面写一个`触发键`，越简单越好，比如hello。
4. [可选] 设置生效范围Scope。解除<scope>标签注释，填上目标文件种类的生效范围。这个不能随便写，需要对照[这个链接](https://gist.github.com/J2TeaM/a54bafb082f90c0f20c9)找到html, js等分别对应的scope码。或者更简单的是在目标文件里按`Ctrl+Alt+P`，就会弹出该文件的Scope码，把它填进<scope>标签即可。
5. 保存snippets文件到Sublime的User文件夹中，文件必须以`.sublime-snippet`结尾。而这个文件夹的位置，如果是Windows就直接在软件文件夹里找`User`文件夹即可，Mac的话在`/Users/用户名/Library/Application Support/Sublime Text 3/Packages/User/`这里。
6. 保存好以后，会及时生效，不用重启软件。


# Sublime 设置按Tab键输入4个空格（而非默认的一个Tab长度）
Tab还是Space之争，如Vim和Emacs之争一样是永无止境的。我是Space派，不过是希望按Tab出空格的那种。
找到Sublime菜单的设置-User设置，在出现的JSON格式配置文件中，加入如下参数：
```javascript
"tab_size": 4, // Tab长度
"translate_tabs_to_spaces": true, // 每次按tab都会变成上面指定长度的space
```
设置如图：
![snip20180207_57](https://user-images.githubusercontent.com/14041622/35902757-6a40bc7c-0c17-11e8-981a-524ec970a69d.png)





# Sublime 的 Vim模式下无法长按键
vim上下移动，经常要长按某一个键，但是Sublime默认不支持vim下的长按，按多久也只生效一次。
解决很简单，
1. 必须先关闭Sublime
2. 在系统终端里输入修改Sublime的代码：
```
# Sublime 3的话是这个
defaults write com.sublimetext.3 ApplePressAndHoldEnabled -bool false

# Sublime 2的话是这个
defaults write com.sublimetext.2 ApplePressAndHoldEnabled -bool false
```

参考这个系统设置的其它设置，看[这篇文章](https://zhuanlan.zhihu.com/p/20234659)。


# VScode
> VS Code 叫 "Visual Studio Code"，但是完全不同于"Visual Studio"，可以不用害怕。实际上相当轻量、可定制、好看。被称为`The last editor you'll ever need`.

[参考Youtube：VS Code: The Last Editor You'll Ever Need](https://www.youtube.com/watch?v=anvYeA1pWlk)

安装极其简单，Mac上下载好文件后，直接双击运行就ok了。

![硅谷第五季截图](https://user-images.githubusercontent.com/14041622/40292967-09e76e30-5d01-11e8-8347-e05a25eb71d0.png)
硅谷第五季截图

## 更改下面状态栏status bar的颜色
vscode界面设计可以说相当出彩。唯一违和的地方就是状态栏的颜色。所以我第一件事就是查清楚怎么改它的颜色。

非常简单，只要修改用户配置文件即可。
Mac上，直接在IDE中`Ctrl+,`打开用户配置文件，在适当位置加入下面这段话：
```js
"workbench.colorCustomizations": {
    "statusBar.background" : "#1A1A1A",
    "statusBar.noFolderBackground" : "#212121",
    "statusBar.debuggingBackground": "#263238"
}
```
完成。
![image](https://user-images.githubusercontent.com/14041622/40293113-e472c3d8-5d01-11e8-8fa0-97304cb04413.png)

## 推荐颜色主题：

### `Cobalt2`
![image](https://user-images.githubusercontent.com/14041622/40586949-7a3b3a00-61fb-11e8-908f-947f444bec44.png)



# VSCode为Python配置Debug调试(virtualenv环境)
因为python自身的版本原因，环境是个非常重要的因素。我们经常需要多种环境，所以必须要配置好才能在vscode里面进行调试和运行。

vscode会在每个项目文件夹下创建一个`.vscode`文件夹，保存当前项目的运行环境的配置文件。
主要有三个：
- `.vscode/launch.json`
- `.vscode/tasks.json`
- `.vscode/settings.json`

这两个文件可以自己手动创建，也可以在菜单里选择让软件来创建。

## `launch.json`
打开菜单：`Debug -> Open Configurations`，如果没有则选择创建，然后进入`launch.json`的编辑。
内容较多，搜索`pythonPath`，找到对应的变量，把内容改为你的python环境地址。如：
![image](https://user-images.githubusercontent.com/14041622/40459385-a1a791e4-5f33-11e8-941b-c57aeb1197ea.png)


## `tasks.json`
打开菜单：`Tasks -> Configure tasks`，没有则选择创建一个，然后进入`tasks.json`的编辑。
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "python",
            "type": "shell",
            "command": "输入你的python运行地址，本机或虚拟环境的都行：如.venv/bin/python",
            "args": [
                "${file}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": [
                "$eslint-compact"
            ]
        }
    ]
}
```

## `settings.json`
在软件左下角状态栏中有选择环境的按钮，选择以后，就会自动生成`.vscode/settings.json`。如果没有，自己创建一个也行。打开文件进入编辑：
找到`Workspace settings`一栏，修改如下变量：
```
"python.pythonPath": "输入你的python运行地址，本机或虚拟环境的都行：如.venv/bin/python"
```


# VS code 隐藏一些文件
Vim等编辑器经常会产生`.swp`等缓存文件，所以在Vs code的文件菜单里面显示很不好看。
隐藏很简单。
只要到本地项目文件夹的`./.vscode/settings.json`里面修改以下位置内容即可：
![image](https://user-images.githubusercontent.com/14041622/40784328-f3ddfaae-6517-11e8-80d6-d31e9da47791.png)

名称匹配的大概语法是
```json
# 屏蔽文件
"**/*.swp"

# 屏蔽文件夹
"**/folder"
```


# VScode为Python添加Debug调试环境(Pipenv)
是时候更新virtualenv环境为pipenv环境了，比较方便。但是vscode中配置就麻烦了一点。

[参考：使用VS Code调试Python代码](https://plytools.github.io/2017/04/29/VSCode-Debug-Python/)

还是主要配置这三个文件让python正常的在vscode中达到差错、调试、运行的功能：
- `settings.json` 当前工作环境的所有配置
- `launch.json` 设置python的调试功能
- `tasks.json` 一般用不到。是设置python在vscode中Run运行的配置


## `settings.json`
vscode管理项目文件夹最重要的配置文件。
需要配置的变量有两个：`python.venvPath`用来指定pipenv存放虚拟环境的文件夹（不是这个repo的bin文件夹）；`python.pythonPath`用来指定具体执行`python`命令的位置。如下所示：
```json
    "python.venvPath": "/Users/Jason/.local/share/virtualenvs",
    "python.pythonPath": "/Users/Jason/.local/share/virtualenvs/repository-QDdBvXzX/bin/python"
```

## `launch.json`
如果在项目文件夹中的`.vscode/`中存在这个文件，那么就直接编辑。如果不存在，则需要在vscode的左侧栏的`Debug`栏目中，点击代表`设置`的小按钮，创建一个`launch.json`。然后点击`add configuration`，输入`python`，根据提示创建python相关的配置行。

打开文件以后，主要需要修改的内容如下：
- 找到`pythonPath`变量，可以用两种方式修改其内容：
    - 使用`settings.json`里配置的python位置：`"pythonPath": "${config:python.pythonPath}"`
    - ~指定python的绝对路径~，不推荐。`"pythonPath": "/Users/Jason/.local/share/virtualenvs/test-venv/bin/python"`。

编辑好后，vscode会提示你安装`pylint`的python包，确定后它会自动用`pip install pylint`安装到你指定的python环境里，这样它就可以随时检查你的文件语法错误了。




# Vscode 的vim模式无法持续按键
默认下，Mac上的vscode进入vim模式后，一直按住h, l, j, k等键，无法持续移动。
虽然在mac的vim里和sublime text里都没问题，但这不是vscode的问题，而还是mac的问题。

[参考：How do I press and hold a key and have it repeat in VSCode?](https://stackoverflow.com/questions/39972335/how-do-i-press-and-hold-a-key-and-have-it-repeat-in-vscode/44010683#44010683)

试着在终端里面输入以下命令关闭Mac的该功能：
```sh
# Disable Mac's "Press&Hold" feature
$ defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false
```
如果要恢复的话，再用这句：
```sh
# Re-enable this feature
$ defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool true
```

 然后重启vscode就可以了。


# Sublime text 记住上次打开的文件
有些人希望每次关闭Sublime text都自动消除记忆，下次打开时什么都不显示。
但我觉得那样不太方便，尤其在做常用项目都时候。
默认是不显示的，所以我需要让它每次打开都显示上次打开的文件或文件夹。

在菜单里找到`preferences -> Settings-User`，或者mac上直接`cmd+,`，打开用户设置的JSON文件，
加入以下变量内容：
```json
"hot_exit": true
```
保存后即生效。