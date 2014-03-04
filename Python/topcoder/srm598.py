# Div2 I
'''
Problem Statement
    
Fox Ciel received a string as a birthday present. However, the string was too long for her, so she decided to make it shorter by erasing some characters.  The erasing process will look as follows:
Find the smallest i such that the i-th character and the (i+1)-th character of the string are same.
If there is no such i, end the process.
Remove the i-th and the (i+1)-th character of the string, and repeat from 1.
  For example, if she receives "cieeilll", she will change the string as follows: "cieeilll" -> "ciilll" -> "clll" -> "cl". You are given a string s. Return the string she will get after she erases characters as described above.
Definition
    
Class:
ErasingCharacters
Method:
simulate
Parameters:
string
Returns:
string
Method signature:
def simulate(self, s):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
64
Constraints
-
s will contain between 1 and 50 characters, inclusive.
-
Each character in s will be a lowercase letter ('a'-'z').
Examples
0)

    
"cieeilll"
Returns: "cl"
This is the example from the statement.
1)

    
"topcoder"
Returns: "topcoder"
She won't erase any characters at all.
2)

    
"abcdefghijklmnopqrstuvwxyyxwvutsrqponmlkjihgfedcba"
Returns: ""

3)

    
"bacaabaccbaaccabbcabbacabcbba"
Returns: "bacbaca"

4)

    
"eel"
Returns: "l"
'''

class ErasingCharacters(object):
    def simulate(self, s):
        s = list(s)
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                i = max(0, i-1)
            else:
                i += 1
        return ''.join(s)

# Div2 II

'''
Problem Statement
    
Fox Ciel has some items. The weight of the i-th (0-based) item is item[i]. She wants to put all items into bins.  The capacity of each bin is 300. She can put an arbitrary number of items into a single bin, but the total weight of items in a bin must be less than or equal to 300.  You are given the tuple (integer) item. It is known that the weight of each item is between 101 and 300, inclusive. Return the minimal number of bins required to store all items.
Definition
    
Class:
BinPackingEasy
Method:
minBins
Parameters:
tuple (integer)
Returns:
integer
Method signature:
def minBins(self, item):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
64
Constraints
-
item will contain between 1 and 50 elements, inclusive.
-
Each element of item will be between 101 and 300, inclusive.
Examples
0)

    
{150, 150, 150, 150, 150}
Returns: 3
You have five items and each bin can hold at most two of them. You need at least three bins.
1)

    
{130, 140, 150, 160}
Returns: 2
For example, you can distribute the items in the following way:
Bin 1: 130, 15
0Bin 2: 140, 160
2)

    
{101, 101, 101, 101, 101, 101, 101, 101, 101}
Returns: 5

3)

    
{101, 200, 101, 101, 101, 101, 200, 101, 200}
Returns: 6

4)

    
{123, 145, 167, 213, 245, 267, 289, 132, 154, 176, 198}
Returns: 8
'''

class BinPackingEasy(object):
    def minBins(self, item):
        item = sorted(item)
        bin = 0
        
        # There can be at most 2 items in a bin!
        while item != []:
            if len(item) == 1:
                return bin + 1
            if item[0] + item[-1] <= 300:
                item.pop(0)
                item.pop(-1)
            else:
                item.pop(-1)
            bin += 1
        return bin
        