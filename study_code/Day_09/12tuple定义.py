tuple1=(1,2,3)#加括号的定义方式
tuple2=1,2,3#不加括号的定义方式
print(type(tuple1),type(tuple2))#都是tuple类型

tuple3=(1)#int类型，括号运算符不影响值
tuple4=(1,)#tuple类型，区别在逗号
print(type(tuple3),type(tuple4))

tuple5=1#int类型
tuple6=6,#tuple类型，区别在逗号
print(type(tuple5),type(tuple6))

data1=1,2,3,4#元组
data2=()#元组为空
print(type(data1),type(data2))
print(data1[1])
#data1[1]=100  #tuple不能修改
