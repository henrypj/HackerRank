# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 16:51:28 2017

@author: henrypj
"""

from collections import Counter
from itertools import groupby
for _ in range(int(input())):
    n = int(input())
    b = input().strip()
    u = b.count("_")
    c = Counter(b.replace("_", "")).values()
    print(c)
    print("len c => ",len(c))
    print("min c => ",min(c))
    if u:
        print("NO" if len(c) and min(c) == 1 else "YES")
    else:
        ans = "YES"
        for k, g in groupby(b):
            if len(list(g)) < 2:
                ans = "NO"
                break
        print(ans)

