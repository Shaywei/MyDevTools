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

'''
Problem Statement
        
Have you ever had a dream, that you were so sure was real? What if you were unable to wake from that dream? How would you know the difference between the dream world and the real world?

To answer this complex puzzle, one of the questions that must be answered is to find out whether the world that you live in can be represented by a chess matrix.

Cells of a matrix are called adjacent if they share an edge. A matrix of zeroes and ones is called a chess matrix if there are no two adjacent cells that share the same value. Hence, in a chess matrix the zeroes and ones have to alternate in the same way the colors alternate on a chessboard:

You are given a String[] board that represents a rectangular grid of cells, with a 0 or a 1 in each cell. Each character of each element of board will be either '0' or '1'. In this grid we selected some rectangular subgrid that is a chess matrix. Return the largest possible area of the selected subgrid.

 
Definition
        
Class:  TheMatrix
Method: MaxArea
Parameters: String[]
Returns:    int
Method signature:   int MaxArea(String[] board)
(be sure your method is public)
    
 
Constraints
-   board will contain between 1 and 100 elements, inclusive.
-   Each element of the board is a string containing between 1 and 100 characters, inclusive.
-   All elements of board will have the same length.
-   Each character of each element of board will be either '0' or '1'.
 
Examples
0)  
        
{"1", 
 "0"}
Returns: 2
The entire board is a chess matrix.
1)  
        
{"0000"}
Returns: 1
The largest possible chess matrix here is just a single cell.
2)  
        
{"01"}
Returns: 2
Again, the entire board is a chess matrix.
3)  
        
{"001",
 "000",
 "100"}
Returns: 2
Each rectangular subgrid is determined by a contiguous range of rows and a contiguous range of columns. The four corners of this grid do not form a valid rectangular subgrid.
4)  
        
{"0"}
Returns: 1
5)  
        
{"101", 
 "010"}
Returns: 6
6)  
        
{"101", 
 "011", 
 "101", 
 "010"}
Returns: 8
7)  
        
{"11001110011000110001111001001110110011010110001011", 
 "10100100010111111011111001011110101111010011100001", 
 "11101111001110100110010101101100011100101000010001", 
 "01000010001010101100010011111000100100110111111000", 
 "10110100000101100000111000100001011101111101010010", 
 "00111010000011100001110110010011010110010011100100", 
 "01100001111101001101001101100001111000111001101010", 
 "11010000000011011010100010000000111011001001100101", 
 "10100000000100010100100011010100110110110001000001", 
 "01101010101100001100000110100110100000010100100010", 
 "11010000001110111111011010011110001101100011100010", 
 "11101111000000011010011100100001100011111111110111", 
 "11000001101100100011000110111010011001010100000001", 
 "00100001111001010000101101100010000001100100001000", 
 "01001110110111101011010000111111101011000110010111", 
 "01001010000111111001100000100010101100100101010100", 
 "11111101001101110011011011011000111001101100011011", 
 "10000100110111000001110110010000000000111100101101", 
 "01010011101101101110000011000110011111001111011100", 
 "01101010011111010000011001111101011010011100001101", 
 "11011000011000110010101111100000101011011111101100", 
 "11100001001000110010100011001010101101001010001100", 
 "11011011001100111101001100111100000101011101101011", 
 "11110111100100101011100101111101000111001111110111", 
 "00011001100110111100111100001100101001111100001111", 
 "10001111100101110111001111100000000011110000100111", 
 "10101010110110100110010001001010000111100110100011", 
 "01100110100000001110101001101011001010001101110101", 
 "10110101110100110110101001100111110000101111100110", 
 "01011000001001101110100001101001110011001001110001", 
 "00100101010001100110110101001010010100001011000011", 
 "00011101100100001010100000000011000010100110011100", 
 "11001001011000000101111111000000110010001101101110", 
 "10101010110110010000010011001100110101110100111011", 
 "01101001010111010001101000100011101001110101000110", 
 "00110101101110110001110101110010100100110000101101", 
 "11010101000111010011110011000001101111010011110011", 
 "10010000010001110011011101001110110010001100011100", 
 "00111101110001001100101001110100110010100110110000", 
 "00010011011000101000100001101110111100100000010100", 
 "01101110001101000001001000001011101010011101011110", 
 "00000100110011001011101011110011011101100001110111", 
 "00110011110000011001011100001110101010100110010110", 
 "00111001010011011111010100000100100000101101110001", 
 "10101101101110111110000011111011001011100011110001", 
 "00101110010101111000001010110100001110111011100011", 
 "01111110010100111010110001111000111101110100111011"}
Returns: 12
'''
class TheMatrix(object):
    def max_area(self, matrix):
        def is_alternating(s):
            for i in xrange(1, len(s)):
                if s[i] == s[i-1]:
                    return False
            return True

        max_area = 0
        rows = len(matrix)
        columns = len(matrix[0])

        # fix two columns 
        for i in xrange(columns):
            for j in xrange(i, columns):
                # Check all possible matrices in those columns
                rows_catagorized = []
                for r in xrange(rows):
                    window = matrix[r][i:j+1]
                    if is_alternating(window):
                        rows_catagorized.append('1') if window[0] == '1' else rows_catagorized.append('0')
                    else:
                        rows_catagorized.append('X')
                max_count = 0
                count_so_far = 0 if rows_catagorized[0] == 'X' else 1
                if len(rows_catagorized) == 1 and rows_catagorized[0] != 'X':
                    max_area = max(max_area, (j+1 - i))
                else:
                    for index in xrange(1, len(rows_catagorized)):
                        if rows_catagorized[index] == 'X':
                            max_count = max(max_count, count_so_far)
                            count_so_far = 0
                        else:
                            if rows_catagorized[index-1] != 'X' and rows_catagorized[index-1] != rows_catagorized[index]:
                                count_so_far += 1
                            else:
                                max_count = max(max_count, count_so_far)
                                count_so_far = 1
                        if index == len(rows_catagorized)-1:
                            max_count = max(max_count, count_so_far)
                max_area = max(max_area, ((j+1 - i) * max_count))
        return max_area




tm = TheMatrix()
#print tm.max_area(["0","1"])




