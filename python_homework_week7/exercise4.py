class Exercise4:
    def __init__(self):
        score = int(input("请输入分数>>"))
        print("\n")
        if score < 0:
            print("错误数据\n")
            return
        if score > 1200:
            print("S\n")
            return
        if score > 500:
            print("A\n")
            return
        if score > 200:
            print("B\n")
            return
        print("C\n")
        