import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

numA = 0
for x in range(m):
    if (a + apple[x] >= s) and (a + apple[x] <= t):
        numA += 1

numO = 0
for y in range(n):
    if (b + orange[y] >= s) and (b + orange[y] <= t):
        numO += 1

print(numA)
print(numO)