#!/bin/python3

import sys

# Alice is playing an arcade game and wants to climb to the top of the 
# leaderboard. Can you help her track her ranking as she beats each level? 
# The game uses Dense Ranking, so its leaderboard works like this:
#
# * The player with the highest score is ranked number 1 on the leaderboard.
# * Players who have equal scores receive the same ranking number, and the 
#   next player(s) receive the immediately following ranking number.
#
# For example, four players have the scores 100, 90, 90, and 80. Those players
# will have ranks 1, 2, 2, and 3, respectively.
#
# When Alice starts playing, there are already n people on the leaderboard. 
# The score of each player i is denoted by s(i). Alice plays for m levels, 
# and we denote her total score after passing each level j as alice(j). After 
# completing each level, Alice wants to know her current rank.
#
# You are given an array, scores, of monotonically decreasing leaderboard scores, 
# and another array, alice, of Alice's cumulative scores for each level of the 
# game. You must print m integers. The j'th integer should indicate the current 
# rank of alice after passing the j'th level.
# 
# Input Format
# 
# The first line contains an integer, n, denoting the number of players already 
# on the leaderboard. 
# The next line contains n space-separated integers describing the respective 
# values of scores(0), scores(1),...scores(n-1). 
# The next line contains an integer, m, denoting the number of levels Alice beats. 
# The last line contains m space-separated integers describing the respective 
# values of alice(0), alice(1),...alice(m-1).
#
# Constraints
#
# 1 <= n <= 2 x 10**5
# 1 <= m <= 2 x 10**5
# 0 <= scores(i) ,= 10**9 for 0 <= i <= n
# 0 <= alice(j) ,= 10**9 for 0 <= j <= m
# The existing leaderboard, scores, is in descending order
# Alices scores are cumulative, so alice is in ascending order
# 
# Output Format
# 
# Print m integers. The j'th integer should indicate the rank of alice after
# passing the j'th level.


n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here
from bisect import bisect_left
def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)   
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (hi - pos if pos != hi and a[pos] == x else hi - pos + 1)  # don't walk off the end
    
scoresSet = set(scores)
scores = list(scoresSet)
scores.sort()

for score in alice:
    print(binary_search(scores, score))