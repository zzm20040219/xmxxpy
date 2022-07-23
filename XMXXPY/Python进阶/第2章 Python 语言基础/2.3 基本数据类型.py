# 由公众号"小明创客"技术管理
# 明氏技术有限公司
# 技术主编 ：小明


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


#转义字符
print('hello\nworld') #\ +转义功能的首字母 n-->newline的首字符表示换行
print('hello\tworld')      #不清楚的地方                                 个gryehqyrhoqhouhhf
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










