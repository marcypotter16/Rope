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

    def render(self, surface: pygame.Surface):
        super().render(surface)
        self.ss.render(surface)