from GameState import GameState
from PlayerController import PlayerController

#Simple stategy that, starting from the leftmost coloumn, places tokens equally in all coloumns turn by turn

class Equality(PlayerController):

    def __init__(self) -> None:
        self.myGameState: GameState
        self.currColoumn = 0

    def makeTurn(self, gs: GameState, lastMoveIllegal = False) -> int:
        coloumnToPlace = self.currColoumn
        self.currColoumn += 1
        if(self.currColoumn == gs.width):
            self.currColoumn = 0
            
        if(lastMoveIllegal):
            while(gs.board[coloumnToPlace][gs.height-1] != 0):
                coloumnToPlace +=1
                if(coloumnToPlace == gs.width):
                    coloumnToPlace = 0
            self.currColoumn = coloumnToPlace

        return coloumnToPlace