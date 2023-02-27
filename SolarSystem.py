import pygame.draw
from pygame import Vector2

from Game import Game
def round_vector(vec):
    return Vector2(round(vec.x), round(vec.y))

class Planet:
    def __init__(self, pos: Vector2, vel: Vector2, rad: float, mass: float):
        self.pos, self.vel, self.rad = pos, vel, rad
        self.mass = mass
        self.acc: Vector2 = Vector2(0, 0)

    def update(self, dt):
        print("DT:", dt)
        print(self.pos, self.vel, dt * self.vel, self.pos + self.vel * dt)
        # self.pos += self.vel * .016
        self.pos += self.vel * dt
        # self.pos = round_vector(self.pos)
        self.vel += self.acc * 0.16
        # Resets the acceleration
        self.acc = Vector2(0, 0)

    def render(self, surf):
        pygame.draw.circle(surf, (255, 255, 255), self.pos, self.rad)


class SolarSystem:
    GRAV_CONST = 1

    def __init__(self, game, planets: list[Planet]):
        self.game = game
        self.planets = planets
        self.num_planets = len(planets)

    def update(self, dt):
        self.calc_accel()
        for p in self.planets:
            p.update(dt)

    def render(self, surf):
        for p in self.planets:
            p.render(surf)

    def calc_accel(self):
        for i in range(self.num_planets):
            for j in range(i + 1, self.num_planets):
                p, other = self.planets[i], self.planets[j]
                force = (self.GRAV_CONST * p.mass * other.mass / p.pos.distance_squared_to(other.pos)) * (
                            other.pos - p.pos).normalize()
                p.acc += force / p.mass
                other.acc += -force / other.mass
