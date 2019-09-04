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
1-文档上传
2-解析文档（良性校验） 		提供校验失败信息
3-DTD以及Schema约束校验		提供校验失败信息  lxml
4-数据持久化
5-文件保存
6-提供各种API （查询，联合查询，条件查询）
	1-新建项目
	2-
# path 和 url 均可作为路由映射，url 是对低版本的向下兼容
# 基于CBV的分发模式
--------------------------------------











----------------------------------
1-完成数据的导入（60M文件太大，效率堪忧）
2-完成创建工程的接口
3-完成文件上传的接口

