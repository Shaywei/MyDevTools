


# DP beginner

'''
Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it's not possible to select coins in such a way that they sum up to S. 
'''

def min_comb(coins, S):
    Min = [None] * (S + 1)
    Min[0] = 0
    for i in xrange(1,S+1):
        for j in range(len(coins)):
            if coins[j] <= i and (Min[i] is None or Min[i-coins[j]] + 1 < Min[i]):
                Min[i] = Min[i-coins[j]] + 1
    return Min[S]        

min_comb([1,3,5], 11)

def non_decreasing_sub(seq):
    seq_l = len(seq)
    Max = [1] * seq_l
    for i in range(len(seq)):
        for j in range(i):
            if seq[i] - seq[j] >= 0 and Max[i] < 1 + Max[j]:
                Max[i] = Max[j] + 1
                print Max
    return Max[seq_l-1]

'''
Problem Statement
        
The old song declares "Go ahead and hate your neighbor", and the residents of Onetinville have taken those words to heart. Every resident hates his next-door neighbors on both sides. Nobody is willing to live farther away from the town's well than his neighbors, so the town has been arranged in a big circle around the well. Unfortunately, the town's well is in disrepair and needs to be restored. You have been hired to collect donations for the Save Our Well fund.

Each of the town's residents is willing to donate a certain amount, as specified in the int[] donations, which is listed in clockwise order around the well. However, nobody is willing to contribute to a fund to which his neighbor has also contributed. Next-door neighbors are always listed consecutively in donations, except that the first and last entries in donations are also for next-door neighbors. You must calculate and return the maximum amount of donations that can be collected.

 
Definition
        
Class:    BadNeighbors
Method:    maxDonations
Parameters:    int[]
Returns:    int
Method signature:    int maxDonations(int[] donations)
(be sure your method is public)
    
 
Constraints
-    donations contains between 2 and 40 elements, inclusive.
-    Each element in donations is between 1 and 1000, inclusive.
 
Examples
0)    
        
 { 10, 3, 2, 5, 7, 8 }
Returns: 19
The maximum donation is 19, achieved by 10+2+7. It would be better to take 10+5+8 except that the 10 and 8 donations are from neighbors.
1)    
        
{ 11, 15 }
Returns: 15
2)    
        
{ 7, 7, 7, 7, 7, 7, 7 }
Returns: 21
3)    
        
{ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 }
Returns: 16
4)    
        
{ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 }
Returns: 2926

'''

class BadNeighbors(object):
    def maxDonations(self,seq):
        return max(seq[0] + self.maxDonationsLinear(seq[2:-1]), seq[-1] + self.maxDonationsLinear(seq[1:-2]))
    def maxDonationsLinear(self, seq):
        seq_l = len(seq)
        Max = [0] * seq_l 
        Max[0] = seq[0]
        Max[1] = max(seq[1], seq[0])
        for i in range(2, len(seq)):
            Max[i] = max(Max[i-1], Max[i-2] + seq[i])
        return Max[seq_l-1]
bn = BadNeighbors()


''' Problem Statement for ZigZag


Problem Statement

A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a zig-zag sequence.

For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, sequence, return the length of the longest subsequence of sequence that is a zig-zag sequence. A subsequence is obtained by deleting some number of elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.


Definition

Class:    ZigZag
Method:    longestZigZag
Parameters:    int[]
Returns:    int
Method signature:    int longestZigZag(int[] sequence)
(be sure your method is public)


Constraints
-    sequence contains between 1 and 50 elements, inclusive.
-    Each element of sequence is between 1 and 1000, inclusive.

Examples
0)

{ 1, 7, 4, 9, 2, 5 }
Returns: 6
The entire sequence is a zig-zag sequence.
1)

{ 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 }
Returns: 7
There are several subsequences that achieve this length. One is 1,17,10,13,10,16,8.
2)

{ 44 }
Returns: 1
3)

{ 1, 2, 3, 4, 5, 6, 7, 8, 9 }
Returns: 2
4)

{ 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32 }
Returns: 8
5)

{ 374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
249, 22, 176, 279, 23, 22, 617, 462, 459, 244 }
Returns: 36
'''
class ZigZag(object):
    def longestZigZag(self, seq):
        # dp[i][0] - length of the longest ZigZag subseq such that the difference between the last two elements is positive
        # dp[i][1] - length of the longest ZigZag subseq such that the difference between the last two elements is negative

        # init dp
        dp = []
        for i in range(len(seq)):
            dp.append([1,1])

        for i in range(len(seq)):
            for j in range(i):
                if seq[j]-seq[i] > 0:
                    dp[i][0] = max(dp[i][0], 1 + dp[j][1])
                elif seq[j]-seq[i] < 0:
                    dp[i][1] = max(dp[i][1], 1 + dp[j][0])
        return max([i for subl in dp for i in subl])