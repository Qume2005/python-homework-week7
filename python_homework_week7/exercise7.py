class Exercise7:
    def __init__(self):
        user_id = int(input("请输入用户编号>>"))
        print("\n")
        if user_id < 100 or user_id > 1000:
            print("数据异常\n")
            return
        user_level = int(input("请输入用户等级>>"))
        print("\n")
        match user_level:
            case 1:
                print("无权限访问\n")
                return
            case 2:
                print("可读权限\n")
            case 3:
                print("读写权限\n")
        print("文件数据：", str(user_id), "\n")