"""
   作者：白星
   1.0：判断密码强弱
   2.0功能：限制密码次数，循环终止
   3.0新增功能：保存密码以及强度到文件中
   4.0新增功能：读取文件中的密码
   5.0新增功能：讲相关的方法封装成一个整体：面向对象编程 定义一个Password工具类
   5.0新增功能：定义一个文件工具类
   版本：1.0
   日期：08/16/20
"""

# 怎么样把跟密码相关的抽象出来 比如:密码强度 定义类
class  PasswordTool:
    """
        密码工具类
    """
    # 定义一个函数 从外面传进来数据  以下是属性
    def __init__(self,password):
        # 类里面的Password等于传进来
        # 类的属性
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')

        # 规则2 ：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码需求包含数字！')

        # 规则3 包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码需求包含字母！')

    # 类的方法
    def check_number_exist(self):
        """
            判断字符串中是否含有数字
        """
        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break

        return has_number

    def check_letter_exist(self):
        """
            判断字符串中是否含有字母
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter
    # 以上是类的定义 以下类的调用 怎么调用

class FileTool:
    """
        文件工具类 用于开发代码使用
    """
    # 构造初始化函数 定义属性
    def __init__(self, filepath):
        self.filepath = filepath
    # 定义方法 一般读写
    def write_to_file(self, line):
        # 打开文件
        f = open(self.filepath, 'a')
        # 写
        f.write(line)
        f.close()
    # 读操作
    def read_from_file(self):
        f = open(self.filepath, 'r')
        # 读
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
       主函数
    """
    # 设置次数
    try_times = 5
    filepath = 'password_6.0.txt'
    # 实例化文件工具对象
    file_tool = FileTool(filepath)


    while try_times > 0:

        password = input('请输入密码:')
        # 实例化密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_password()


        line = '密码:{},强度:{}\n'.format(password, password_tool.strength_level)
        # 写操作
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格!')
            break
        else:
            print('密码强度不合格!')
            try_times -= 1

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

    # 读操作
    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()