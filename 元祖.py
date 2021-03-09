# 表示()
a = ('abc', 12, "find", 10.2)
a1 = ('gf', 15, 12.52, "yes")
# 访问第一个值
print(a[0])

# 访问列表的第一个值到第二个值
print(a[1:2])

# 从头访问到尾
print(a[1:])

# *号的作用
print(a*3)

# +号的作用
print(a+a1)

list = [1, 2, 3, 4, 5, "abc"]
c = (1, 2, 3, 4, 5, "abc")
list[0] = 'abc'
print(list)

# 元祖不可以修改
# c[0] = 'abd'
