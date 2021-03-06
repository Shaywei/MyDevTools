# SRM 602 Dvi2 I

'''
roblem Statement
    
TypoCoder is a programming contest like TopCoder. TypoCoder also has a rating system. There are two types of coders in TypoCoder: brown coders and ciel coders. A brown coder is a coder whose rating is greater than or equal to 1200. A ciel coder is a coder whose rating is less than 1200.  Whenever a new contestant joins TypoCoder, their rating is 500. Cat Lower joined TypoCoder and then competed in some contests. You are given a tuple (integer) rating. For each i (0-based index), rating[i] is Cat Lower's rating after he competed in (i+1) contests.  Return the number of times Cat Lower changed his color (i.e., changed from being a ciel coder to being a brown coder or back).
Definition
    
Class:
TypoCoderDiv2
Method:
count
Parameters:
tuple (integer)
Returns:
integer
Method signature:
def count(self, rating):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
-
rating will contain between 1 and 50 elements, inclusive.
-
Each element of rating will be between 0 and 4000, inclusive.
Examples
0)

    
{1000,1200,1199}
Returns: 2
After the first contest Cat Lower was still a ciel coder. After the second contest his new rating was 1200 which made him a brown coder. (This was the first color change.) After the third contest his new rating was 1199 which made him a ciel coder again. (This was the second color change.)
1)

    
{1500,2200,900,3000}
Returns: 3
The color changed after the first, the third and the fourth competition.
2)

    
{600,700,800,900,1000,1100,1199}
Returns: 0
Cat Lower wasn't a brown coder at any time in this case.
3)

    
{0,4000,0,4000,4000,0,0}
Returns: 4

4)

    
{575,1090,3271,2496,859,2708,3774,2796,1616,2552,3783,2435,1111,526,562}
'''

import operator
class TypoCoderDiv2(object):
    def count(self, rating):
        op = operator.ge
        ans = 0
        
        for r in rating:
            
            if op(r, 1200):
                ans += 1    
                if op == operator.ge:
                    op = operator.lt
                else:
                    op = operator.ge
        
        return ans

        
        
            
        
        
        