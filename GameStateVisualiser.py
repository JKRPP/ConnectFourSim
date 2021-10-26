from typing import List
import pygame
from GameState import GameState

def computeSquares(gs: GameState, squareSize, border) -> List[int]:
        borderSpace = border
        output = []
        for i in range(gs.height):
            for o in range(gs.width):
                output.append([o*squareSize+borderSpace, i*squareSize+borderSpace, squareSize, squareSize])

        return output

def computeTokens(gs: GameState, playerNum, squareSize, border)-> List[int]:
    board = gs.board
    borderSpace = border
    tokenOffset = (int) (squareSize/2)
    output = []

    for i in range(gs.height):
            for o in range(gs.width):
                if(board[o][i] == playerNum):
                    x = o*squareSize+borderSpace+tokenOffset
                    y = (gs.height*squareSize-borderSpace)-(i*squareSize+borderSpace)
                    output.append([x, y])

    return output

class GameStateVisualiser:
    pygame.init() 

    def __init__(self, gs: GameState) -> None:
        self.gs = gs
        self.next = False
        # Set the height and width of the screen
        self.size = [800, 600]
        self.screen = pygame.display.set_mode(self.size)

    def setGS(self, gs: GameState):
        self.gs = gs

    def setNext(self, next):
        self.next = next

    def getNext(self) -> bool:
        return self.next

    def visualise(self):
        BLACK = (  0,   0,   0)
        WHITE = (255, 255, 255)
        BLUE =  (  0,   0, 255)
        GREEN = (  0, 255,   0)
        RED =   (255,   0,   0)

        linewidth = 1
        border = 10

        squareSize = (int) (min((self.size[0]-2*border)/self.gs.width, (self.size[1]-2*border)/self.gs.height))
        tokenSize = (int) (squareSize/3)

        squareCoord = computeSquares(self.gs, squareSize, border)
    
        pygame.display.set_caption("Game State Visualiser")
        done = False
        clock = pygame.time.Clock()

        self.screen.fill(WHITE)

        tokens1 = computeTokens(self.gs,1,squareSize,border)
        tokens2 = computeTokens(self.gs,2,squareSize,border)
        
        for i in range(len(tokens1)):
            pygame.draw.circle(self.screen,RED,tokens1[i],tokenSize)
        for i in range(len(tokens2)):
            pygame.draw.circle(self.screen,BLUE,tokens2[i],tokenSize)

        for i in range(self.gs.height*self.gs.width):
            pygame.draw.rect(self.screen,BLACK, squareCoord[i],width=2)
        
        
        pygame.display.flip()
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                self.next = True

    
    
    #visualise(GameState(10,10,4))