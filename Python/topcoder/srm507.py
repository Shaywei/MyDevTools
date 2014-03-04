# Div2 I

'''
Problem Statement
    
Little Elephant from the Zoo of Lviv likes integers.

You are given an tuple (integer) A. On a single turn, Little Elephant can double (i.e., multiply by 2) any element of A. He may double the same element more than once, if he wants to. He wants to obtain an array in which all elements are equal. Return "YES" (quotes for clarity) if it is possible to do that and "NO" otherwise.
Definition
    
Class:
LittleElephantAndDouble
Method:
getAnswer
Parameters:
tuple (integer)
Returns:
string
Method signature:
def getAnswer(self, A):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
64
Notes
-
The return value is case-sensitive. Make sure that you return the exact strings "YES" and "NO".
Constraints
-
A will contain between 1 and 50 elements, inclusive.
-
Each element of A will be between 1 and 1,000,000,000, inclusive.
Examples
0)

    
{1, 2}
Returns: "YES"
One possible way of making all elements equal is to double the element at index 0.
1)

    
{1, 2, 3}
Returns: "NO"
It's impossible to make all three elements equal in this case.
2)

    
{4, 8, 2, 1, 16}
Returns: "YES"

3)

    
{94, 752, 94, 376, 1504}
Returns: "YES"

4)

    
{148, 298, 1184}
Returns: "NO"

5)

    
{7, 7, 7, 7}
Returns: "YES"
'''

import math
class LittleElephantAndDouble(object):
    def getAnswer(self, A):

        m = min(A)
        for a in A:
            if a % m != 0:
                return 'NO'

        div_by_m = lambda(x): x / m
        A = map(div_by_m, A)

        log2 = lambda(x): math.log(x, 2)
        A = map(log2, A)

        for a in A:
            if math.ceil(a) != a:
                return 'NO'
        return 'YES'


# Div2 II

'''
Problem Statement
    
Little Elephant from the Zoo of Lviv likes strings.

You are given a string A and a string B of the same length. In one turn Little Elephant can choose any character of A and move it to the beginning of the string (i.e., before the first character of A). Return the minimal number of turns needed to transform A into B. If it's impossible, return -1 instead.
Definition
    
Class:
LittleElephantAndString
Method:
getNumber
Parameters:
string, string
Returns:
integer
Method signature:
def getNumber(self, A, B):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
64
Constraints
-
A will contain between 1 and 50 characters, inclusive.
-
B will contain between 1 and 50 characters, inclusive.
-
A and B will be of the same length.
-
A and B will consist of uppercase letters ('A'-'Z') only.
Examples
0)

    
"ABC"
"CBA"
Returns: 2
The optimal solution is to make two turns. On the first turn, choose character 'B' and obtain string "BAC". On the second turn, choose character 'C' and obtain "CBA".
1)

    
"A"
"B"
Returns: -1
In this case, it's impossible to transform A into B.
2)

    
"AAABBB"
"BBBAAA"
Returns: 3

3)

    
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"ZYXWVUTSRQPONMLKJIHGFEDCBA"
Returns: 25

4)

    
"A"
"A"
Returns: 0

5)

    
"DCABA"
"DACBA"
Returns: 2
'''

from collections import Counter
import re

def find_subsequance(subseq, s):
    return True if re.search('.*'.join(subseq), s) else False

class LittleElephantAndString(object):
    def getNumber(self, A, B):
        if A == B:
            return 0

        c1 = Counter(A)
        c2 = Counter(B)
        if c1 != c2:
            return -1

        for i in xrange(len(A)):
            if find_subsequance(B[i:], A):
                return i