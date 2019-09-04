
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