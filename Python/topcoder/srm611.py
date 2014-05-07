import math_utils
'''
Div2 I
Problem Statement
        Fox Ciel thinks that the number 41312432 is interesting. This is because of the following property: There is exactly 1 digit between the two 1s, there are exactly 2 digits between the two 2s, and so on.





Formally, Ciel thinks that a number X is interesting if the following property is satisfied: For each D between 0 and 9, inclusive, X either does not contain the digit D at all, or it contains exactly two digits D, and there are precisely D other digits between them.





You are given a String x that contains the digits of a positive integer. Return "Interesting" if that integer is interesting, otherwise return "Not interesting".
 
Definition
        
Class:  InterestingNumber
Method: isInteresting
Parameters: String
Returns:    String
Method signature:   String isInteresting(String x)
(be sure your method is public)
    
 
Constraints
-   x will correspond to an integer between 1 and 1,000,000,000, inclusive.
-   x will not start with a '0'.
 
Examples
0)  
        
"2002"
Returns: "Interesting"
There are 0 digits between the two 0s, and 2 digits between the two 2s, so this is an interesting number.
1)  
        
"1001"
Returns: "Not interesting"
There should be 1 digit between the two 1s, but there are 2 digits between them. Hence, this number is not interesting.
2)  
        
"41312432"
Returns: "Interesting"
This is the number in the statement.
3)  
        
"611"
Returns: "Not interesting"
There is only one digit 6 in this number, so it's not interesting.
4)  
        
"64200246"
Returns: "Interesting"
5)  
        
"631413164"
Returns: "Not interesting"
This number contains the digit 1 three times.
'''
class  InterestingNumber(object):
    def isInteresting(self,num):
        for i in xrange(10):
            i_str = str(i)
            c = num.count(i_str)
            if c not in [0,2]:
                return 'Not interesting'
            if c == 2 and num[num.index(i_str)+1:].index(i_str) != i:
                return 'Not interesting'
        return 'Interesting'

'''
Problem Statement
        For any non-empty sequence of positive integers s1, s2, ..., sK their least common multiple is the smallest positive integer that is divisible by each of the given numbers. We will use "lcm" to denote the least common multiple. For example, lcm(3) = 3, lcm(4,6) = 12, and lcm(2,5,7) = 70.





You are given a int[] S and an int x. Find out whether we can select some elements from S in such a way that their least common multiple will be precisely x. Formally, we are looking for some s1, s2, ..., sK, K >= 1, such that each si belongs to S, and x=lcm(s1, s2, ..., sK). Return "Possible" if such elements of S exist, and "Impossible" if they don't.
 
Definition
        
Class:  LCMSetEasy
Method: include
Parameters: int[], int
Returns:    String
Method signature:   String include(int[] S, int x)
(be sure your method is public)
    
 
Constraints
-   S will contain between 1 and 50 elements, inclusive.
-   Each element in S will be between 1 and 1,000,000,000, inclusive.
-   Elements in S will be distinct.
-   x will be between 2 and 1,000,000,000, inclusive.
 
Examples
0)  
        
{2,3,4,5}
20
Returns: "Possible"
We can obtain 20 in multiple ways. One of them: 20 = lcm(4, 5).
1)  
        
{2,3,4}
611
Returns: "Impossible"
If S={2,3,4}, the only values we can obtain are 2, 3, 4, 6, and 12.
2)  
        
{2,3,4}
12
Returns: "Possible"
3)  
        
{1,2,3,4,5,6,7,8,9,10}
24
Returns: "Possible"
4)  
        
{100,200,300,400,500,600}
2000
Returns: "Possible"
5)  
        
{100,200,300,400,500,600}
8000
Returns: "Impossible"
6)  
        
{1000000000,999999999,999999998}
999999999
Returns: "Possible"
'''

class LCMSetEasy(object):
    def include(self, nums, target_lcm):
        nums = sorted(nums)

        possible_lcms = set([nums[0]])
        
        for i in xrange(1, len(nums)):
            new_lcms = set()
            
            for lcm in possible_lcms:
                new_lcms.add(math_utils.lcm(nums[i], lcm))

            possible_lcms.add(nums[i])

            for lcm in new_lcms:
                possible_lcms.add(lcm)

            if target_lcm in possible_lcms:
                return "Possible"

        return "Impossible"





