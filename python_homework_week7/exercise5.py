class Exercise5:
    def __init__(self):
        a = int(input("请输入a边>>"))
        print("\n")
        b = int(input("请输入b边>>"))
        print("\n")
        c = int(input("请输入c边>>"))
        print("\n")
        if a < 0 or b < 0 or c < 0:
            print("这个不是三角形\n")
            return
        condition1 = a + b > c and abs(a - b) < c;
        condition2 = b + c > a and abs(b - c) < a;
        condition3 = a + c > b and abs(a - c) < b;
        if condition1 and condition2 and condition3:
            print("这个是三角形\n")
            return
        print("这个不是三角形\n")