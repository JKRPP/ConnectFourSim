from GameState import GameState

class GameLogic:
    def __init__(self, gs: GameState):
        self.GameState = gs

    #place a token of colour 'playerColor' in coloumn 'coloumn'
    def placeToken(self, coloumn, playerColor) -> bool:
        #check if the coloumn is within the boards limits
        if(coloumn < 0):
            print("Player ", playerColor, " tried to place a token in a row below 0")
            return False
        if(coloumn > self.GameState.width-1):
            print("Player ", playerColor, " tried to place a token in a row beyond the board")
            return False
        
        coloumnToPlace = self.GameState.board[coloumn]

        #place the token in the first available slot
        for i in range(self.GameState.height):
            if(coloumnToPlace[i] == 0):
                coloumnToPlace[i] = playerColor
                print("Player ", playerColor, " placed a token in coloumn ", coloumn)
                return True
        
        #if no free space was found, complain and return false
        print("Player ", playerColor, " tried to place a token in a row that was already full")
        return False

    #Check if a player won the game by stacking the required tokens on top of each other
    def checkVerticalWin(self) -> int:
        board = self.GameState.board

        for i in range(self.GameState.width):
            connectedSpaces = 0
            connectedColor = 0

            for o in range(self.GameState.height):
                if (board[i][o] == 0):
                    #if the space is empty, move to the next coloumn
                    break
                if (board[i][o] == connectedColor):
                    #if the space is held by the same player as the last, increase the connected component by 1 and check if the component wins the game
                    connectedSpaces += 1
                    if(connectedSpaces == self.GameState.winNumber):
                        print("Player ", connectedColor, " has a vertical row of ", self.GameState.winNumber)
                        return connectedColor
                else:
                    #if the space is held by another player, reset the size of the component to one and continue
                    connectedSpaces = 1
                    connectedColor = board[i][o]

        #if no component of the required size was found, return 0
        return 0

    def checkHorizontalWin(self) -> int:
        board = self.GameState.board

        for i in range(self.GameState.height):
            connectedSpaces = 0
            connectedColor = 0

            for o in range(self.GameState.width):
                if (board[o][i] == 0):
                    connectedSpaces = 0
                    connectedColor = 0
                    continue
                if (board[o][i] == connectedColor):
                    #if the space is held by the same player as the last, increase the connected component by 1 and check if the component wins the game
                    connectedSpaces += 1
                    if(connectedSpaces == self.GameState.winNumber):
                        print("Player ", connectedColor, " has a horizontal row of ", self.GameState.winNumber)
                        return connectedColor
                else:
                    #if the space is held by another player, reset the size of the component to one and continue
                    connectedSpaces = 1
                    connectedColor = board[o][i]

        #if no component of the required size was found, return 0
        return 0

    def checkDiagonalWin(self) -> int:
        board = self.GameState.board
        width = self.GameState.width
        height = self.GameState.height
        winNum = self.GameState.winNumber

        for i in range(width-(winNum-1)):
            for o in range(height-(winNum-1)):
                connectedSpaces = 0
                connectedColor = 0

                #Check for rows in upward diagonal direction
                for p in range(winNum):
                    currColor = board[i+p][o+p]
                    if(currColor == 0):
                        break
                    if(currColor == connectedColor):
                        connectedSpaces += 1
                        if(connectedSpaces == winNum):
                            print("Player ", connectedColor, " has an upward diagonal row of ", winNum)
                            return connectedColor
                    else:
                        connectedSpaces = 1
                        if(p != 0):
                            break
                        else:
                            connectedColor = currColor

                connectedSpaces = 0
                connectedColor = 0

                #Check for rows in downward diagonal direction
                for p in range(winNum):
                    currColor = board[i+p][height-(o+p+1)]
                    if(currColor == 0):
                        break
                    if(currColor == connectedColor):
                        connectedSpaces += 1
                        if(connectedSpaces == winNum):
                            print("Player ", connectedColor, " has a downward diagonal row of ", winNum)
                            return connectedColor
                    else:
                        connectedSpaces = 1
                        if(p != 0):
                            break
                        else:
                            connectedColor = currColor
        return 0

    #Check if any player won the game in any way
    def checkWin(self) -> int:
        vw = self.checkVerticalWin()
        if(vw != 0):
            return vw
        hw = self.checkHorizontalWin()
        if(hw != 0):
            return hw
        dw = self.checkDiagonalWin()
        if(dw != 0):
            return dw

        return 0