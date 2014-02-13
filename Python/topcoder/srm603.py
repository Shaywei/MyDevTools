
# SRM 603 Div I

'''
Problem Statement
    
Hero is learning a new algorithm to encode a string. You are given a string s that consists of lowercase letters only. Your task is to simulate the algorithm described below on this string, so that Hero can see how it works.  The algorithm starts with a given input string s and an empty output string t. The execution of the algorithm consists of multiple steps. In each step, s and t are modified as follows:
If the length of s is odd, the middle character of s is added to the end of t, and then deleted from s.
If the length of s is even, the two characters in the middle of s are compared. The smaller one of them (either one in case of a tie) is added to the end of t, and then deleted from s.
If after some step the string s is empty, the algorithm terminates. The output of the algorithm is the final string t.  Return the string t that will be produced by the above algorithm for the given string s.
Definition
    
Class:
MiddleCode
Method:
encode
Parameters:
string
Returns:
string
Method signature:
def encode(self, s):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Notes
-
When comparing letters, the smaller one is the one earlier in the alphabet - i.e., the character with the smaller ASCII code.
Constraints
-
s will contain between 1 and 50 characters, inclusive.
-
Each character in s will be a lowercase letter ('a'-'z').
Examples
0)

    
"word"
Returns: "ordw"
In the first step, 'o' is smaller than 'r', thus 'o' is selected.
After the first step: s="wrd", t="o".
After the second step: s="wd", t="or".
In the third step, 'w' is greater than 'd', thus 'd' is selected.
After the third step: s="w", t="ord".
After the fourth step: s="", t="ordw", and the algorithm terminates.
1)

    
"aaaaa"
Returns: "aaaaa"

2)

    
"abacaba"
Returns: "caabbaa"

3)

    
"shjegr"
Returns: "ejghrs"

4)

    
"adafaaaadafawafwfasdaa"
Returns: "afawadafawafaafsadadaa"
'''

class MiddleCode(object):
    def encode(self, s):
        t = ''
        s = list(s)
        while s != []:
            if len(s) % 2 != 0:
                t += s.pop(len(s)/2 )
            else:
                c1, c2 = s[len(s)/2 - 1], s[len(s)/2]
                if c1 <= c2:
                    t += s.pop(len(s)/2-1)
                    
                else:
                    t += s.pop(len(s)/2)        
            
        return t

# SRM 603 Div2 II
'''
Problem Statement
    
You are given a tuple (integer) A with N elements, where N is even. Note that some elements of A may be negative. You are also given a integer X which is guaranteed to be negative. You must divide the elements of A into N/2 disjoint pairs. (That is, each element of A must be in exactly one of those pairs.) Your goal is to maximize the number of pairs in which the product of the two elements is greater than or equal to X. Return the largest possible number of such pairs.
Definition
    
Class:
SplitIntoPairs
Method:
makepairs
Parameters:
tuple (integer), integer
Returns:
integer
Method signature:
def makepairs(self, A, X):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
-
A will contain between 2 and 50 elements, inclusive.
-
The number of elements in A will be even.
-
Each element in A will be between -1,000,000,000 and 1,000,000,000, inclusive.
-
X will be between -1,000,000,000 and -1, inclusive.
Examples
0)

    
{2,-1}
-1
Returns: 0
One possible pair has product -2, which is lower than needed.
1)

    
{1,-1}
-1
Returns: 1
Here product is -1, it's enough.
2)

    
{-5,-4,2,3}
-1
Returns: 2
If first pair contains numbers -5 and -4, and second contains 2 and 3, both will have positive product.
3)

    
{5,-7,8,-2,-5,3}
-7
Returns: 3
Acceptable splitting is {5,8}, {-7,-5} and {-2,3}.
4)

    
{3,4,5,6,6,-6,-4,-10,-1,-9}
-2
Returns: 4

5)

    
{1000000,1000000}
-5
Returns: 1
Beware overflow.
'''
class SplitIntoPairs(object):
    def makepairs(self, A, X):
        negs = [x for x in A if x < 0]
        
        # If there are an even number of negatives - we won!
        if len(negs) %2 == 0:
            return len(A) / 2
        

        # Lets sort the positives by descending and negs by ascending
                
        positives = sorted([x for x in A if x >= 0])
        negs = sorted(negs)
        negs.reverse() # ascending

        # if we can match two negatives, to two non-negatives - we won!        
        if negs[0]*positives[0] >= X:
            return len(A)/2
        return len(A)/2 - 1
            
