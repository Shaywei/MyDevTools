# Div2 I
'''
Problem Statement
    
It's winter time! Time to eat a lot of mandarins with your friends.

You have several bags with mandarins. You are given an tuple (integer) bags. For each i, the i-th element of bags represents the number of mandarins in the i-th bag. You are also given an integer K. You want to choose exactly K bags and distribute them among you and your friends. To be as fair as possible, you want to minimize the difference between the chosen bag with most mandarins and the chosen bag with fewest mandarins. Return the smallest difference that can be achieved.
Definition
    
Class:
WinterAndMandarins
Method:
getNumber
Parameters:
tuple (integer), integer
Returns:
integer
Method signature:
def getNumber(self, bags, K):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
-
bags will contain between 2 and 50 elements, inclusive.
-
Each element of bags will be between 1 and 1,000,000,000, inclusive.
-
K will be between 2 and N, inclusive, where N is the number of elements in bags.
Examples
0)

    
{10, 20, 30}
2
Returns: 10
There are three ways to choose two bags in this case: {10, 20}, {20, 30}, and {10, 30}. Both in the first case and in the second case the difference between the largest and the smallest number of mandarins is 10. In the third case the difference is 20. Thus, the smallest possible difference is 10.
1)

    
{4, 7, 4}
3
Returns: 3

2)

    
{4, 1, 2, 3}
3
Returns: 2

3)

    
{5, 4, 6, 1, 9, 4, 2, 7, 5, 6}
4
Returns: 1

4)

    
{47, 1000000000, 1, 74}
2
Returns: 27
'''
class WinterAndMandarins(object):
    def getNumber(self, bags, K):
        if K in (0,1):
            return 0
            
        ans = 1000001 # infinity
        
        bags = sorted(bags)
        
        for i in range(len(bags) - K + 1):
            sliding_window = bags[i:i+K]
            print sliding_window
            ans = min(ans, sliding_window[-1] - sliding_window[0])
        
        return ans
            

# Div2 II

'''
roblem Statement
    
It's winter time! You have some candies arranged in a row and now you want to choose some of them and give them to your friend.

You are given a tuple (integer) type. Each candy has a type, which is some positive integer. For each i, type[i] represents the type of i-th candy. You want to choose some non-empty subset of candies with the following property: if the number of candies you choose is K, their types must be precisely all the numbers from 1 to K, inclusive. Return the number of different ways to do that. (Two ways are considered different if there exists some candy that is chosen in only one of them.)
Definition
    
Class:
WinterAndCandies
Method:
getNumber
Parameters:
tuple (integer)
Returns:
integer
Method signature:
def getNumber(self, type):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Notes
-
The answer will always fit in a signed 32-bit integer.
Constraints
-
type will contain between 1 and 50 elements, inclusive.
-
Each element of type will be between 1 and 50, inclusive.
Examples
0)

    
{1, 3, 2}
Returns: 3
There are 7 possible non-empty subsets in this case:
(1)
(3)
(2)
(1, 3)
(1, 2)
(3, 2)
(1, 3, 2)
Out of them, only first, fifth and seventh are valid. Thus, the answer is 3.
1)

    
{1, 1, 2}
Returns: 4
Note that the chosen subset can never contain two elements with the same type.
2)

    
{1, 3, 2, 5, 7, 4, 5, 4}
Returns: 9

3)

    
{1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
Returns: 62

4)

    
{2}
Returns: 0
'''

from collections import Counter

class WinterAndCandies(object):
    def getNumber(self, type):

        # check if there is a valid result for K, is so, calculate the number of possible way to get that K.
        
        c = Counter(type)
        
        dp = [0] * 51 # dp[i] = number of possible solutions for K = i
        
        dp[0] = 0
        dp[1] = c[1]
        
        for k in range(2,51):
            if k not in c.keys():
                dp[k] = 0
            else:
                dp[k] = dp[k-1]*c[k]
        return sum(dp)
