# 由公众号"小明创客"技术管理
# 明氏技术有限公司
# 技术主编 ：小明


#选择结构  if语句

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






