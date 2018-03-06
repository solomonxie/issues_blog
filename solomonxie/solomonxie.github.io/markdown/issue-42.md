# API 数据操作实践
> 目前是操作Github API获取自己的repo和issues数据，然后还会研究bitbucket等各种各样的网站API


# Github API 文档学习
[v3版API的文档链接](https://developer.github.com/v3/)
[v3版API的官方教程](https://developer.github.com/v3/guides/getting-started/)

## 基本访问路径 (Root Endpoints)
一开始读文档的时候，照着它的事例直接在命令行里`curl`，或者在InSomnia或Postman软件里访问，都完美显示200状态。可是一旦把链接里改写成自己的用户名就各种显示404无页面。还以为是授权问题，然后在页头HEADER中按照各种方式试了username和token密钥，都没用还是404。结果发现，原来不是方法的问题，纯粹是链接地址没写对！
`实际上只是读取的话，完全不用任何授权`，可以在命令行、Insomnia、网页等各种情况下直接输入链接访问任何人的所有公开信息。
然后对照[官方路径列表Root Endpoints](https://api.github.com/)得到的链接，好像怎么访问都不对。反而在Stackoverflow中看到的一个链接，顺藤摸瓜自己发现了各种正确的访问路径，总结如下：
- 首先！访问的链接最后不能有`/`。如`https://api.github.com/users/solomonxie`是可以访问到我个人信息的，但是`https://api.github.com/users/solomonxie/`就不行了，唯一不同是多了一个`/`.
- 其次！不同于一般URL访问，GIthub的API访问链接是`区分大小写`的！
- 个人主要信息。 `https://api.github.com/users/用户名`,得到数据如下图：
![image](https://user-images.githubusercontent.com/14041622/35799473-cc7cd7e0-0aa0-11e8-89bd-5f8e8150fa02.png)
- 个人所有repo。`https://api.github.com/users/用户名/repos`。会得到一个repo的JSON格式列表。
- repo详细信息。`https://api.github.com/repos/用户名/仓库名`。repo的路径就开始和个人信息不同了。
- 获取某个repo的内容列表。`https://api.github.com/repos/solomonxie/gists/contents`，注意这只会返回根目录的内容。
- 获取repo中子目录的内容列表。`https://api.github.com/repos/solomonxie/gists/contents/目录名`。一定要注意这里一定要完全遵循原文件名的大小写，否则无法获得信息。如果是更深层的内容，则在链接列按照顺序逐级写上目录名称。
- 获取repo中某文件信息（不包括内容）。`https://api.github.com/repos/solomonxie/gists/contents/文件路径`。文件路径是文件的完整路径，区分大小写。只会返回文件基本信息。
- 获取某文件的原始内容（Raw）。1. 通过上面的文件信息中提取`download_url`这条链接，就能获取它的原始内容了。2. 或者直接访问：`https://raw.githubusercontent.com/用户名/仓库名/分支名/文件路径`
- repo中所有的commits列表。`https://api.github.com/repos/用户名/仓库名/commits`。
- 某一条commit详情。`https://api.github.com/repos/用户名/仓库名/commits/某一条commit的SHA`
- issues列表。`https://api.github.com/repos/用户名/仓库名/issues`。
- 某条issue详情。`https://api.github.com/repos/用户名/仓库名/issues/序号`。issues都是以1,2,3这样的序列排号的。
- 某issue中的comments列表。`https://api.github.com/repos/用户名/仓库名/issues/序号/comments`。
- 某comment详情。`https://api.github.com/repos/用户名/仓库名/issues/comments/评论详情的ID`。其中评论ID是从issues列表中获得的。

## 查询参数 (Parameters)
如果在上面基本链接中加入查询条件，那么返回的数据就是filtered，过滤了的。比如要求只返回正在开放的issues，或者让列表数据分页显示。常用如下：
- 分页功能。格式是`?page=页数&per_page=每页包含数量`。
如`https://api.github.com/users/solomonxie/repos?page=2&per_page=3`
- issues状态。格式是`?state=状态`。
如`https://api.github.com/repos/solomonxie/solomonxie.github.io/issues?state=closed`

## 权限认证 Authentication
> 首先需要知道都是，到此为止之前所有都查询都是不需要任何权限的，给个地址就返回数据，全公开。
但是创建文件、更新、删除等就是必须用自己的账号"登录"才能实现的。所以为了下面的增删改做准备，需要先看一下权限问题。
官网虽然写的很简答，不过如果不熟悉API的话还是不能马上就理解。

常用的认证方法有三种，`Basic authentication`, `OAuth2 token`, `OAuth2 key/secret`
三种方法效果一样，但是各有其特点和方便之处。选哪种就要看自己哪种方便了。

### 认证方法一：Basic authentication
这种最简单，如果是用curl的话，就：
```
curl -u "用户名:密码" https://api.github.com
```
如果是用Insomnia等api调试工具的话，直接在Auth选项栏里选Basic Auth，然后填上用户名密码即可。

### 认证方法二：OAuth2 token
#### 关于token
> 这种token方式，说实话如果不是操作过API或深度了解REST的话，是很难理解的东西。
说白了就是`第二个密码`，你既不用到处泄露自己的用户名密码，又可以专门给这个"第二密码"设置不同需要的权限，如有的只可读有的还可以写等。而且这个“第二密码”是既包括用户名又包括密码功能的，全站只此一个绝对不会和别人重复。初次之外，你还可以设置很多个token，也就是第三、第四、第五...密码。很方便。

#### 设置token方法
就位于github个人账号设置->开发者设置->个人token里。创建一个新token时，可以选择具体的权限，创建成功时一定要复制到本地哪里保存，只会让你看见一次，如果忘记的话就需要重新生成（其实丢了也不算麻烦）。
![image](https://user-images.githubusercontent.com/14041622/36475101-a0745628-1734-11e8-9393-829813c2f6e3.png)

另外！注意：
> token字符串不能存储在github的repo中，经过测试，一旦提交的文件中包含这个token字符串，那么github就会自动删除这个token -_-! 我用了很久才明白过来，创建的Personal Access Token总是自动消失，还以为是有时限的。

#### 用token通过权限认证
有两种传送方法，哪种都可以：
1. 作为url中的参数明文传输：
```
curl https://api.github.com/?access_token=OAUTH-TOKEN
```
2. 作为header中的参数传输：
```
curl -H "Authorization: token OAUTH-TOKEN" https://api.github.com
```
如果不是用curl而是Insomnia测试的话，和上面basic auth是大同小异的，很容易操作就不复述了。
到此为止，权限认证就算搞清了，而且也实际验证过有效了。强烈建议用insomnia工具操作，有GUI界面方便理解，成功后再转为curl或python等程序语言。

### 认证方法三：OAuth2 key/secret
这个是除了Personal Access Token之外的另一种好用的方法，即创建自己的OAuth app，然后得到一对`client_id`和`client_secret`。如下：
![image](https://user-images.githubusercontent.com/14041622/36474687-3e2ac3e0-1733-11e8-9fff-1d7a8f52e9cc.png)
![image](https://user-images.githubusercontent.com/14041622/36474746-6ac5d8fe-1733-11e8-9789-64cf8d1a5c14.png)
得到这两个值之后，直接在访问任何api的url连接后面显性加上这两个参数即可完成认证，如：
`https://api.github.com/users/yourusername?client_id=YOUR-CLIENT-ID&client_secret=YOUR-CLIENT-SECRET`
但是：
> 目前这种认证方式**不支持**查询以外的操作，也就是只能GET获取某些api信息，不能执行request里的任何PUT/PATCH/DELETE操作。


## 创建新文件 Create content
> [Contents操作 官方文档](https://developer.github.com/v3/repos/contents/#get-contents)

- 传输方法：`PUT`
- 访问路径：`https://api.github.com/repos/用户名/仓库名/contents/文件路径`
- JSON格式：
```javascript
{
  "message": "commit from INSOMNIA",
  "content": "bXkgbmV3IGZpbGUgY29udGVudHM="
}
```
JSON填写如下图：
![image](https://user-images.githubusercontent.com/14041622/35808306-59661422-0ac0-11e8-8c35-55afa4f533c9.png)
- 注意：1.必须添加权限验证（上面有写） 2. 数据传送格式选择JSON 3. 文件内容必须是把文件整体转为Base64字符串再存到JSON变量中 4. 文件路径中如果有不存在的文件夹，则会自动创建


起初不管怎么尝试都一直报同样都错误，400 Invalid JSON，如下图：
![image](https://user-images.githubusercontent.com/14041622/35806800-b6fc8170-0abb-11e8-997e-f69b19698d06.png)

最后发现原来是犯了很小很小都错误才导致如此：
![image](https://user-images.githubusercontent.com/14041622/35806838-dc8adedc-0abb-11e8-8d8a-c0d0b32ebe58.png)
原来，我的token看似是正常的，唯独错误的是，多了一个空行！也就是说，标明都是invalid JSON，结果没注意竟然是invalid Token!

增加文件成功后返回的消息：
![image](https://user-images.githubusercontent.com/14041622/35807261-30b29d8c-0abd-11e8-8d61-723a9886441a.png)


## 更新文件 Update content
> 主要这几点： 1. 传送方式用`PUT` 和创建文件一样 2. 需要权限验证，3. 传输内容数据用JSON 4. 需要指定该文件的SHA码 4. 路径和访问content时一样 5. 文件内容必须是把文件整体转为Base64字符串再存到JSON变量中

- 传输方法：`PUT`
- 访问路径：`https://api.github.com/repos/用户名/仓库名/contents/文件路径`
- JSON格式：
```javascript
{
  "message": "update from INSOMNIA",
  "content": "Y3JlYXRlIGZpbGUgZnJvbSBJTlNPTU5JQQoKSXQncyB1cGRhdGVkISEhCgpJdCdzIHVwZGF0ZWQgYWdhaW4hIQ==",
  "sha": "57642f5283c98f6ffa75d65e2bf49d05042b4a6d"
}
```
- 注意：必须指定该文件的`SHA码`，相当于文件的ID。
## `SHA`虽然是对文件的唯一识别码，相当于ID，但是它是会随着文件内容变化而变化的！所以必须每次都重新获取才行。
至于获取方式，验证后发现，目前最靠谱的是用前面的`get content`获取到该文件的信息，然后里面找到`sha`。

对上传时的JSON格式另有要求，如果没有按照要求把必填项输入，则会出现422错误信息：
![image](https://user-images.githubusercontent.com/14041622/35807463-d447ec7c-0abd-11e8-8d17-742052321128.png)

或者如果用错了SHA，会出现409错误消息：
![image](https://user-images.githubusercontent.com/14041622/35807736-97e5feee-0abe-11e8-8e9b-5f9bb6576a7f.png)

如果正确传送，就会显示200完成更新：
![image](https://user-images.githubusercontent.com/14041622/35807698-77cf55d8-0abe-11e8-9677-59f2961b5b0f.png)

## 删除文件 Delete content
- 传输方法：`DELETE`
- 访问路径：`https://api.github.com/repos/用户名/仓库名/contents/文件路径`
- JSON格式：
```javascript
{
  "message": "delete a file",
  "sha": "46d2b1f2ef54669a974165d0b37979e9adba1ab2"
}
```

删除成功后，会返回200消息：
![image](https://user-images.githubusercontent.com/14041622/35809967-2c095124-0ac5-11e8-84e3-d55117ed0709.png)

## 增删改issues
> 如果做过了上面文件的增删改，这里大同小异，不同的访问路径和JSON的格式而已。唯一不同的是，issues是不用把内容转为Base64码的。

参考链接：[github官方文档](https://developer.github.com/v3/issues/#create-an-issue)

### 增加一条issue
- 传输方法：`POST`
- 访问路径：`https://api.github.com/repos/用户名/仓库名/issues`
- JSON格式：
```javascript
{
  "title": "Creating issue from API",
  "body": "Posting a issue from Insomnia"
}
```
- 注意：issue的数据里面是可以加label，milestone和assignees的。但是必须注意milestone和assignees必须是已有的名次完全对应才行，否则无法完成创建。

### 更改某条issue
- 传输方法：`PATCH`
- 访问路径：`https://api.github.com/repos/用户名/仓库名/issues/序号`
- JSON格式：
```javascript
{
  "title": "Creating issue from API ---updated",
  "body": "Posting a issue from Insomnia \n\n Updated from insomnia.",
  "state": "open"
}
```
- 注意：如果JSON中加入空白的labels或assignees，如`"labels": []`，作用就是清空所有的标签和相关人。

### 锁住某条issue 
不允许别人评论（自己可以）
![image](https://user-images.githubusercontent.com/14041622/35862570-22025a00-0b87-11e8-9077-23c09fd5a094.png)

- 传输方法：`PUT`
- 访问路径：`https://api.github.com/repos/用户名/仓库名/issues/序号/lock`
- JSON格式：
```javascript
{
  "locked": true,
  "active_lock_reason": "too heated"
}
```
- 注意：active_lock_reason只能有4种值可选：`off-topic`, `too heated`, `resolved`, `spam`，否则报错。
另外，成功锁住，会返回`204 No Content`信息。

### 解锁某条issue
- 传输方法：`DELETE`
- 访问路径：`https://api.github.com/repos/用户名/仓库名/issues/序号/lock`
- 无JSON传输




## 增删改comments
> 参考[官方文档](https://developer.github.com/v3/issues/comments/#create-a-comment)


### 增加comment
- 传输方法：`POST`
- 访问路径：`https://api.github.com/repos/用户名/仓库名/issues/序号/comments`
- JSON格式：
```javascript
{
  "body": "Create a comment from API"
}
```

### 更改comment
- 传输方法：`PATCH `
- 访问路径：`https://api.github.com/repos/用户名/仓库名/issues/comments/评论ID`
- JSON格式：
```javascript
{
  "body": "Create a comment from API \n\n----Updated"
}
```
- 注意：地址中，issues后不用序号了，因为可以通过唯一的`评论ID`追查到。查看评论ID的方法，直接在上面查询链接中找。

### 删除comment
- 传输方法：`DELETE `
- 访问路径：`https://api.github.com/repos/用户名/仓库名/issues/comments/评论ID`
- 无传输数据


# 先留一个空位介绍API调试客户端Insomnia和Postman


# Insomnia 客户端添加插件
Insomnia是带我入门API且我认为最棒最棒的入门工具，正如其标语: `Debug APIs like a human, not a robot`. 不过在接触更多的API时，会发现有些不便利，比如百度翻译api的权限验证需要各种随机码和MD5，github的api需要文件的base64等。Insomnia本身暂时不具备这么多功能。所以需要给它安装插件。
安装方法很简单，不需要在命令行通过npm安装插件，直接在界面GUI里输入插件名即可下载安装。
![image](https://user-images.githubusercontent.com/14041622/35841980-438ccce8-0b3a-11e8-8c1e-1cda921a454d.png)

## 常用插件
- `insomnia-plugin-randomnumber` 生成随机数，只要在`enviroment`中输入random就会自动提示，并调用随机函数。



# Postman和Insomnia客户端的代理设置
试用过百度api后才知道，这种服务商竟然还要求指定的ip地址才能获取数据。必须现在百度后台设定好一个ip，然后用这个ip才能访问它的api。可是我发现我自己本机每次访问，它都会告诉我地址在变化。所以只能用我在租用的服务器访问了。
可是在服务器端访问，只能通过命令行，也就是curl访问，比较麻烦，需要从postman里面复制出来再粘贴过去才行。后来发现原来postman是可以直接设置代理的（只不过是软件全局代理，而不是为每个项目设置）

### 怎么为软件设置代理
因为回国后也一直在用Spotify听歌，所以必须用代理，研究了下才明白过来怎么使用。首先必须这个软件自备代理设置，然后你在里面输入（本机）代理的ip地址和端口即可。注意，是本机的ip和端口，而不是代理服务器的ip和端口！
只是，如果用的是shadowsocks代理，则需要软件支持socks代理才行，这两款api工具都不具备，只能用http和https代理。所以，如果要实现，还需要用单独软件将本机数据从socks转发到http端口才可以。
网上有很多解决socks->http方案。只是如果这么麻烦，就还不如从服务器直接访问了。



# Postman 脚本语法总结
> Postman的强大之处在于其允许在对某一个request访问的之前和之后分别运行自定义的一段Javascript脚本，这样直接就完成了一个`chain request`的效果，可以将数条request连结成一个流程完成一体化测试。这在很多的API操作中都是极其有用的，所以这里有必要总结一些常用语句。

## 脚本执行流程
![image](https://user-images.githubusercontent.com/14041622/35856198-39f1e052-0b70-11e8-80e4-08341126a2b1.png)
- `pre-request`脚本，是在对API进行请求之前的脚本，一般用于动态生成参数、JSON数据包、链接地址等。
- `test`脚本，其实更应该叫`post-request`，实在完成API访问并得到其response回应之后运行的脚本，一般用于获取response的内容，用于之后对于别的资源的请求，如获取页面标题和内容等。

## 运行脚本要求
需要注意，`pre-request`脚本，在里面直接写代码就可以了，但是`test`脚本需要在某个指定的函数`pm.test(...)`中执行才会被识别，且作为`test`脚本运行。如下图：
![image](https://user-images.githubusercontent.com/14041622/35856475-0d0ab400-0b71-11e8-8cda-fdb966b7803d.png)
`pm.test()`中第一个参数是测试描述(会在测试结果栏显示，应和其它测试描述做以区分)，第二个参数是一个函数，具体执行代码都在这个函数中运行。
另外，`pm`对象是Postman的主要对象，所有的内置函数，数据调用等，都需要通过它来实现。

## 脚本调试
如果要看已经设置的Enviroment变量的话，可以点开右上方小眼睛看到，如下图，我设置了3个环境变量：
![image](https://user-images.githubusercontent.com/14041622/35856730-d226466e-0b71-11e8-9d3a-849d4886044a.png)

调试时要打印的话，一般都是用`console.log(...)`，这样就能在console中看到。
如果你的Postman是Chrome app的话，直接在chrome浏览器的开发者工具里调试就行。如果是Mac等桌面软件，则需要打开内置的console才能看到调试信息。位置在左下角，如下图：
![image](https://user-images.githubusercontent.com/14041622/35856605-7ec4f15a-0b71-11e8-8167-a4d7e52ca206.png)

## 常用语句 Code Snippets
一般会在脚本编写栏的右边都会有常用语句片段，点击以下就会出来代码，但是一开始不太了解的话点出来其实也看不懂。如下图：
![image](https://user-images.githubusercontent.com/14041622/35859452-15026d7e-0b7b-11e8-9e91-2f131e6223f5.png)

官方文档解释的各种函数调用链接在这里：[Postman Sandbox](https://www.getpostman.com/docs/postman/scripts/postman_sandbox)

以下是我自己总结的常用代码片段：
```javascript
// 获取response返回内容
var rsb = responseBody; // 是字符串格式

// 获取环境变量
var v = pm.environment.get("变量名称");

// 设置环境变量 只能存储字符串，如果是对象的话则无法在下次运行时获取到内容
// 如需要存储JSON数据，可以用JSON.stringify(..)存储，再用JSON.parse(..)转化为对象使用
pm.environment.set("变量名称", 变量内容);

// 清除某个环境变量
pm.environment.unset("环境变量名");

// 获取全局变量和普通变量
var gb = pm.globals.get("全局变量名");
var nm = pm.variables.get("普通变量名");

// Javascript 获取变量类型
console.log( typeof pm.enviroment );
```

## 测试结果
除了上面的具体功能代码外，经常还需要返回一个结果，告诉Postman这个测试结果是Pass还是Fail，默认是pass。

这里返回值就不是简单的return语句可以，必须要通过Postman自带的对象或方法才可以，一般是通过`pm.expect()`或`tests[]`这两个地方返回测试结果。

这些方法名看起来都很容易理解，一般都会叫`pm.expect()`或`.to.be()`或`.to.have()`这样的，字面意思就是期待什么或要求它必须是什么或必须有什么，才能通过测试。
另外，同样的测试结果，实际上还有更简单的写法，即不通过`pm`对象，而是内置`tests`对象，常用操作如下：
```javascript

# 反应时间必须少于200毫秒
tests["Response time is less than 200ms"] = responseTime < 200;

# 判断反应代号是否等于某一个指定的代号
tests["Status code name has string"] = responseCode.name.has("Created");

```
看这个用法，猜测`tests`是一个JSON格式的对象，`tests[...]`括号内的字符串是测试的描述， `=`后面是判断语句，然后将True或False赋予为`tests[..]`的值，然后postman轮训所有`tests`对象里的参数，并返回pass与否的结果。

这里是官方总结的常用测试脚本方法：[Test examples](https://www.getpostman.com/docs/postman/scripts/test_examples)

以下是我总结的常用的返回测试结果的内置函数：

```javascript
# “期待”返回结果必须包含某一段内容
pm.expect(从response里获取的字符串).to.include("必须包含的内容");

# 返回body值必须完全等于某一段内容
pm.response.to.have.body("必须等于的内容");

# 反应时间必须少于200毫秒
pm.expect(pm.response.responseTime).to.be.below(200);

# 必须返回某一个状态 如"Created"
pm.response.to.have.status("状态名");

```

![image](https://user-images.githubusercontent.com/14041622/35860402-deba93c8-0b7e-11e8-8d81-310873a64d63.png)





# Github API 访问次数限制

[参考官方说明](https://developer.github.com/v3/#rate-limiting)

如果没有任何授权直接访问的话，单IP限制每小时60次requests。如果有授权的话，每小时5000次。
![image](https://user-images.githubusercontent.com/14041622/36171363-5351c5a8-113d-11e8-9134-26f50844efd1.png)

通过官方介绍，我们可以在response返回的headers中获取`X-RateLimit-Remaining`和`X-RateLimit`来查看当前剩余的访问次数和当前的每小时限次。

![image](https://user-images.githubusercontent.com/14041622/36188652-53291c34-1188-11e8-89ec-6501c26c5563.png)




# Markdown中插入数学公式
以下方法：
- Google Charts API（根据url地址返回公式图片）
- [Forkosh](http://www.forkosh.com/mathtex.html)（根据url地址返回公式图片）
- [Codecogs](https://latex.codecogs.com/)  （根据url地址返回公式图片）
- MathJax 引擎（引入js文件渲染markdown中LaTex公式）

## Google Charts API 制作数学公式图
都知道Markdown中插入公式不易，需要平台自己提供LaTex渲染引擎。
如果是自己的平台倒还好说，很简单引入一个js文件即可。
但是Github的README和issues等都默认是不支持LaTex的，也不能插入外部js文件。
所以在Github中显示正常的公式唯一的方法就是引用公式的图片。
目前最流行的是Google Chart API和Forkosh服务器，但是forkosh服务器连接不畅，除非自己架服务器搭建forkosh平台，否则就只能选google了。

[参考文章。](https://www.jianshu.com/p/888c5eaebabd)

用法如下：

```
![](http://chart.googleapis.com/chart?cht=tx&chl= 在此插入Latex公式)
```
注意：公式虽然是LaTex语法，但是特殊符号必须经过url编码才行，否则Github不显示。
例：
```
https://chart.apis.google.com/chart?cht=tx&chf=bg,s,FFFF00&chl=%0D%0A4x_0%5CDelta%28x%29%2B3%5CDelta%28x%29%2B2%5CDelta%28x%5E2%29%3E0%0D%0A
```
![formula](https://chart.apis.google.com/chart?cht=tx&chf=bg,s,FFFF00&chl=%0D%0A4x_0%5CDelta%28x%29%2B3%5CDelta%28x%29%2B2%5CDelta%28x%5E2%29%3E0%0D%0A)


## Codecogs 制作数学公式
相比Google来说，Codecogs采用了一样的url引用方式，一样的语法，且也必须是url编码。但是Codecogs提供了一个网页编辑器，可以直接在上面可视化编辑公式，然后直接拷贝图片链接即可，所见即所得，要快捷的多了。
当然如果在意服务器稳定性还是想用Google的话，那还可以把图片链接前面直接改成Google api的地址即可。

![image](https://user-images.githubusercontent.com/14041622/37030346-9e91bc2e-2175-11e8-997a-234be6a543c6.png)

生成好图片后，直接右键点击生成的图片获取链接即可。