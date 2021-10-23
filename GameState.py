from numpy import string_


class GameState:

    #initialise a Game with m coloumns of height n
    def __init__(self, n, m, w) -> None:
        self.height = n
        self.width = m
        self.winNumber = w

        self.board = []

        #initialise the board (board = board[coloumn][row])
        for i in range(m):
            column_elements = []
            for o in range(n):
                column_elements.append(0)
            self.board.append(column_elements)

    def printState(self):
        for i in range(self.height):
            rowOutput = ""
            for o in range(self.width):
                rowOutput += (str(self.board[o][self.height-(i+1)])+" ")
            print(rowOutput)