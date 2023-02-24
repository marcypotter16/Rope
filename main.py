from Game import Game
from States.Title import Title

g = Game()
title = Title(g)
g.state_stack.push(title)
g.settings['fps'] = 60
g.slomo_factor = 0.1
g.game_loop()
