from Game import Game
from States.Title import Title

g = Game()
title = Title(g)
g.state_stack.push(title)
g.slomo_factor = 0.00000005
g.game_loop()
