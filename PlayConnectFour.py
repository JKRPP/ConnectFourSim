from GameLogic import GameLogic
from GameState import GameState
from GameLogic import GameLogic
from PlayerController import PlayerController

class PlayConnectFour:
    def __init__(self, maxTurns=20, width=7, height=6, rowsToWin=4):
        self.maxTurns = maxTurns
        self.width = width
        self.height = height
        self.rowsToWin = rowsToWin
        self.possibleTurns = self.width*self.height
        pass

    def play(self, p1: PlayerController, p2: PlayerController) -> int:

        gs = GameState(self.height,self.width,self.rowsToWin)
        gl = GameLogic(gs)

        player1 = p1
        player2 = p2

        players = [player1, player2]

        print("Starting game")

        for i in range(self.maxTurns):
            #Select the player currently placing tokens
            playerNum = i%2

            #End the game in a draw if the board is full
            if(i >= self.possibleTurns):
                return 3
            
            #Make the active player make their choice and place their token
            if not (gl.placeToken(players[playerNum].makeTurn(gl.GameState),(playerNum+1))):
                #If the player did not chose a valid coloumn, ask the player to place their token somewhere else
                if not (gl.placeToken(players[playerNum].makeTurn(gl.GameState, True),(playerNum+1))):
                    #If the player chose an illegal coloumn again, award the other player the win
                    playerNum = (i+1)%2
                    return (playerNum+1)
            
            #Check if a player won the game and award the win accordingly
            if(gl.checkWin() != 0):
                    print("Turn ", i)
                    gl.GameState.printState()
                    print("Game over")
                    return (playerNum+1)
                
        #If the maximum amount of turns was exhausted, end the game in a draw
        print("Game over, max turns exhausted")
        return 3