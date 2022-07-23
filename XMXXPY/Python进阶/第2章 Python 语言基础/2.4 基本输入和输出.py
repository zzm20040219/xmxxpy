# 由公众号"小明创客"技术管理
# 明氏技术有限公司
# 技术主编 ：小明


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









