# 由公众号"小明创客"技术管理
# 明氏技术有限公司
# 技术主编 ：小明


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

'''
2.2.2理解Python中的变量
在Python中，严格意义上变量应该称为“名字”，也可以理解为标签。当把一个值赋给一个名字
(如把值“学会Pyhon还可以飞”赋给python)时，python就称为变量。在大多数编程语言中，都把这
称为“把值存储在变量中”。意思是在计算机内存中的某个位置，字符串序列“学会Python 还可以飞”
已经存在。你不需要准确地知道它们到底在哪里。只需要告诉Python 这个字符串序列的名字是python，
然后就可以通过这个名字来引用这个字符串序列了。这个过程就像上门取快递一样，内存就像一个巨大
的货物架，在Python中使用变量就像是给快递盒子加标签
'''



