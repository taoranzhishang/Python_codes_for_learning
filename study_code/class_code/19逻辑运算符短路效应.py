'''
and:当表达式1为true还要算表达式；表达式1为false则不计算表达式2，结果直接为false
false：当表达式1为true则不计算表达式2；当表达式1为false还要计算表达式2
'''
num=eval(input("num:"))
# if num>1 and num<100 or num<0:
print(num>1 and num<100 or num<0)

x=4;y=5
print(x>=y>=0)
print(x<=y>=0)
print(x!=y==5)
print(x!=0 or x==0)
