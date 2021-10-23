from GameState import GameState
import numpy as np

#Randomised Strategy that places tokens in random coloumns. All other strategies should inherit this class

class PlayerController:
    #Initialise the Player Controller
    def __init__(self) -> None:
        pass

    #Chose wich coloumn (0 <= x < width) to place the token in. If the last chosen coloumn was illegal, the "lastMoveIllegal" variable will be set to true
    def makeTurn(self, gs: GameState, lastMoveIllegal = False) -> int:
        return np.random.randint(0,gs.width)