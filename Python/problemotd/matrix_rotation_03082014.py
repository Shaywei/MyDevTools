'''
Matrix Rotation

The bank manager at my local bank recently gave me the algorithm to access the bank's vault. I thought I'd pass on the algorithm to you all for "safe keeping". Basically the vault has a USB port which you'll need to plug in to. Once plugged in the vault will send you an NxN matrix such as the one below.

Monday-Friday the key to the vault is to rotate the matrix 90 degrees clockwise. On Saturday and Sunday you have to rotate the matrix 90 degrees counter-clockwise. My dog accidentally got locked in the vault and the bank manager is no where to be found. Can someone help me write a program to get him out?

matrix=[[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]

#Rotated 90 degrees clockwise
matrix=[[21, 16, 11, 6, 1], 
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]]

#Rotated 90 degrees counter-clockwise
matrix=[[5, 10, 15, 20, 25], 
        [4, 9, 14, 19, 24],
        [3, 8, 13, 18, 23],
        [2, 7, 12, 17, 22],
        [1, 6, 11, 16, 21]]

Bonus points for fewer characters of code.
'''

def martrix_rotate(m, d):
    n=len(m)
    c=[[None]*n for i in range(n)]
    for i,r in enumerate(reversed(m)):
        for j,e in enumerate(r):
            (x,y) = (n-1-j,n-1-i) if d in [1,7] else (j,i)
            c[x][y] = e
    return c

if __name__ == '__main__':
        # Saturday/Sunday are days 1 and 7
        print martrix_rotate(  [[1,2,3,4,5],
                          [6,7,8,9,10],
                          [11,12,13,14,15],
                          [16,17,18,19,20],
                          [21,22,23,24,25]] , 1 )
        '''
        [[5, 10, 15, 20, 25],
         [4, 9, 14, 19, 24],
         [3, 8, 13, 18, 23],
         [2, 7, 12, 17, 22],
         [1, 6, 11, 16, 21]]
        '''


        print martrix_rotate(  [[1,2,3,4,5],
                          [6,7,8,9,10],
                          [11,12,13,14,15],
                          [16,17,18,19,20],
                          [21,22,23,24,25]] , 5 )
        '''
        [[21, 16, 11, 6, 1], 
         [22, 17, 12, 7, 2],
         [23, 18, 13, 8, 3],
         [24, 19, 14, 9, 4],
         [25, 20, 15, 10, 5]]        
        '''


