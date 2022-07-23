# 由公众号"小明创客"技术管理
# 明氏技术有限公司
# 技术主编 ：小明


# 条件表达式
'''
条件表达式是if……else的简写

语法结构:
    if  判断条件 else y

运算规则:
    如果判断条件的布尔值为True，条件表达式的返回值为 x ，
    否则条件表达式的返回值为False
'''
'''
从键盘录入两个整数，比较两个整数的大小
'''
num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第二个整数'))
#比较大小
'''
if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于等于',num_b)
'''
print('条件表达式进入比较')
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于等于'+str(num_b))


#pass语句
'''
pass语句
    语句什么 都不做，只是一个占位符，用在语法上需要语句的地方
什么时候使用：
    先搭建语法结构，还没想好代码怎么写的时候
那些语句一起 使用
    if语句的条件执行体
    for-in语句的循环体
    定义函数时的函数体
'''
#什么都不做，只是一个占位符，用到需要写语句的地方
answer=input('您是会员吗？y/n')
#判断是否是会员
if answer=='y':
    pass
else:
    pass


#内置函数range（）
'''
range()内置函数
    用于生成一个整数序列
'''
#range（）的三种创建方式：
#第一种创建方式，只有一个参数（小括号中只给了一个参数）
r=range(10)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],默认从0开始，默认步长为1
print(r)     #range(0, 10)
print(list(r))#用于查看range对象中的整数序列  -->list是列表的意思

#第二种 给了两个参数（小括号中给了两个参数）
r=range(1,10)   #指定了起始值，从1开始，到10结束（不包含10）默认步长为1
print(list(r))  #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#第三种 给了三个参数（小括号中给了三个参数）
r=range(1,10,2)  #起始 结束 步长 start stop step
print(list(r))  #[1, 3, 5, 7, 9]

#判断指定的整数 在序列中是否存在 in， not in
print(10 in r) #False,10不在当前的r这个整数序列中
print(9 in r)  #True，9在当前的r这个整数序列中

print(10 not in r)#True，10在当前的r这个整数序列中
print(9 not in r) #False,9不在当前的r这个整数序列中

print(range(1,20,1)) #[1……19]
print(range(1,101,1))#[1……100]


#循环结构
'''
反复做同一件事情的情况，称为循环
循环的分类
    while
    for-in
语法结构
while 条件表达式：
    条件执行体（循环体）
'''
a=1
#判断条件表达式
while a<10:
    #执行条件执行体
    print(a)
    a+=1
#while循环执行流程
'''
四步循环法
    初始化变量
    条件判断
    条件执行体（循环体）
    改变变量
'''
sum=0
a=0
while a<5:
    sum+=a
    a+=1
print('和为',sum)







