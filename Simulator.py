from PlayConnectFour import PlayConnectFour
from PlayerController import PlayerController
from Equality import Equality
import numpy as np
import matplotlib.pyplot as plt

pcf = PlayConnectFour(maxTurns=200, width=10, height=10)

turns = []

#Play 10000 games and see who wins more
for i in range(10000):
    p1 = Equality()
    p2 = PlayerController()
    turns.append(pcf.play(p1, p2))

turns_plot = np.array(turns,dtype='int')
x ,y = np.unique(turns_plot, return_counts=True)

#Print exact number of wins (y[0] = Player 1, y[1] = Player 2, y[3] = draw) and share of player 1s Wins
print(y)
print(y[0]/sum(y))

#Show a plot of the wins
plt.bar(x,y)
plt.show()