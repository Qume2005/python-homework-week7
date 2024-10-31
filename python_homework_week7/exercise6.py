class Exercise6:
    def __init__(self):
        amount = int(input("请输入敌人数量>>"))
        print("\n")
        if amount < 1:
            print("敌人个数异常\n")
            return
        if amount > 40:
            print("增加1000分\n")
            return
        if amount > 30:
            print("增加400分\n")
            return
        if amount > 20:
            print("增加200分\n")
            return
        print("增加100分\n")