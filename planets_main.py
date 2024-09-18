from Game import Game
from pygame import Vector2
from SolarSystem import SolarSystem, Planet
from States.PlanetsScene import PlanetScene

if __name__ == '__main__':
    g = Game()
    p1 = Planet(Vector2(g.screen_size[0] / 2, g.screen_size[1] / 2), Vector2(0, 0), rad=100, mass=1000000)
    p2 = Planet(Vector2(100, g.screen_size[1] / 2), Vector2(0, 100), rad=20, mass=100)
    p3 = Planet(Vector2(150, 400), Vector2(0, 10), rad=5, mass=1)
    p4 = Planet(Vector2(1400, g.screen_size[1] / 2), Vector2(10, -100), rad=20, mass=100)
    ss = SolarSystem(g, [p1, p2, p3, p4])
    ps = PlanetScene(g, ss)
    g.state_stack.push(ps)
    g.slomo_factor = 1
    g.settings['fps'] = 60
    g.game_loop()