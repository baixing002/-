# 逻辑运算符 and 两者都为真的是会后就为真
a = 10
b = 20
print(a and b)

c = bool(a)
print(c)

# or 或 有一个为真则为真
a = 10
b = 0
print(bool(a))
print(bool(b))
print(a or b)

# not 真假相反
a = 0
print(not a)
