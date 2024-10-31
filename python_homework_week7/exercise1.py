class Exercise1:
    def __init__(self):
        year = int(input("请输入年份>>"));
        print("\n")
        year = year % 400
        if year == 0:
            print("该年是闰年\n")
            return
        year = year % 100
        if year == 0:
            print("该年是平年\n")
            return
        year = year % 4
        if year == 0:
            print("该年是闰年\n")
            return
        print("该年是平年\n")
