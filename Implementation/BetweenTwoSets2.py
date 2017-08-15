import sys
    
def getTotalX(a, b):
    # Complete this function
    total = 0
    print(a[-1])
    print(b[0] + 1)
    print(list(range(a[-1], b[0] + 1)))
    
    for x in list(range(a[-1], b[0] + 1)):
        hold = 0
        for v in a:
            if (x % v == 0): hold += 1
            else: hold = 0; break    
        
        for c in b:
            if (c % x == 0): hold += 1
            else: hold = 0; break       
        if (hold == len(a) + len(b)):
            total += 1
        print("hold  => ", hold)
        print("total => ", total)
    return total    

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

total = getTotalX(a, b)
print(total)