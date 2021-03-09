# 标识符
"""
有数字。字母、下划线组成，但是数字不能开头

命名规则：
1.见名知意
2.驼峰命名法
    大驼峰 MyName
    小驼峰 myName
3._下划线链接单词
    my_name

关键字：
关键字:一些具有特殊功能的标识

总结
注释：
# 单行注释
"""""" 多行注释，三引号之间的内容都是注释
多行语句\
a = "abdncgf"+\
    "dsgjhgds"

列表 元祖 字典不需要换行符的

数据类型：
数字 number
a
print(a)
顺序
从左到右 0
从右到左 -1

字符串：
str = "i love you"
print(str[起始值：终止值])

列表：
list = [12,"sdfsd"]

访问
print(list[起始值：终止值])

修改
list[0] = "abc"

元祖：
tuple = (1,)
访问方式
print(tuple[起始值:终止值])
元祖不可修改

字典：
dict = {键:值}
访问
dict[键]
dict.key()
dict.value()

数据类型转换
转字符串 str()
转数字 int()
转列表 list[]
转元祖 tuple()

标识符与关键字：
数字 字母 下划线 组成 数字不能开头
命名规则
见名知意
驼峰命名
    大驼峰MaName
    小驼峰myName
下划线链接
my_name

关键字：
python 中已经赋予特殊意义的词

import keyword
print(keyword.kwlist)


"""
import keyword
print(keyword.kwlist)
