class LazyPeople:
    name = "coder"  # 静态属性，代码块内部可用，外部不可用
    """
    self.只能在类的内部，不能在外部
    self可以调用属性和方法
    self相当于实例化后的对象，二者的地址相同，提高重用性和区分谁在调用方法
    类中属性是独立的，方法是共享的，调用方法要传递self（实例化的对象用self表示）
    """

    def habit1(self):  # self用于区分谁在调用，相当于实例化对象的地址，二者地址相同
        # self.name1 = "实例属性"  # 实例属性，其它方法可以使用，跨方法使用
        # name2 = "静态属性"  # 静态属性，相当于局部变量，其它方法不能使用，实例化对象不可以使用
        print(self.name, "love sleep")  # self调用属性
        # self.habit2()  # self调用方法
        self.num1 = 1

    def habit2(self):
        print(self.name, "love eat")
        # print(self.name1)  # 使用其它方法的实例属性
        # print(name2)  # 其它方法内的静态属性外部不能使用
        # self.num2=self.num1
        self.num2 = 1


# print(self.name)  # self.只能在类的内部使用
# self.habit1
person1 = LazyPeople()
# person1.habit1()
person2 = LazyPeople()
"""
不同对象调用同一个类，使用的是同样的属性和方法，地址相同，重用
"""
print(id(LazyPeople), id(person1.name), id(person1.habit1()),
      id(person1.num1))  # 1453129904880 1453100951344 140732057692288 140732057925408
print(id(LazyPeople), id(person2.name), id(person2.habit2()),
      id(person2.num2))  # 1453129904880 1453100951344 140732057692288 140732057925408
print(id(person1))  # 2789667183488
print(id(person2))  # 2789685320816
