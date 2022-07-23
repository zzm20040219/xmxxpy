# 由小明公众号"小明创客"技术管理
# 技术主编 ： 小明
# 明氏技术有限公司



#第一章初识Python 环境安装




#第二章Python语法特点
#注释规则
'''
#：   单行注释
'''   '''：多行注释
'''


#输出功能
#可以输出数字
print(520)
#可以输出字符串
print('helloworld')
#还有运算符的表达式
print(3+2)
#将数据输出文件中
'''
注意点:
打开文件 a+：若没有则新建 存在就在后面续写 fp：赋值
1.所指定的盘符存在
2.file=fp
'''
fp=open('E:/test.txt','a+')
print('helloworld')
fp.close()

#不进行换行输出
print('hello','world','Python')


#转义字符
print('hello\nworld') #\ +转义功能的首字母 n-->newline的首字符表示换行
print('hello\tworld')      #naenavuodnovuhovhoqhvhqvouqdbvobdouiachehojoquvhoeqcouenvgeqbvehcbqciubquigvbebcusoavb
print('helloooo\tworld')
print('hello\rworld') #world将hello进行了覆盖
print('hello\bworld') #\b退一个格，将o退没了

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')


#源字符： 不希望字符串中的转义字符起作用，就使用源字符，就是在字符串之前加r,或R
print(r'hello\nworld')
#注意事项，最后一个字符不能是反斜杠
#print(r'hello\nworld\')
print(r'hello\nworld\\')

#保留字    查询保留字

import keyword
print(keyword.kwlist)

#标识符
'''
1.字母 数字 下滑线
2.不能以数字开头
3.不能是保留字
4.严格区分大小写
'''

#Python中的变量
name='朱志明'
print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)

#变量的多次赋值
name='玛利亚'
name='楚留香'
print(name) #赋值后指向新的赋值程序

#数据类型
'''

整数类型 ：int 
浮点数类型：float
布尔类型： bool
字符串类型： str

'''
#整数类型 ：int   :
#英文名 integer 简写int 可以为正数 负数和零
#整数不同的进制不同的表示
#十进制 ：默认进制
#二进制 ：以0b开头
#八进制 ：以0o开头
#十六进制 ：以0x开头
print('十进制',118)
print('二进制',0b111010)
print('八进制',0o1147)
print('十六进制',0x1EAF)

#浮点数类型：float
#浮点数整数部分和小数部分组成
#浮点数储存不准确性
    #使用浮点数进行计算时，可能会出现小数位数不确定的情况
n1=1.1
n2=2.2
print(n1+n2)
#解决方案
    #导入模块
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型： bool   英文名boolean
#用来表示真或假的值
#True表示真，False表示假
#布尔值可以转化为整数
    #True表示：1
    #False表示：0
f1=True
f2=False
print(type(f1),f1)
print(type(f2),f2)
#布尔值转成整数计算
print(f1+1)
print(f2+1)


#数据类型转换
#为什么需要数据类型转换？
    #将数据类型的数据拼接在一起
#int（x）将x转换成整数类型
#float（x）将x转换成浮点数类型
#str（x）将x转换成字符串

name='张三'
age=20

print(type(name),type(age)) #说明name与age的数据类型不相同
'''
数据类型不相同的错误输出案例
print('我叫'+name+'今年'+age+'岁')
'''
#将int类型通过str()函数转成了str类型
print('我叫'+name+'今年'+str(age)+'岁')
#事例
print('------str()将其他类型转成str类型-------')
f=12
b=23.5
c=False
print(type(f),type(b),type(c))
print(str(f),str(b),str(c),)

print('-------int()将其他类型转成int类型-------')
qwe1='123'
qwe2=23.8
qwe3='23.2'
qwe4=True
qwe5='hello'
print(type(qwe1), type(qwe2), type(qwe3), type(qwe4), type(qwe5))
print(int(qwe1),type(int(qwe1))) #将str转换成int类型，字符串为数字串
print(int(qwe2),type(int(qwe2))) #将float转成int类型，截取整数部分，舍去小数部分
#print(int(qwe3),type(int(qwe3))) #将str转成int类型，报错，因为字符串为小数串
print(int(qwe4), type(int(qwe4)))
#print(int(qwe5),type(int(qwe5)))#将str转成int类型时，字符串必须为数字串（整数），非数字串是不允许转换的

print('-------float()函数，将其他数据类型转成float类型------')
qw1='123.4'
qw2='42'
qw3=True
qw4= 'hello'
qw5=42
print(type(qw1), type(qw2), type(qw3), type(qw4),type(qw5))
print(float(qw1),type(float(qw1)))
print(float(qw2),type(float(qw2)))
print(float(qw3),type(float(qw3)))
#print(float(qw4),type(float(qw4))) #字符串中的数据如果非数字串，则不允许转换
print(float(qw5),type(float(qw5)))



#第三章
'''
1.python的输入函数input
2.Python中的运算符
    算术运算符
    赋值运算符
    比较运算符
    布尔运算符
    位运算符
3.运算符的优势
'''
#python的输入函数input
present=input('提示文字')
print(present)
print(type(present))
#练习题
#从键盘录入两的整数，计算两个整数的和
one=input('请输入一个加数：')
two=input('请输入一个被加数：')
print(one+two)  #计算起数字连接作用
#解决方法
    #利用数据转换进行转换
one=int(input('请输入一个加数：'))
two=int(input('请输入一个被加数：'))
print(one+two)

#算术运算符
    #标准运算符 加（+）减（-）乘（*）除（/）整除(//)
print(1+1)   #加法运算
print(1-1)   #减法运算
print(2*4)   #乘法运算
print(1/2)   #除法运算
print(11//2) #整除运算
print(11%2)  #取余运算
print(2**2)  #幂运算
print(-9//4) #一正一负的整数公式，向下取整

#赋值运算符
#赋值 运算顺序从右往左
a=b=c=11
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('-----------支持参数赋值-----------')
a=20
a+=30  #相当于a=a+30
print(a)
a-=10
print(a)
a*=2
print(a)
print(type(a))
a/=3
print(a)
print(type(a))
a//=2
print(a)
print(type(a))
a%=3
print(a)

print('-------------解包赋值-------------')
a,b,c=20,30,40
print(a,b,c)

print('-----------交换两个变量的值-------------')
print('交换之前：',a,b)
a,b=b,a
#交换
print('交换之后：',a,b)

#比较运算符   比较运算符的结果为bool类型
m,n=10,20
print('m>n?',m>n)    #False
print('m<n?',m<n)    #True
print('m<=n?',m<=n)  #True
print('m>=n?',m>=n)  #False
print('m==n?',m==n)  #False
print('m!=n',m!=n)   #True
'''一个  =  称为赋值运算符 ， ==称为比较运算符
   一个运算由三个部分组成，标识，类型，值
   ==比较的是值
   比较对象的标识使用 is
'''
o=10
p=10
print(o==p)    #True 说明 o与p的value 相等
print(o is b)  #True 说明，a与b的id标识 相等
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)   #value  True
print(lst1 is lst2) #id  False
print(id(lst1))
print(id(lst2))
print(o is not b)  #Flsae o的id与p的id是不相等的
print(lst1 is not lst2)   #True o与p的id不相等

#布尔运算符
    #  and,  or,  not,  in,  not in.
we1,we2=1,2
print('---------------and 并且-----------------')
print(we1==1 and we2 )     #Ture   True and True -->True
print(we1==1 and we2<2)    #False  True and False-->False
print(we1!=1 and we2==2)   #False  False and True-->False
print(we1!=1 and we2!=2)   #False  False and False->False

print('---------------or 或者------------------')
print(we1==1 or we2==2)    #True or True -->True
print(we1==1 or we2<2)     #True or False -->True
print(we1!=1 or we2==2)    #False or True -->Ture
print(we1!=1 or we2!=2)    #False or False -->False

print('------------ not 对bool类型操作数取反--------------')
j=True
k=False
print(not j)
print(not k)

print('----------------in 与not in-----------------') #存在  不存在
poopoiiipi='helloworld'
print('w' in poopoiiipi) #False
print('k' in poopoiiipi) #True
print('w' not in poopoiiipi) #True
print('k' not in poopoiiipi) #False

#位运算符：将数据转成二进制进行计算
    #位与&： 对应数都是1，结果位数才是1，否者为0
    #位或|： 对应数位都是0，结果数位才是0，否则为1
    #左移位运算符<<: 高位溢出舍弃，低位补0
    #右移位运算符>>: 低位溢出舍弃，高位补0
print(4&8)  #按位与&，同为1时结果为1
print(4|8)  #按位或|,同为0时结果为0
print(4<<1) #向左移动1位（移动1个位置）相当于乘以2
print(4>>2) #向右移动2位（移动2个位置）相当于除以4

#运算符的优先级
#算术运算->位运算->比较运算->布尔运算->赋值运算
#有（）先算（）内的


#第四章
'''

1.程序的组织结构
2.顺序结构
3.对象的布尔值
4.分支结构
  单分支结构
  双分支结构if...else结构
  多分支结构if...elif...else结构
  if语句的嵌套
  条件表达式

'''


#程序的组织结构

#顺序结构
'''把大象装进冰箱一共分几步'''
print('-------------程序开始---------------')
print('1.把冰箱门打开')
print('2.把大象装进冰箱')
print('3.把冰箱门关上')
print('------------程序结束---------------')

#运行知识点
'''
单击左侧出现一个红色圆点（断点）
点击虫子运行断点以下的
'''

#对象的布尔值
'''
pyton一切皆对象，所有对象都有一个布尔值
    获取对象的布尔值
        使用内置函数bool（）
以下对象的布尔值为False
    False
    数值（）
    None
    空字符串
    空列表
    空元组
    空字典
    空集合
'''

#测试对象的布尔值
print('------------以下布尔值为False--------------')
print(bool(False))  #False
print(bool(0))      #False
print(bool(0.0))    #False
print(bool(None))   #False
print(bool(''))     #False
print(bool(""))     #False
print(bool([]))     #空列表
print(bool(list())) #空列表
print(bool(()))     #空元组
print(bool(tuple()))#空元组
print(bool({}))     #空字典
print(bool(dict())) #空字典
print(bool(set()))  #空集合

print('------------其他布尔值均为True--------------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))


#选择结构

#单分支结构
'''
中文语义：如果……就……

语法结构：
if 条件表达式：
    条件执行体
'''
money=1000  #余额
s=int(input('请输入取款金额'))
#判断余额是否充足
if money>=s:
    money=money-s
    print('取款成功，余额为：',money)


#双分支结构
'''
中文语义：如果……不满足……就……

语法结构：
if 条件表达式：
    条件执行体1
else：
    条件执行体2
'''
#双分支结构if……else……，二选一执行
'''从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数'''
num=int(input('请输入一个整数'))

#条件判断
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')


#多分支结构
'''
中文语义：
    ……是……不是
    ……是……不是
    ……是……不是
    ……是……不是
    ……是……是
语法结构：
    if 条件表达式1
        条件执行体1
    elif 条件表达式2
        条件执行体2
    elif 条件表达式N
        条件执行体N
    [else:]  #可写可不写
        条件执行体N+1
'''
'''
从键盘录入一个整数 成绩
90-100  A
80-89   B
70-79   C
60-69   D
0-59    E
小于0或大于100 为非法数据（不是成绩有限范围）
'''
score=int(input('请输入一个成绩：'))
#判断
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score <=89:
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=69:
    print('D级')
elif score>=0 and score<=59:
    print('E级')
else:
    print('对不起，成绩有误，不在成绩的有效范围')
#第二种写法
if 90<=score<=100:
    print('A级')
elif 80<=score <=89:
    print('B级')
elif 70<=score<=79:
    print('C级')
elif 60<=score<=69:
    print('D级')
elif 0<=score<=59:
    print('E级')
else:
    print('对不起，成绩有误，不在成绩的有效范围')


#嵌套if
'''
语法结构：
if 条件表达式1
    if 内层条件表达式：
        内存条件执行体1
    else：
        内存条件执行体2
else：
    条件执行体
'''
'''
会员 >=200 8折
    >=100 9折
     不打折
非会员 >=200 9.5折
     不打折
'''
answer=input('你是会员吗？y/n')
money=float(input('请输入您的购物金额'))
#外层判断是否是会员
if answer=='y':  #会员
    if money>=200:
        print('打8折，付款金额为:',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为',money)
else:  #非会员
    if money>=200:
        print('打9.5折，付款金额为：',money*9.5)
    else:
        print('不打折，付款金额为：',money)


#条件表达式
'''
条件表达式是if……else的简写

语法结构:
    if  判断条件 else y
    
运算规则:
    如果判断条件的布尔值为True，条件表达式的返回值为 x ，
    否则条件表达式的返回值为False
'''






