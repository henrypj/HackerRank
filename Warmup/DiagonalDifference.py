import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

d1 = d2 = 0
for x in range(n):
    d1 += a[x][x]
    d2 += a[n-1-x][x]

print(abs(d1 - d2))  
    