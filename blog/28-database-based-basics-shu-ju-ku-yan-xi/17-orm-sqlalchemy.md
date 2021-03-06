# ❖ ORM: SQLAlchemy 初识

ORM: Object Relational Mapper.

目前Python有很多ORM工具可以将数据库映像为Python的Objects对象。
其中比较知名的有Django的ORM，SQLAlchemy, PostgreSQL等。
`SQLAlchemy`有更多的人维护，功能也比较齐全。所以一般是我们的首选项。

对于`SQLAlchemy`的使用者来说，只要你一开始连接上数据库，不管是Sqlite，MySQL还是什么，后面的处理方式完全一样。这种便利性也是它受欢迎的原因。

抛弃了传统的自己编织SQL语句、制作模型、连接数据库方式，`SQLAlchemy`直接把这些东西全包在黑盒里面，让我们完全不需要去管。连SQL-Injection注入这种东西也被它帮忙防范了。这样一来，可以说在连接数据库方面，帮我们节省了最少一半以上的代码。

甚至连数据查询，SQLAlchemy也代替了SQL语句，而使用了专门的类似MongoDB的`Object.query.filter_by(name='Jason').all()`这种方法。

安装：
```sh
# 安装sqlalchemy
$ pip install sqlalchemy
```

安装Drivers：
```sh
# Sqlite
# 不需要，Python自带

# MySQL
$ pip install pymysql

# Postgresql
$ pip install psycopg2
```
SQLAlchemy自身不带数据库driver，需要我们自己安装，并在连接时候指定。
而这些driver，实际上就是我们曾经手动连接数据库所用的包。而SQLAlchemy只是代替我们使用这些同样的包。


## 连接数据库

[参考：Engine Configuration](https://docs.sqlalchemy.org/en/13/core/engines.html)

标准格式：
```uri
dialect+driver://username:password@host:port/database
```

创建一个sqlite的ORM引擎：
```py
from sqlalchemy import create_engine

# 连接格式为：sqlite://<Hostname>/<path>
engine  = create_engine('sqlite:///foo.db', echo=True)
```

创建一个MySQL的ORM引擎：
```py
from sqlalchemy import create_engine

# 连接格式为：dialect+driver://username:password@host:port/database
engine  = create_engine('mysql+pymysql://root:password123@localhost/db_test_01', echo=True)
```

创建PostgresQL的引擎(不同的driver)：
```py
# Driver: default
engine = create_engine('postgresql://user:password@127.0.0.1/mydatabase')

# Driver: psycopg2
engine = create_engine('postgresql+psycopg2://user:password@127.0.0.1/mydatabase')
```

数据库的位置（三斜杠为相对路径，四斜杠为绝对路径）：
```py
# 使用绝对路径的数据库文件(////)，如/tmp/mydatabase.db
engine  = create_engine('sqlite:////tmp/mydatabase.db')

# 使用当前「执行位置」数据库文件(///或///./)
engine  = create_engine('sqlite:///mydatabase.db')

# 使用当前「执行位置」父级目录(///../)的数据库文件
engine  = create_engine('sqlite:///../mydatabase.db')

# 使用当前「脚本位置」的数据库文件
import os
cwd = os.path.split(os.path.realpath(__file__))[0]
engine  = create_engine('sqlite:///{}/mydatabase.db'.format(cwd))
```

### Create Tables 创建表

> 注意：不同于SQL语句，SQLAlchemy中的表名是**完全区分大小写的**！

创建一个Schema表（指单纯表，不包含ORM对象）：
```py
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, ForeignKey

engine  = create_engine('mysql+pymysql://root:password123@localhost/db_test_01', echo=True)
metadata = MetaData(engine)

# 创建一个表
user_table = Table( 'tb_user', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(50)),
        Column('fullname', String(100))
)

# 让改动生效
metadata.create_all()
```


创建一个ORM对象（包括表）：
```py
# 导入表格创建引擎
from sqlalchemy import create_engine
# 导入列格式
from sqlalchemy import Column, Integer, String, ForeignKey
# 导入创建ORM模型相关
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class User(Base):
    __tablename__ = 'tb_Person'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)

engine = create_engine('sqlite:///test.sqlite', echo=True)
User.__table__.create( engine )

# 或生成所有绑定到Base类的子ORM
Base.metadata.create_all( bind=engine )
```

用普通表Table和ORM对象创建的表有什么不同？
他们在数据库中创建的，是完全相同的表！唯一区别是，Table创建的不包含ORM对象，也就是不提供让你直接操作Python对象的功能。
这么做的好处是，有很多只是关联作用的表，没有必要生成ORM对象。




## 删除数据库中的表

```py
# engine = ...
# Base = ...

# 逐个ORM对象删除对应的表，如User类
User.__table__.drop(engine)

# 删除全部表
Base.metadata.drop_all(engine)
```
设计或调试过程中，我们经常要频繁改动表格，所以有必要在创建表格前把测试数据库中的表都清除掉，再创建新的定义。




## Insertion 插入数据

将数据添加到数据库：
```py
# ...
# 导入session相关(用于添加数据)
from sqlalchemy.orm import sessionmaker, relationship

user = User()
user.id = 1
user.username = 'Jason'

Session = sessionmaker(bind=engine)
session = Session()
session.add(user)
session.commit()
session.close()
```

注意：这里的`session`和网站上的session概念有点不一样。这里是用来commit提交数据库变动的工具。


批量添加数据（向add_all()传入列表）：
```py
session.add_all( [user1, user2, user3] )
```

添加每条数据的时候自动flush():
```py
session = sessionmaker(bind=engine, autoflush=True)
```

`autoflush`是在每次`session.add()`自动执行`session.flush()`，即在插入数据库之前就在内存中生成所有对象的动态数据（如主键ID等）。一般默认是选false，因为会影响效率。最好是需要的时候，才手动执行`session.flush()`

具体缘由，看下一节“数据生效”。


## Take effect 数据生效

SQLAlchemy中的`create_all()`和`session.commit()`都是直接让python文件中定义的对象在数据库中生效的语句。在此之前，无论怎么定义，数据都是在内存中，而没有在数据库中的。

注意区分：
- `create_all`只是让创建表格结构生效，无关insert的数据条目
- `session.commit()`只是让添加的数据生效，而不负责任何表格结构。

这两个的顺序，当然是先创建表格，再插入数据。

只是，如果我们知道了这个原理，在编码中才能比较运用自由。比如，连`create_engine()`创建引擎，我们都可以在后面定义，而没必要非得写在文件头，即所有的ORM定义之前。
`create_engine`只要定义在所有ORM类和Schema表之后即可。

**此后**，我们再开始进行数据插入工作，也就利用到了session。

session过程中呢，我们也会遇到互相引用主键外键ID的情况。但是注意，这时候因为还没有使用最终的`session.commit()`真正提交数据到数据库中，这些ID是没有值的。
解决办法就是利用内置的方法`session.flush()`，将session中已添加的所有对象填充好数据，但是这时候还没有提交到数据库，只是我们内部可以正常访问各种ID了。


## 更新／删除数据

更新：
```py
# Get a row of data
me = session.query(User).filter_by(username='Jason').first()

# Method 1:
me.age += 1
session.commit()

# Method 2:
session.query().filter(
    User.username == 'Jason'
).update(
    {"age": (User.age +1)}
)
session.commit()

# Method 3:
setattr(user, 'age', user.age+1)
session.commit()
```



## Get Primary Key Value 获取主键值

`#sqlalchemy can't get primary key `, `#sqlalchemy 如何获得主键的值`

> 这个问题花了我很多时间探索查询，不得其解，才明白原来是很显然的事。

[参考思否：SQLAlchemy中返回新插入数据的id？](https://segmentfault.com/q/1010000004827321)

虽然在没有用session或engine插入数据之前，我们可以直接浏览从ORM创建的对象中的属性值。
但是这个时候无论如何都获取不到`primar_key`主键列的值。

**因为这时候主键还没有插入数据库，作为`动态的值`，在数据库没生效之前也就为None。**

为什么需要获取`value of primary_key`？考虑如下这些场景：
- 子表中的`foreign key`外键需要引用主表的id
- ??

那么该怎么获取主键ID呢？

[再参考Stackoverflow：sqlalchemy flush() and get inserted id?](https://stackoverflow.com/questions/1316952/sqlalchemy-flush-and-get-inserted-id)
[再参考：sqlalchemy获取插入的id](http://ju.outofmemory.cn/entry/20258)
[再参考：Sqlalchemy;将主键设置为预先存在的数据库表（不使用sqlite）](https://stackoverrun.com/cn/q/12543164)

如果要想在插入数据之前就获取主键等`动态列`的值，那么有这几种方法：
- 直接利用SQLAlchemy建立类直接的内部关联，而不直接使用ID
- 主表插入数据，另session生效后，再用query获取相应对象，来得到它的ID。
- (*) 主表先用`session.add(..)`，再`session.flush()`，然后就可以获取ID，最后再`session.commit()`
- 不使用primary key主键，自己手动创建ID，这样来随便获取。

推荐做法如下：
![image](https://user-images.githubusercontent.com/14041622/50040642-7f1f0a80-0082-11e9-8581-1029426790ba.png)

即每次新创建对象后，立刻session.add(..)，然后立刻session.flush()，全部都添加好的文末，再session.commit().



## Query 查询

注意：query是通过session进行的，也就是必须在`session.commit()`之后才能进行查询，否则会报错。

> 这里将的query查询，指的都是`在插入到数据库生效之后`。理解这个很重要，因为在对象未插入到数据库之前，很多主键、外键等内容都是不存在的，也就无法查询到。

[参考：pythonsheets - Object Relational basic query](https://www.pythonsheets.com/notes/python-sqlalchemy.html#object-relational-basic-query)

查询数据：
```py
session.commit()
# ...

users = session.query(User).all()
# 返回的是多个User类的对象：>>> [ <User 1>, <User 2>, .... ]

for u in users:
    print(u.id, u.username)
```

常用查询方法：
```py
# 获取某ORM中数据 .query(ORM类名)
>>> session.query( User ).all()     # All rows of data
>>> session.query( User ).first()    # First row of data as an object

# 查询结果排序 .order_by(类名.列名)
>>> session.query(User).order_by( User.birth ).all()

# 筛选结果 .filter( True/False 表达式 )
>>> session.query(User).filter( User.name != 'Jason' ).all()
>>> session.query(User).filter( User.name.like('%ed%') ).all()    # Fuzzy search
>>> session.query(User).filter( User.id in [1, 2, 3] ).all()    # IN
>>> session.query(User).filter( ~ User.id in [4, 5, 6] ).all()   # NOT IN
>>> session.query(User).filter( User.school == 'MIT', User.age < 24 ).first()   # AND
>>> session.query(User).filter( _or(User.school == 'MIT', User.age < 24) ).first()   # OR
```


## Sqlalchemy Core (手动执行)

Sqlalchemy除了用ORM去访问数据库外，还可以用`Core` 像别的Driver驱动器一样去手动执行SQL语句访问数据库，而且速度会快几倍。

### 执行查询

```py
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://user:password@127.0.0.1:5432/mydatabase')
sql = 'SELECT name, age FROM persons'
with engine.connect() as conn:
    result = conn.execute(sql)
    for name, age in result:
        print(name, age)
```


### 执行增删改

```py

```
