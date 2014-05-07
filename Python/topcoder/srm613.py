# SRM 613 Div2 I

'''
Problem Statement
        

Cat Taro has a string S. He wants to obtain the string "CAT" from the string S. In a single turn he can choose any character and erase all occurrences of this character in S. He can do as many turns as he wants (possibly zero).

You are given the String S. Return "Possible" (quotes for clarity) if it is possible to obtain the string "CAT" and "Impossible" otherwise.
 
Definition
        
Class:  TaroString
Method: getAnswer
Parameters: String
Returns:    String
Method signature:   String getAnswer(String S)
(be sure your method is public)
    
 
Constraints
-   S will contain between 1 and 50 characters, inclusive.
-   S will contain only uppercase English letters ('A'-'Z').
 
Examples
0)  
        

"XCYAZTX"

Returns: "Possible"

It is possible to obtain string "CAT" in three turns, as follows:

    Erase all characters 'X' (and obtain the string "CYAZT")
    Erase all characters 'Y' (and obtain the string "CAZT")
    Erase all characters 'Z' (and obtain the string "CAT")

1)  
        

"CTA"

Returns: "Impossible"

2)  
        

"ACBBAT"

Returns: "Impossible"

Note that whenever you are erasing a character, you must erase all its occurrences. In this case, it is not possible to erase the first 'A' and keep the second one.
3)  
        

"SGHDJHFIOPUFUHCHIOJBHAUINUIT"

Returns: "Possible"

4)  
        

"CCCATT"

Returns: "Impossible"
'''

class TaroString(object):
    def getAnswer(self, S):
        while S != 'CAT':
            if (len(S) < 3) or (len(S) == 3 and S != 'CAT'):
                return 'Impossible'
            if S[0] == 'C':
                if S[1] == 'A':
                    if S[2] == 'T':
                        S = S.replace(S[3], '')
                    else:
                        S = S.replace(S[2], '')
                else:
                    S = S.replace(S[1], '')
            else:
                S = S.replace(S[0], '')
        return 'Possible'
#ts = TaroString()
#print ts.getAnswer('ACBBAT')

'''
Problem Statement
        

Cat Taro likes to play with his cat friends. Each of his friends currently sits on some coordinate on a straight line that goes from the left to the right. When Taro gives a signal, each of his friends must move exactly X units to the left or to the right.

You are given an int[] coordinates and the int X. For each i, the element coordinates[i] represents the coordinate of the i-th cat before the movement. Return the smallest possible difference between the positions of the leftmost cat and the rightmost cat after the movement.
 
Definition
        
Class:  TaroFriends
Method: getNumber
Parameters: int[], int
Returns:    int
Method signature:   int getNumber(int[] coordinates, int X)
(be sure your method is public)
    
 
Constraints
-   coordinates will contain between 1 and 50 elements, inclusive.
-   Each element of coordinates will be between -100,000,000 and 100,000,000, inclusive.
-   X will be between 0 and 100,000,000, inclusive.
 
Examples
0)  
        

{-3, 0, 1}

3

Returns: 3

The difference 3 is obtained if the cats move from {-3,0,1} to {0,-3,-2}. 

1)  
        

{4, 7, -7}

5

Returns: 4

The difference 4 is obtained if the cats move from {4,7,-7} to {-1,2,-2}. 

2)  
        

{-100000000, 100000000}

100000000

Returns: 0

3)  
        

{3, 7, 4, 6, -10, 7, 10, 9, -5}

7

Returns: 7

4)  
        

{-4, 0, 4, 0}

4

Returns: 4

5)  
        

{7}

0

Returns: 0
'''

class TaroFriends(object):
    def getNumber(self, coordinates, X):
        avg = sum(coordinates)/len(coordinates)
        coordinates = sorted(coordinates)
        #print coordinates
        #print avg
        action_on_avg = None
        
        if abs(coordinates[0] - avg) > abs(coordinates[-1] - avg):
            action_on_avg = 'SUB'
        else:
            action_on_avg = 'ADD'
        
        def f(x, action_on_avg=action_on_avg):
            if x < avg:
                return x + X
            elif x > avg:
                return x - X
            else:
                return x - X if action_on_avg=='SUB' else x + X

        coordinates = map(f, coordinates)
        #print coordinates
        coordinates = sorted(coordinates)
        #print coordinates
        return abs(coordinates[0] - coordinates[-1])
        

#tf = TaroFriends()
#print tf.getNumber([4, 7, -7], 5)
