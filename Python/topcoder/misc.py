# DP beginner

'''
Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. 
Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it's not possible to select coins in such a way that they sum up to S. 
'''

def min_comb(coins, S):
    Min = [None] * (S + 1)
    Min[0] = 0
    for i in xrange(1,S+1):
        for j in range(len(coins)):
            if coins[j] <= i and (Min[i] is None or Min[i-coins[j]] + 1 < Min[i]):
                Min[i] = Min[i-coins[j]] + 1
    return Min[S]

#min_comb([1,3,5], 11)

def total_comb(coins, S):
    dp = [None] * (S+1) # dp[i] will represent the number of way to give change for sum i with coins
    dp[0] = set([()]) # There is only one combination to give change for sum zeor.
    for i in xrange(1, S+1):
        for j in xrange(len(coins)):
            c = coins[j]
            if c <= i and (dp[i-c] is not None):
                new_combs = set() if dp[i] is None else dp[i]
                for comb in dp[i-c]:
                    new_combs.add(tuple(sorted(comb + (c,))))
                dp[i] = new_combs
    return (len(dp[S]), dp[S])

total_comb([1,3,5], 11)

def non_decreasing_sub(seq):
    seq_l = len(seq)
    Max = [1] * seq_l
    for i in range(len(seq)):
        for j in range(i):
            if seq[i] - seq[j] >= 0 and Max[i] < 1 + Max[j]:
                Max[i] = Max[j] + 1
                print Max
    return Max[seq_l-1]


class ColorfulRoad:
 def getMin(_, road):
    next = { 'R':'G', 'G':'B', 'B':'R' }
    n = len(road)
    INF = 10**9
    f = [0] * n
    f[n-1] = 0

    # cost if we move from i to j:
    def cost(i, j):
        if road[j] != next[road[i]]:
            return INF
        else:
            return (i-j)**2 + f[j]

    #for each i in reversed order, pick the minimum cost:
    for i in reversed(range(n-1)):
        f[i] = min( cost(i,j) for j in range(i+1, n) )
        print f

    return -1 if f[0] >= INF else f[0]


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