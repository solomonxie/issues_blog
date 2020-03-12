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
