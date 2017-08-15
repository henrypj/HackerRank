import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

n = 6
arr = [-4, 3, -9, 0, 4, 1]

negNum = posNum = zeroNum = 0
for i in range(n):
    if arr[i] < 0:
        negNum += 1
    elif arr[i] > 0:
        posNum += 1
    else:
        zeroNum += 1

print("%.6f" % (posNum / n))
print("%.6f" % (negNum / n))
print("%.6f" % (zeroNum / n))