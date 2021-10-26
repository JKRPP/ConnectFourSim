from GameState import GameState
from PlayerController import PlayerController

#Simple stategy that, starting from the leftmost coloumn, places tokens equally in all coloumns turn by turn

class TowerBuilder(PlayerController):

    def __init__(self, color) -> None:
        self.currColoumn = 0
        self.color = color

    def makeTurn(self, gs: GameState, lastMoveIllegal=False) -> int:
        if(gs.board[self.currColoumn][gs.height-1] == 0):
            return self.currColoumn
        else:
            while(gs.board[self.currColoumn][gs.height-1] == 0):
                self.currColoumn += 1
            return self.currColoumn