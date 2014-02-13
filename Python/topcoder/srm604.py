
# SRM 604, Div2, I
'''
roblem Statement
    
One day, Fox Ciel looked at the words "tokyo" and "kyoto" and noticed an unusual property: We can split "tokyo" into "to"+"kyo", and then swap those two parts to obtain "kyo"+"to" = "kyoto".  Formally, let S and T be two different strings. We call the pair (S,T) interesting if there are two non-empty strings A and B such that S = A+B and T = B+A. For example, according to this definition, if S="tokyo" and T="kyoto", then the pair (S,T) is interesting, because we can find A="to" and B="kyo".  You are given a tuple (string) words. Return the number of interesting pairs we can find among the elements of words. Only count each pair once. E.g., ("tokyo","kyoto") and ("kyoto","tokyo") is the same interesting pair.
Definition
    
Class:
FoxAndWord
Method:
howManyPairs
Parameters:
tuple (string)
Returns:
integer
Method signature:
def howManyPairs(self, words):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
-
words will contain between 2 and 50 elements, inclusive.
-
Each element of words will contain between 1 and 50 characters, inclusive.
-
Each character in each element of words will be a lowercase letter ('a'-'z').
-
All the elements in words will be pairwise distinct.
Examples
0)

    
{"tokyo", "kyoto"}
Returns: 1
As mentioned in the problem statement, ("tokyo", "kyoto") is an interesting pair.
1)

    
{"aaaaa", "bbbbb"}
Returns: 0
("aaaaa", "bbbbb") is not an interesting pair.
2)

    
{"ababab","bababa","aaabbb"}
Returns: 1
There is one interesting pair: ("ababab","bababa"). Note that for this interesting pair there is more than one way to choose the strings A and B.
3)

    
{"eel", "ele", "lee"}
Returns: 3

4)

    
{"aaa", "aab", "aba", "abb", "baa", "bab", "bba", "bbb"}
Returns: 6

5)

    
{"top","coder"}
Returns: 0
Different elements of words may have different lengths.
'''

from collections import Counter

def are_interesting(word1, word2):
    print 'checking for: ', word1, word2
    for i in range(1,len(word1)):
        print '\t', word1[i:], word1[0:i], word2
        if word1[i:] + word1[0:i] == word2:
            print 'Interesting!'
            return True
    return False

class FoxAndWord(object):
    def howManyPairs(self, words):
        ans = 0
        d = dict()
        for word in words:
            c = Counter(word)
            if str(c) not in d.keys():
                d[str(c)] = [word]
            else:
                d[str(c)].append(word)
        print d
        for key in d.keys():
            if len(d[key]) > 1:
                for i in range(len(d[key])):
                    for j in range(i+1,len(d[key])):
                        if are_interesting(d[key][i], d[key][j]):
                            ans += 1
        return ans

# SRM 604, Div2, II

'''
Problem Statement
    
Fox Ciel has a robot. The robot is located on an infinite plane. At the beginning, the robot starts at the coordinates (0, 0). The robot can then make several steps. The steps are numbered starting from 0.  In each step, Ciel must choose one of two directions for the robot: right (x coordinate increases) or up (y coordinate increases). In step k, the robot will move 3^k units in the chosen direction. It is not allowed to skip a step.  You are given integers x and y. Return "Possible" (quotes for clarity) if it is possible that the robot reaches the point (x,y) after some (possibly zero) steps. Otherwise, return "Impossible".
Definition
    
Class:
PowerOfThreeEasy
Method:
ableToGet
Parameters:
integer, integer
Returns:
string
Method signature:
def ableToGet(self, x, y):

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
-
x will be between 0 and 1,000,000,000, inclusive.
-
y will be between 0 and 1,000,000,000, inclusive.
Examples
0)

    
1
3
Returns: "Possible"untitled
In step 0 Ciel will send the robot right to (1,0). In step 1 she will send it up to (1,3).
1)

    
1
1
Returns: "Impossible"

2)

    
3
0
Returns: "Impossible"

3)

    
1
9
Returns: "Impossible"
Note that it is not allowed to move the robot right in step 0, skip step 1, and then move the robot up in step 2.
4)

    
3
10
Returns: "Possible"

5)

    
1093
2187
Returns: "Possible"

6)

    
0
0
Returns: "Possible"
'''
class PowerOfThreeEasy(object):
    def ableToGet(self, x, y):
        if x == 0 and y == 0:
            return 'Possible'
        else:
            return self.ableToGetRec(x,y,0)

    def ableToGetRec(self, x, y, k):
        ttk = pow(3,k)
        if (x - ttk == 0 and y == 0) or (x == 0 and y - ttk == 0):
            return 'Possible'
        elif x < 0 or y < 0 or (x - ttk < 0 and y - ttk < 0):
            return 'Impossible'
        else:
            ans = 'Possible' if self.ableToGetRec(x - ttk, y, k+1) == 'Possible' or self.ableToGetRec(x, y - ttk, k + 1) == 'Possible' else 'Impossible'
            return ans
