import sys
import functools

def factors(n):    
    return set(functools.reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
def getTotalX(a, b):
    # Complete this function
    total = 0
    xList = []
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
            xList.append(x)
        print("hold  => ", hold)
        print("total => ", total)
    print(xList)
    return total    
    # Determine all factors of list B
#    factsBset = set()
#    for n in b:
#        factsBset.update(factors(n))
#    factsBlist = sorted(factsBset)
##    print(factsBlist)
#    
#    i = 0
#    while i < len(factsBlist):
##        print("factsBlist[i] => ", i, factsBlist[i])
#        if factsBlist[i] == 1:
##            print("Deleting => ", factsBlist[i])
#            del factsBlist[i]
#            i -= 1
#        else:
#            # Check to see if numbers in A are factors of numbers in B
#            for n in a:
##                print("n => ", n)
#                # Delete number from B if A is not a factor of it
#                if factsBlist[i] % n != 0:
##                    print("Deleting => ", factsBlist[i])
#                    del factsBlist[i]
#                    i -= 1
#        i += 1
##    print(factsBlist)       
#    
#    # Check to see if facts in factsBlist are factos of all elements in B
#    i = 0
#    while i < len(factsBlist):
#        for fact in b:
#            if fact % factsBlist[i] != 0:
#                del factsBlist[i]
#                i -= 1
#        i += 1
##    print(factsBlist)
#    return len(factsBlist)

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))


total = getTotalX(a, b)
print(total)