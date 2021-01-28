class MyClass:
    """
    __init__方法：构造函数用于初始化类的内部状态，为类的属性设置默认值（是可选的）。
    如果不提供__init__方法，python将会给出一个默认的__init__方法
    """

    def __init__(self):  # 初始化时调用
        print("构造函数", id(self))

    """
    __del__方法：构析函数用来释放对象占用的资源（是可选的）。
    如果程序中不提供构析函数，python会在后台提供默认的构析函数；所以只有在需要的时候才会定义构析函数
    """

    def __del__(self):  # 删除时调用
        print("析构函数", id(self))


cl1 = MyClass()
cl2 = MyClass()
