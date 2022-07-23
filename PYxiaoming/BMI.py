# 由小明公众号"小明创客"技术管理
# 技术主编 ： 小明
# 明氏技术有限公司

# ===============程序开始==================#
height = float(input("输入身高 单位米"))
weight = float(input("请输入体重 单位千克"))

bmi: float = weight / (height * height)
print("您的BMI指数为：" + str(bmi))

#判段身材是否合理
if bmi<18.5:
    print("你的体重过轻")
if bmi>=18.5 and bmi<24.9:
    print("你的体重正常 继续保持")
if bmi >= 24.9 and bmi < 29.9:
    print("你的体重过重")
if bmi>=29.9:
    print("你已过于肥胖")
#==================程序结束=================#


