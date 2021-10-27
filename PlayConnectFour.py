from GameLogic import GameLogic
from GameState import GameState
from GameLogic import GameLogic
from PlayerController import PlayerController
from GameStateVisualiser import GameStateVisualiser

import numpy as np
import pygame

class PlayConnectFour:
    def __init__(self, maxTurns=20, width=7, height=6, rowsToWin=4):
        self.maxTurns = maxTurns
        self.width = width
        self.height = height
        self.rowsToWin = rowsToWin
        self.possibleTurns = self.width*self.height
        pass

    def play(self, p1: PlayerController, p2: PlayerController, visualise: bool) -> int:

        gs = GameState(self.height,self.width,self.rowsToWin)
        gl = GameLogic(gs)
        if(visualise):
            gsv = GameStateVisualiser(gs)

        clock = pygame.time.Clock()

        player1 = p1
        player2 = p2

        players = [player1, player2]

        for i in range(self.maxTurns):
            next = False

            #Let player 2 start in 50% of games
            if(i == 0):
                if(np.random.randint(0,2) == 0):
                    self.maxTurns += 1
                    print("Starting player is player ", 2)
                    continue
                print("Starting player is player ", 1)
            
            #Select the player currently placing tokens
            playerNum = i%2

            #End the game in a draw if the board is full
            if(i >= self.possibleTurns):
                return 3
            
            #Make the active player make their choice and place their token
            tokenPos = players[playerNum].makeTurn(gl.GameState)

            if not (gl.placeToken(tokenPos,(playerNum+1))):
                #If the player did not chose a valid coloumn, ask the player to place their token somewhere else
                tokenPos = players[playerNum].makeTurn(gl.GameState, True)

                if not (gl.placeToken(tokenPos,(playerNum+1))):
                    #If the player chose an illegal coloumn again, award the other player the win
                    print("Player ", i+1, " has made an illegal move again after being warned. The player was punished with a loss.")
                    playerNum = (i+1)%2
                    return (playerNum+1)

            if(visualise):
                gsv.setGS(gl.GameState)
                gsv.visualise()

                while not next:
                    clock.tick(10)
                    for event in pygame.event.get(): # User did something
                        if event.type == pygame.QUIT: # If user clicked close
                            return 4
                        if event.type == pygame.KEYDOWN:
                            next = True

            #Check if a player won the game and award the win accordingly
            if(gl.checkWin() != 0):
                    print("Turn ", i)
                    #gl.GameState.printState()
                    print("Game over")

                    return (playerNum+1)
                
        #If the maximum amount of turns was exhausted, end the game in a draw
        print("Game over, max turns exhausted")
        return 3