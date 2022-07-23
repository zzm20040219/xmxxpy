# 由小明公众号"小明创客"技术管理
# 技术主编 ： 小明
# 明氏技术有限公司
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
支付攒类型： str

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


















