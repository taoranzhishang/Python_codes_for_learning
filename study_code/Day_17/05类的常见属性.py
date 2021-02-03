class C:
    """
    类的常见属性演示
    """

    def __init__(self):
        pass

    def func(self):
        pass


print(C.__name__)  # C 类的名称
print(C.__module__)  # __main__ 从哪个位置执行
print(C.__doc__)  # 类的常见属性演示，文档，类的说明
print(C.__bases__)  # (<class 'object'>,)，类的父类
print(C.__dict__)  # 类的所有属性存放在字典内
