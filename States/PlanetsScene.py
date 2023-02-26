import pygame

from Game import Game
from SolarSystem import SolarSystem, Planet
from States.State import State


class PlanetScene(State):
    def __init__(self, game, solar_system):
        super().__init__(game)
        self.ss = solar_system

    def update(self, delta_time):
        super().update(delta_time)
        self.ss.update(delta_time)
        print([p.pos for p in self.ss.planets])

    def render(self, surface: pygame.Surface):
        super().render(surface)
        self.ss.render(surface)

if __name__ == '__main__':
    g = Game()
    p1 = Planet(pygame.Vector2(g.screen_size[0] / 2, g.screen_size[1] / 2), pygame.Vector2(0, 0), rad=100, mass=1000000)
    p2 = Planet(pygame.Vector2(100, g.screen_size[1] / 2), pygame.Vector2(0, 100), rad=20, mass=100)
    p3 = Planet(pygame.Vector2(150, 400), pygame.Vector2(0, 10), rad=5, mass=1)
    p4 = Planet(pygame.Vector2(1400, g.screen_size[1] / 2), pygame.Vector2(10, -100), rad=20, mass=100)
    ss = SolarSystem(g, [p1, p2, p3, p4])
    ps = PlanetScene(g, ss)
    g.state_stack.push(ps)
    g.slomo_factor = 1
    g.settings['fps'] = 60
    g.game_loop()