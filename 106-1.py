# coding:utf-8
def add_function(a,b):
    c= a+b
    print(c)

if __name__ == "__main__":
    add_function(2,0)


# 分别写出三个变量为int类型，float类型，str类型，例如int类型：a = 1
# 查看定义三个变量的类型（type）并计算数值类型总值

a = 1
b = '25'
c = 3.14
print(type(a),type(b),type(c))
print(a+int(b)+int(c))


a = "如果给这份爱加上⼀个期限我希望是"
b = "9999.00"
c = "1"
d = "年"
# 请根据我们提供的a,b,c,d变量 进⾏运算拼接处出： 如果给这份爱加上⼀个期限我希望是
# 10000年
#
# 首先我们把b转换成float浮点类型，
# 然后转换成int类型去掉小数,再把c转换成int类型，
# 将b+c进行数字计算，整体为： e = int(float(b))+int(c)，
# 然后我们把字符串进行拼接,需要把我们计算的e再转换为str类型进行字符串拼接
print(type(a),type(b),type(c),type(d))
print(a+str(int(c)+int(float(b)))+d)
time = 9
# 条件1，如果加班时间>=10,小k打车回家
if time >= 10:
    print('小k打车回家')
elif time <= 10:
    print('小k做地铁回家')
elif time <= 8:
    print('小k骑单车回家')
else:
    print(小k不回家)