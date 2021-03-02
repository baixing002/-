def main():
    """
        主函数
    :return: 
    """

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
        if strength_level == 3:
            print('恭喜！密码强度合格!')
            break
        else:
            print('密码强度不合格!')
            try_times -= 1

        print()
if __name__ == '__main__':
    main()