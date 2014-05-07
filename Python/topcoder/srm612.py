#Div2 I

'''
Problem Statement

Some students are seated in a row next to each other. Each of them is either left-handed or right-handed. You are given a String S that describes the row of students. Each character of S is either 'L' or 'R', representing a left-handed or a right-handed person, respectively. The characters describe the row from the left to the right: for all i, the person described by character i+1 sits to the right of the person described by character i.

The students are trying to write down lecture notes. Whenever a left-handed person sits immediately to the right of a right-handed person, their elbows collide when they both try to write at the same time. Compute and return the number of elbow collisions, assuming that all students in the row attempt to write at the same time.

Definition

Class:  LeftAndRightHandedDiv2
Method: count
Parameters: String
Returns:    int
Method signature:   int count(String S)
(be sure your method is public)

Constraints
-   S will contain between 1 and 50 characters, inclusive.
-   Each character of S will be either 'L' or 'R'.

Examples
0)

"L"

Returns: 0

There's only one person in the row so there are no collisions.
1)

"RRR"

Returns: 0

Everybody is right-handed so there are no collisions.
2)  


"LRLRLR"

Returns: 2

There will be two collisions: one of them between the second and the third person from the left (described by S[1] and S[2]) and the other between the fourth and the fifth person.
3)


"LLLRRR"

Returns: 0

4)


"RLRLRL"

Returns: 3
'''

class LeftAndRightHandedDiv2(object):
    def count(self, s):
        return s.count('RL')

LARHD2 = LeftAndRightHandedDiv2()
print LARHD2.count('RLRLRL')

'''
Problem Statement
You are very happy because you advanced to the next round of a very important programming contest. You want your best friend to know how happy you are. Therefore, you are going to send him a lot of smile emoticons. You are given an int smiles: the exact number of emoticons you want to send.

You have already typed one emoticon into the chat. Then, you realized that typing is slow. Instead, you will produce the remaining emoticons using copy and paste.

You can only do two different operations:

    Copy all the emoticons you currently have into the clipboard.
    Paste all emoticons from the clipboard.

Each operation takes precisely one second. Copying replaces the old content of the clipboard. Pasting does not empty the clipboard. Note that you are not allowed to copy just a part of the emoticons you already have.

Return the smallest number of seconds in which you can turn the one initial emoticon into smiles emoticons.
 
Definition
        
Class:  EmoticonsDiv2
Method: printSmiles
Parameters: int
Returns:    int
Method signature:   int printSmiles(int smiles)
(be sure your method is public)
    
 
Constraints
-   smiles will be between 2 and 1000, inclusive.
 
Examples
0)  
        

2

Returns: 2

First use copy, then use paste. The first operation copies one emoticon into the clipboard, the second operation pastes it into the message, so now you have two emoticons and you are done.
1)  
        

6

Returns: 5

    Copy. This puts one emoticon into the clipboard.
    Paste. You now have 2 emoticons in the message.
    Copy. The clipboard now contains 2 emoticons.
    Paste. You now have 4 emoticons in the message.
    Paste. You now have 6 emoticons in the message and you are done.

2)  
        

11

Returns: 11

3)  
        

16

Returns: 8

4)  
        

1000

Returns: 21
'''

'''
1 -> 0
2 -> 2
3 -> 3
4 -> 4
5 -> 5
6 -> 5
7 -> 7
8 -> 6
9 -> 6
10 -> 7
11 -> 11
13 -> 13
15 -> 5 + 5 + 5
_1000 = _500 + 2 = _250 +4 = _125 +6
125 = 5*5*5 --> _125 = _25 + 5 
25 = 5^2 --> _25 = _5 + 5 = 10
_125 = 15
_1000 = 21

The amount need for X is the amount needed for X/2 + 2 for even numbers!
What about odd numbers?
If X is prime, we must copy once and paste X-1 times
...
General solutions:
Find the smallest prime divisor of X, denote as p, the answer is (the anser for X/p) + p
        * For case of even numbers: 2 is smallest prime factor
        * For case of primes the ans for 1 is 0 ans so it is p.
'''
class EmoticonsDiv2(object):
    def is_prime(self, x):
        i = 2
        while (i*i <= x):
            if (x % i == 0):
                return False
            i+=1
        return True

    def smallest_prime_factor(self, x):
        for i in xrange(2, x+1):
            if (x % i == 0) and self.is_prime(i):
                return i

    def printSmiles(self, num_of_emoticons):
        dp = [None] * (num_of_emoticons + 1)
        dp[1] = 0
        for i in xrange(2, num_of_emoticons+1):
            spf = self.smallest_prime_factor(i)
            dp[i] = dp[i/spf] + spf

        return dp[num_of_emoticons]

EC2 = EmoticonsDiv2()
print EC2.printSmiles(1000)

'''
Problem Statement
        Fox Ciel likes powers of two. She has a bag with some positive powers of two. Note that some powers may occur multiple times in the bag. You are given a long[] powers. Each element of powers is one of the numbers in Ciel's bag.



Ciel likes each non-negative integer that can be written as the sum of some numbers from her bag.



For example, suppose that her bag contains the numbers 2, 4, 4, and 64. In this case, Ciel likes 10 (because 10=2+4+4), 64 (because 64=64), and also 0 (the sum of no numbers). She does not like 1, and she does not like 12 (note that 12=4+4+4 is not valid, as she only has two 4s; 12=4+4+2+2 is also not valid, as she only has one 2).



Return the number of integers Ciel likes.
 
Definition
        
Class:  PowersOfTwo
Method: count
Parameters: long[]
Returns:    long
Method signature:   long count(long[] powers)
(be sure your method is public)
    
 
Constraints
-   powers will contain between 1 and 50 elements, inclusive.
-   Each element of powers is a power of two between 1 and 2^50, inclusive.
 
Examples
0)  
        

{1,2}

Returns: 4

Fox Ciel likes 0, 1, 2 and 3.
1)  
        

{1,1,1,1}

Returns: 5

Fox Ciel likes 0, 1, 2, 3 and 4.
2)  
        

{1,2,2,2,4,4,16}

Returns: 32

3)  
        

{1,32,1,16,32}

Returns: 18

4)  
        

{1048576,1073741824,549755813888,70368744177664,4398046511104,262144,1048576,2097152,8796093022208,
 1048576,1048576,35184372088832,2097152,256,256,256,262144,1048576,1048576,70368744177664,262144,1048576}

Returns: 18432

Lets make a counter of the number of powers of two:
{1, 2, 2, 2, 4, 4, 16} --> 0:1, 1:3, 2:2, 4:1
All the permutations of length 0 - 1
All the permutations of length 1 - len(keys) = 4
All the permutations of length 2 - 7!/3!2!

'''
