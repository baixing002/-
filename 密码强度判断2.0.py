"""
   作者：白星
   功能：判断密码强弱
   版本：1.0
   日期：08/16/20
   新增功能：限制密码次数，循环终止
"""

def check_number_exist(password_str):
    """
        判断字符串中是否含有数字
    """
    has_number = False

    for c in password_str:
        if c.isnumeric():
            has_number = True
            break

    return has_number


def check_letter_exist(password_str):
    """
        判断字符串中是否含有字母
    """
    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
       主函数
    """
    # 设置次数
    try_times = 5

    while try_times > 0 :

        password = input('请输入密码:')

        # 密码强度
        strength_level = 0

        # 规则1：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位！')

        # 规则2 ：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码需求包含数字！')

        # 规则3 包含字母
        if check_letter_exist(password):
            strength_level +=1
        else:
            print('密码需求包含字符！')

        if strength_level == 3:
            print('恭喜！密码强度合格!')
            break
        else:
            print('密码强度不合格!')
            try_times -= 1

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

if __name__ == '__main__':
    main()