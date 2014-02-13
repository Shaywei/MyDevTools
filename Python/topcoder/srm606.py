# SRM 606

# Div2 I

class AlienAndPassword(object):
    def getNumber(self, S):
        '''different_passwords = set()
        for i in xrange(len(S)):
            different_passwords.add(S[0:i] + S[i+1:])    
        return len(different_passwords)'''
        ans = 1
        for i in xrange(1, len(S)):
            ans += 1 if S[i] != S[i-1] else 0
        return ans

aap = AlienAndPassword()

# Div2 II

class AlienAndGame(object):
    def getNumber(self, board):
        width_of_board = len(board)
        length_of_board = len(board[0])
        # Go over all possible lengths for a square, starting form min(w,l) to 2
        for l in xrange(min(width_of_board, length_of_board),1,-1):
            # go over all possbile top left corners of said quare
            for i in xrange(0, width_of_board - l + 1):
                for j in xrange(0, length_of_board - l + 1):
                    # check if that square is possible
                    if self.check_if_square_that_starts_at_i_j_of_length_l_is_possible(board, i, j, l):
                        return l*l
        return 1
    def check_if_square_that_starts_at_i_j_of_length_l_is_possible(self, board, i, j, l):
        # For each of the l rows:
        for k in xrange(l):
            # check the row (starting for i) 
            if board[i+k][j:j+l+1].count('W') not in (l,0):
                return False
        return True
