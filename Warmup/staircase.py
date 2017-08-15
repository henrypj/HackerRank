import sys

n = int(input().strip())

for i in range(n):
    blankStr = hashStr = ""
    numBlanks = n - i -1
    numHashes = i + 1
    for x in range(numBlanks):
        blankStr += " "
    for x in range(numHashes):
        hashStr += "#"
    print(blankStr + hashStr)