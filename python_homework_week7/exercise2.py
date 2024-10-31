class Exercise2:
    def __init__(self):
        month = int(input("请输入月份>>"))
        print("\n")
        if month > 12 or month < 1:
            print("错误的输入\n")
        if month <= 3:
            print("第一季度\n")
        elif month <= 6:
            print("第二季度\n")
        elif month <= 9:
            print("第三季度\n")
        elif month <= 12:
            print("第四季度\n")
        match month:
            case 1:
                print("一月\n")
            case 2:
                print("二月\n")
            case 3:
                print("三月\n")
            case 4:
                print("四月\n")
            case 5:
                print("五月\n")
            case 6:
                print("六月\n")
            case 7:
                print("七月\n")
            case 8:
                print("八月\n")
            case 9:
                print("九月\n")
            case 10:
                print("十月\n")
            case 11:
                print("十一月\n")
            case 12:
                print("十二月\n")
