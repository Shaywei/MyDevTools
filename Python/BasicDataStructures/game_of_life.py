import itertools, time

class GameOfLife(object):
    def __init__(self, _board):
        self._board = _board

    def _print(self):
        for row in self._board:
            print ' '.join([str(i) for i in row])

    def next_step_cell(self, i, j):
        num_of_living_neighbohrs = self._accumulate_number_of_living_neighbohrs(i,j)
        if num_of_living_neighbohrs < 2 or num_of_living_neighbohrs > 3:
            return 0
        elif num_of_living_neighbohrs == 2:
            return self._board[i][j] 
        elif num_of_living_neighbohrs == 3:
            return 1

    def _accumulate_number_of_living_neighbohrs(self, i,j):
        # check for boundary conditions:
        num_of_living_neghbohrs = 0
        for position in itertools.product((-1,0,1), (-1,0,1)):
            if position != (0,0):
                try:
                    x_pos = i + position[0]
                    y_pos = j + position[1]
                    if x_pos >= 0 and y_pos >= 0:
                        if self._board[x_pos][y_pos] == 1:
                            num_of_living_neghbohrs += 1
                except:
                    pass
        return num_of_living_neghbohrs    

    def next_step(self):
        next_step_board = []
        for i in range(len(self._board)):
            next_step_board.append([])
            for j in range(len(self._board[i])):
                next_step_board[i].append(self.next_step_cell(i,j))
        self._board = next_step_board


    def run(self):
        while True:
            time.sleep(0.5)
            print '\n'
            self._print()
            self.next_step()

if __name__ == '__main__':
    import random
    gol = GameOfLife([[0,1,0],[0,1,0],[0,1,0]])
    gol.run()