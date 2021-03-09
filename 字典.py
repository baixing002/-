# 定义()
dict = {"name": "john", "age": 18, "great": "小学六年级"}

# 访问所有的值
print(dict)

# 访问固定键里面的内容
print(dict["name"])
print(dict["age"])
print(dict["great"])

# 访问所有的键
print(dict.keys())

# 访问所有的值
print(dict.values())

# 修改
dict["age"] = 16
print(dict)
