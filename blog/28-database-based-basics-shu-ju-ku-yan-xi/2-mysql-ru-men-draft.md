# ❖ MySQL 入门 [DRAFT]

[`▶参考：CyC2018/CS-Notes/MySQL`](https://github.com/CyC2018/CS-Notes/blob/master/notes/MySQL.md)

## RDBMS

RDBMS的全称是：`Relational Database Management System`.

关系型数据库是建立在`关系模型`上的。所谓的关系模型，其实就是一大堆独立的表格，通过一个id关联起来的`表格库`，也就是->`关系型数据库`。

常见的关系型数据库有：
- Oracle (重量级)
- MS SQL Server
- MySQL (中轻量)
- Sqlite (极轻量单文件)

常见的非关系型(NoSQL)数据库：
- MongoDB
- Redis


## 存储引擎 Engine

MySQL中，可以选择每种数据库使用什么Engine处理引擎，而每种Engine能够计算、处理的事情会有不同。

MySQL常用的引擎有：
- `InnoDB`
- `MyISAM`

一般都是选择默认的`InnoDB`，因为它支持`事务处理`、`外键`、`行级锁`。但是`MyISAM`都不具备，所以它一般只在小项目里能用。
而`MyISAM`能够达到99.99%的稳定性和高可用性，并且具备高可扩展性，所以也比较流行。

其中，`行级锁`相对于`表级锁`，是指在多端同时操作数据库时，能以row为单位锁住一条信息，同一时间只允许一人操作这一行。

总而言之：
- MyISAM强调性能，速度远高于InnoDB
- InnoDB支持的数据处理方式比较多
- MyISAM的数据和索引是分开的，所以占用内存小。相比下InnoDB内存占用率远高于MyISAM。
- 如果是GB／TB级的数据，在面对SQL误操作下，MyISAM能够极快的挽救(因为读写速度)，但InnoDB则表示很难支撑。


## 安装与启动服务器

Ubuntu下：
```sh
# 安装服务器
$ sudo apt-get install mysql-server

# 启停服务器：
$ sudo service mysql start
$ sudo service mysql stop
$ sudo service mysql restart
```

Mac下：安装比较麻烦。推荐GUI安装，因为命令行安装会有很多问题：
```sh
# 安装
brew install mysql

# 修复命令链接
brew link --overwrite mysql
```


## 配置MySQL

主要配置文件为`/etc/mysql/my.cnf`。
(如果不确定位置，可在`/etc/mysql/my.cnf`中查看具体引用的配置文件的位置)

文件中，常用的配置项有：
```ini
# 绑定的服务器地址
bind-address 127.0.0.1
port 3306

# 数据库目录
datadir /var/lib/mysql

# 日志
general_log_file /var/log/mysql/mysql.log
log_error /var/log/mysql/error.log
```


## 数据类型

主要需要区分的有：
- `enum`枚举类型：相当于List或Checkbox列表，只提供固定的选项。如Gender字段只能选`男、女`。
- `char` 固定长度字符串
- `varchar` 可变长度字符串

![image](https://user-images.githubusercontent.com/14041622/48895096-3dce7d00-ee7f-11e8-9990-479464f752ca.png)


## 数据约束

有以下集中约束类型：
- Primary Key 主键：填写作为每条数据的全表唯一性ID。
- Foreign Key 外键：填写另一个表中数据的唯一性ID。不推荐使用，因为会很大降低存取速度。推荐在代码中实现这个功能。
- Unique 唯一：该字段不允许重复。（相当于Set集合）
- Not null 非空：不允许空值。
- Default 默认值：不填写时会使用设定好的默认值。
