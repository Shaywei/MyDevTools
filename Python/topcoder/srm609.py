'''
Problem Statement for MagicalStringDiv2


Problem Statement
        Magical Girl Illy uses "magical strings" to cast spells. For her, a string X is magical if and only if there exists a positive integer k such that X is composed of k consecutive '>' characters followed by k consecutive '<' characters. 

Once Illy picked up a String S. The length of S was even, and each character of S was either '<' or '>'. Illy wants to change S into a magical string. In each step, she can change a single '>' to a '<' or vice versa. Compute and return the smallest number of steps in which she can change S into a magical string.
 
Definition
        
Class:  MagicalStringDiv2
Method: minimalMoves
Parameters: String
Returns:    int
Method signature:   int minimalMoves(String S)
(be sure your method is public)
    
 
Constraints
-   S will contain between 2 and 50 characters, inclusive.
-   S will contain even number of characters.
-   Each character of S will be '<' or '>'.
 
Examples
0)  
        
">><<><"
Returns: 2
She needs to change character 2 (0-based index) from '<' to '>', and character 4 from '>' to '<'.
1)  
        
">>>><<<<"
Returns: 0
S is already a magical string, so no changes are needed.
2)  
        
"<<>>"
Returns: 4
3)  
        
"<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"
Returns: 20
'''

class MagicalStringDiv2(object):
    def minimalMoves(self, s):
        c = 0
        mid = len(s) / 2
        for i in xrange(len(s)):
            if (i < mid) and s[i] != '>':
                c += 1
            elif i >= mid and s[i] != '<':
                c += 1
        return c

'''
Problem Statement
        We have R red, G green, and B blue balls. We want to divide them into as few packages as possible. 
        Each package must contain 1, 2, or 3 balls. 
        Additionally, each package must be either a "normal set" (all balls in the package have the same color), or 
        a "variety set" (no two balls have the same color). 
        Compute and return the smallest possible number of packages.
 
Definition
        
Class:  PackingBallsDiv2
Method: minPacks
Parameters: int, int, int
Returns:    int
Method signature:   int minPacks(int R, int G, int B)
(be sure your method is public)
    
 
Constraints
-   R, G, and B will each be between 1 and 100, inclusive.
 
Examples
0)  
        
4
2
4
Returns: 4
We have 4 red, 2 green, and 4 blue balls. Clearly, we need at least four packages to store 10 balls. One possibility of using exactly four packages looks as follows: RGB, RG, RR, BBB. (I.e., the first package has 1 ball of each color, the second package has a red and a green ball, and so on.)
1)  
        
1
7
1
Returns: 3
Here the only possible solution is to have one package with RGB and two packages with GGG each.
2)  
        
2
3
5
Returns: 4
3)  
        
78
53
64
Returns: 66
4)  
        
100
100
100
Returns: 100
'''

class PackingBallsDiv2(object):
    def minPacks(self, reds, greens, blues):
        ans = min(reds, greens, blues)

        # first, take all the 1-1-1 combinations possible
        reds -= ans
        greens -= ans
        blues -= ans

        # then take all the homogenious 3s possible
        amount = reds / 3
        ans += amount
        reds -= 3 * amount

        amount = greens / 3
        ans += amount
        greens -= 3 * amount

        amount = blues / 3
        ans += amount
        blues -= 3 * amount        

        # Now we have one of the following situations: {0,0,0} {0, 1, ,1}, {0, 2, 1}, {0, 2 2}
        if set((reds, greens, blues)) == set((0, 0, 0)):
            return ans
        elif set((reds, greens, blues)) == set((0, 1, 1)):
            return ans + 1

        return ans + 2

pb2 = PackingBallsDiv2()

'''
Problem Statement
        Vocaloids Gumi, Ia, and Mayu love singing. They decided to make an album composed of S songs. Each of the S songs must be sung by at least one of the three Vocaloids. It is allowed for some songs to be sung by any two, or even all three Vocaloids at the same time. The number of songs sang by Gumi, Ia, and Mayu must be gumi, ia, and mayu, respectively. 

They soon realized that there are many ways of making the album. Two albums are considered different if there is a song that is sung by a different set of Vocaloids. Let X be the number of possible albums. Since the number X can be quite large, compute and return the number (X modulo 1,000,000,007).
 
Definition
        
Class:  VocaloidsAndSongs
Method: count
Parameters: int, int, int, int
Returns:    int
Method signature:   int count(int S, int gumi, int ia, int mayu)
(be sure your method is public)
    
 
Constraints
-   S will be between 1 and 50, inclusive.
-   gumi, ia and mayu will be each between 1 and S, inclusive.
 
Examples
0)  
        
3
1
1
1
Returns: 6
In this case, there are 3 songs on the album. And Gumi, Ia, Mayu will each sing one song. There are 3*2*1 = 6 ways how to choose which Vocaloid sings which song.
1)  
        
3
3
1
1
Returns: 9
Gumi will sing all three songs. Ia and Mayu can each choose which one song they want to sing.
2)  
        
50
10
10
10
Returns: 0
It is not possible to record 50 songs if each Vocaloid can only sing 10 of them.
3)  
        
18
12
8
9
Returns: 81451692
4)  
        
50
25
25
25
Returns: 198591037
'''

import itertools
class VocaloidsAndSongs(object):
    def count(self, S, gumi, ia, mayu):
        self.dp = [[[[-1 for i in xrange(mayu+1)] for i in xrange(ia+1)] for i in xrange(gumi+1)] for i in xrange(S+1)]
        return self.count_rec(S, gumi, ia, mayu) % 1000000007
    def count_rec(self, S, gumi, ia, mayu):
        res = self.dp[S][gumi][ia][mayu]
        if res == -1:
            if S == 0:
                res = 1 if gumi == 0 and ia == 0 and mayu == 0 else 0
            else:
                res = 0
                new_g = [gumi] if gumi == 0 else [gumi, gumi-1]
                new_i = [ia] if ia == 0 else [ia, ia-1]
                new_m = [mayu] if mayu == 0 else [mayu, mayu-1]
                for g in new_g:
                    for i in new_i:
                        for m in new_m:
                            if g != gumi or i != ia or m != mayu:
                                res = res + self.count_rec(S-1, g, i, m)
            #print 'putting', res, 'in', S, gumi, ia, mayu
            self.dp[S][gumi][ia][mayu] = res
        return res
                            

vas = VocaloidsAndSongs()
#print vas.count(50, 25, 25, 25)


'''
Problem Statement
        Magical Girl Illy uses "magical strings" to cast spells. For her, a string X is magical if and only if there exists a non-negative integer k such that X is composed of k consecutive '>' characters followed by k consecutive '<' characters. Note that the empty string is also magical (for k=0). 

Once Illy picked up a String S. Each character of S was either '<' or '>'. 
Illy can change S by removing some of its characters. 
(The characters she does not remove will remain in their original order.) 
Illy wants to change S into a magical string by removing as few of its characters 
as possible. 

You are given the String S. Compute and return the length of the magical 
string Illy will obtain from S.
 
Definition
        
Class:  MagicalStringDiv1
Method: getLongest
Parameters: String
Returns:    int
Method signature:   int getLongest(String S)
(be sure your method is public)
    
 
Constraints
-   S will contain between 1 and 50 characters, inclusive.
-   Each character of S will be '<' or '>'.
 
Examples
0)  
        
"<><><<>"
Returns: 4
The longest magical string Illy can produce is ">><<". Its length is 4. 
To change S into ">><<", Illy must remove the characters at 0-based indices 
0, 2, and 6.

1)  
        
">>><<<"
Returns: 6
S is already a magical string. Therefore Illy doesn't have to remove any character.
2)  
        
"<<<>>>"
Returns: 0
Illy has to remove all characters of S.
3)  
        
"<<<<><>>><>>><>><>><>>><<<<>><>>>>><<>>>>><><<<<>>"
Returns: 24
'''



class MagicalStringDiv1(object):
    def getLongest(self, s):
        # To remove as little as possible = getting the longest.
        # We need to know what is the longest continous subseries
        # Iterate over the string from left to right and keep count of how many '>'s
        # Iterate over the string from right to left and keep count of how many '<'s
        ans = 0

        gts = 0
        count_gts = []
        for i in xrange(len(s)):
            if s[i] == '>':
                gts += 1
            count_gts.append(gts)

        lts = 0
        for i in reversed(xrange(len(s))):
            if s[i] == '<':
                lts += 1
            
            ans = ans if min(lts, count_gts[i]) < ans else min(lts, count_gts[i])

        return ans*2


msd2 = MagicalStringDiv2()
#print msd2.getLongest('<<<<><>>><>>><>><>><>>><<<<>><>>>>><<>>>>><><<<<>>')

