import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


if x1 <= x2 and v1 <= v2:
    print("NO")
elif (x2 -x1) % (v1 -v2) == 0:
    print("YES")
else:
    print("NO")

#x1curr = x1
#x2curr = x2
#landSame = False
#outOfRange = False
#while not landSame and not outOfRange:
#    x1curr += v1
#    x2curr += v2
#    if x1curr == x2curr:
#        landSame = True
#    if x1curr > 100000 or x2curr > 100000:
#        outOfRange = True

#if landSame:
#    print("YES")
#else:
#    print("NO")
