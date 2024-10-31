def argmax(arr: list[int]):
    max_val = arr[0]
    max_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    
    return max_idx

class Exercise3:
    def __init__(self):
        a = int(input("请输入a>>"))
        print("\n")
        b = int(input("请输入b>>"))
        print("\n")
        c = int(input("请输入c>>"))
        print("\n")
        match argmax([a, c, b]):
            case 0:
                print("a最大\n")
            case 1:
                print("c最大\n")
            case 2:
                print("b最大\n")
        
        
        