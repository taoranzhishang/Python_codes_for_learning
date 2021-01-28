class LazyPeople:
    name = "coder"  # 没有self，静态属性，有self是实例属性

    def habit(self):  # 无双下划线开头的是公有方法
        print(self.name, "拿得起放不下的是筷子，陷进去出不来的是被窝。")#属性的引用要加self


person = LazyPeople()
print(type(person))
print(person.name)
person.habit()
