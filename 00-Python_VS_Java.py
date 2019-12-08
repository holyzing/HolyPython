
# 0-综述
'''
    0-1:语言特点
        Pyth: Python是动态的,解释执行.
        Java: Java是静态的,编译执行.
'''
# 1-变量和常量
'''
    1-1:严格区分变量与对象
        Pyth: 变量就是引用,对象就是实例.引用 指向 实例. 变量是不可变的,变得是指向的对象的内容,
              变量通过方法操纵对象,那些操作符也都是方法.
        Java: 与Python几乎一致
    1-2:类的成员变量 ---->>可通过类名直接访问的变量
        Pyth: 方法之外声明且已经被初始化的变量.(初始化的意思就是它有指向一个对象)
              python中变量声明即确定类型,确定类型就得有指向,所以必须得初始化.
        Java: 带有static 描述的成员变量. 基本类型都有默认值,引用类型可不初始化,值为null
    1-3:对象的成员变量
        Pyth: 定义在__init__中的变量,且以 self. 引用.
        Java: 类中,定义在方法之外的无 static 修饰的变量.
    1-4:局部变量
    1-5:常量
        Pyth:
        Java: 指向不能被改变的变量,用final修饰
    1-6:基本类型和引用类型 ---->>重点
        Pyth: python中没有基本类型的概念,一切皆对象,但是python中数字这类对象的值是不能被改变的,改变意味着重开内存.
        Java: 基本类型都有默认值,变量指向数据空间(栈),变意味着指向的内存值变. 注意操作符 + 其实是分先后顺序的

'''
# 4-方法
'''
     4-1:类的普通成员方法
        Pyth: 总是将调用成员方法的实例作为第一个实参,成员方法的第一个形参接收这个实参,规范为 self
        Java: 中具有同样功能的this,指向调用成员方法的对象.
    4-2:类的静态成员方法
        Pyth:
        Java: 中的静态方法中是不能使用 this 的,原因很简单...
    4-3:方法的返回类型
        Pyth: 中的方法是不强调返回类型的,也就是说 return 是随时可以使用的.
        Java: 中具有明确的返回以及返回类型限制
    4-4:方法的形参与实参
        Pyth: 中方法的形参与实参具有强大的匹配机制.
              形参以 key=value 的形式给定默认值的方式,极大的方便了开发.
              实参以 可严格按照形参列表赋值,也可以key=value的形式给定实参,这个实参key在形参列表中如果有的话就匹配到这个形参,
              如果没有的话依然会传递,经常使用的场景就是不定参的传递,方法内部会判断这个参数是否存在,如果存在则处理,不存在...
        Java: 实参严格按照形参的列表进行传递,即使有可变参数的存在.
    4-5:类的构造方法
        Pyth: 不可重载,从上到下的同名方法依次被覆盖. __init__ 被称为魔法方法
        Java: 可重载
    4-6:方法的使用
        Pyth: Pyth的 method 和 method() 是有不一样的效果的,方法也是一个对象
        Java: 一切方法属于类或接口,只能通过一个实例调用

'''
# 3-对象(实例)
'''
    3-1:对象三特征
        类型,值,编号
    3-2:Python中一切皆对象,Java中有基本类型和引用类型的区分.
    3-3:Python中的引用变量就是一个便利贴,Java中的引用变量就是一个盒子.
    3-4:is | == | equals()
'''
# 2-类
'''
'''

# 5-注释
'''
'''

----------------------------------------------------------------------------------------------------------------------
======================================================================================================================



"""
1-配置淘宝镜像源
	npm install -g cnpm --registry=https://registry.npm.taobao.org
	npm install
	npm -g isntall
	npm view XXX version/versions
	npm ls	--depth 0
	npm ls -g --depth 0
2-安装angular-cli
	cnpm install -g @angular/cli@latest 【指定版本】
3- 清除缓存
	npm cache clean --force
4- 安装依赖
	在工程根目录下 npm install
5- angular ng 命令 的使用	【查看help】
6-<app-route>
	局部页面的占位符 为 <route-outlet> 占位
7-<route-outlet>看
	为路由的 xxx.compemt.html 占位  单页面路由
8-一个angular App下的ts文件
	moudule/service/component/spec
9-angular指令
10-数据绑定
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
1- 创建虚拟环境
	virtualenv --no-site-packages -p [python路径] [虚拟环境名称]
	windows下虚拟环境移动后会失效，可能和注册表信有关
2- 重装pip
	python3 -m pip install -U pip	【升级】
	python3 setup.py install        【安装】
	python3 -m pip install --upgrade pip --force-reinstall 【升级，重装】
3- pip -V
	查看当前python路径，确保使用的是虚拟环境。
4- Django同步model
	使用 python manage.py 查看有哪些指令
	python manage.py makemigrations
	python manage.py migrate/sqlmigrate/syncdb	【实现同步】
5- 解压版mysql安装
	5.1-配置文件
		配置文件中的配置以 [mysqld] 独占一行开头
	5.2-mysql操作命令
		mysqld.exe --defaults-file="D:\mysql-5.7.24-winx64\my.ini" --console --skip-grant-tables 【安全模式】
		update user set host='localhost' where user='root';   									 【root赋权】
6-rest_framework
	幂等性：对同一个接口的多次访问，得到的资源状态是相同的。
	​安全性：对该REST 接口访问，不会使服务端资源状态发生改变
	FBV：
	CBV：
	MiXin：
	oauth：
	Dispather：
	views.APIView：										【主要完成认证】
	openid-connect：
	viewsets.ModelViewSet：
	AUTHENTICATION_BACKENDS：
	permissions.BasePermission：
	serializers.ModelSerializer：
	django.contrib.auth.backends.ModelBackend						【登录认证是否登录成功】
	django.contrib.auth.middleware.AuthenticationMiddleware			【登录后认证session】
7-在shell中执行python文件
	import sys;sys.path.append("F:/mywork/ctskb/tools-backend/apiv1");import xmlparser;xmlparser.parser_ctskb_xml("","","")
8-shell中清屏
	import os
	os.system('cls')
9-Django
	9.1-on_delete 删除外键记录时，绑定外键记录操作
	9.2-related_name="cts_releases" 反向操作时的表名
	9.3-DateTimeField 的类型为 datetime.datetime
10-UnboundLocalError:
	局部变量与全局变量的定义
	global 声明一个全局变量
	class Demo():
		name = "name"	【类对象属性，共享】
		def __init__(self):
			self.name = "name"	【克隆对象属性】

	类对象.__dict__		获取公有属性,及其值
	实例对象.__dict__   获取私有属性，及其值
	dir(类和对象是一样的)
	dir和__dict__分别应用到类和对象上的区别
	python中数字的默认类型为int
	【erro】local variable 'xxx' referenced before assignment  当使用NULL去引用时报出
	not and or
	None、空列表[]、空字典{}、空元组()、0等一系列代表空和无的对象会被转换成False。除此之外的其它对象都会被转化成True，和C语言类似。
	is	type() isinstance id()
	创建实例时，可给定类成员参数赋值  test = Test(类成员=“”，实例成员=“”) 参数命名空间顺序 【与__init__(self,..)区别联系】
	super() self

	为什么 挨着的两个try_catch块 在文件的命名空间下。在方法中第二个try_catch块会无效
------------------------------------------------------------------------------------------------------------
	getattr
	hasattr
	setattr
	__all__
	os.path.join
	@classonlymethod
	@classmethod
	@staticmethod
	annotation
------------------------------------------------------------------------------------------------------------

windows7中内置telnet服务以及客户端
win10已经内置openSSH客户端，但移除telnet服务
windows中也可以使用 	>
-------------------------------------------

# path 和 url 均可作为路由映射，url 是对低版本的向下兼容
# 基于CBV的分发模式

0-基础设置
	sudo passwd 【root初始密码设置】
1-ubuntu 软件安装
	//默认都是以
	/etc/apt/source.list 【配置源(apt-yum)】
	PPA:Personal Package Archives (daily dev stable beta)
	sudo add-apt-repository ppa:chromium-daily/stable 【安装谷歌浏览器的源】
	sudo add-apt-repository ppa:videolan/stable-daily 【安装VLC播放器】
	sudo apt-get update | grep "Failed" 【搜索获取失败的源】
	sudo add-apt-repository --remove ppa:finalterm/daily 【移除失败的源】
	sudo apt-get update 【更新源】
	sudo apt-show-versions -a git 【查看软件的所有版本】

	apt-(tab) 【可查看所有已安装apt命令 使用参数 --help可产看帮助，要有看帮助的习惯！】
	dpkg
	curl
	wget
	snap store 	【？？？ 】

2-ubuntu下python版本控制
	Ubuntu16.04 有太多应用依赖自带的 python3.5，所以不能卸载.
	find / -name 'python'【所有安装路径】
	/usr/bin/ 【所有用户安装的脚本，包括所有版本的python】
	/bin 【系统级别目录】


3-ubuntu下Java版本控制
	update-alternative
4-ubuntu下MySQL的安装
5-linux中出现 Read-only file system
	mount -o,remount,rw /dev/sda18 /opt/gracenote/db/
6-由windows下拷贝的文件./install_ssh.sh 安装时出现一下错误。
	 bad interpreter: Permission denied
"""