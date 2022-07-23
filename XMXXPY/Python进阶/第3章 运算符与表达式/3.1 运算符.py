# 由公众号"小明创客"技术管理
# 明氏技术有限公司
# 技术主编 ：小明


'''
Python中的运算符：
    算术运算符
    赋值运算符
    比较运算符
    布尔运算符
    位运算符
'''

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