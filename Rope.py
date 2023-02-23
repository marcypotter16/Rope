import os

import pygame.draw
from pygame import Vector2, Surface

from Game import Game

def vector_sum(vectors: list[Vector2]):
    s = Vector2(0, 0)
    for v in vectors:
        s += v
    return s


class Force:
    def __init__(self):
        pass

class ConstantForce(Force):
    earth_gravity = Vector2(0, -0.001)
    def __init__(self):
        super().__init__()


class Particle:
    def __init__(self, pos: Vector2, vel: Vector2 = Vector2(0, 0), mass: float = 1, forces: list[Vector2] = [Vector2(0, 0.001)]):
        self.forces = forces
        self.prev_pos = pos
        self.mass = mass
        self.pos, self.vel = pos, vel

    def relax_constraint(self, other, desired_distance):
        direction = self.pos - other.pos
        print(self.pos, other.pos, desired_distance)
        delta_d = self.pos.distance_to(other.pos) - desired_distance
        aux = .5 * delta_d * direction.normalize()
        self.pos += aux
        other.pos -= aux

    def get_accel(self):
        return self.mass * vector_sum(self.forces)


class Rope:
    def __init__(self, game: Game, a: Vector2, b: Vector2, a_fixed = True, b_fixed = True, num_punti: int = 40):
        self.game = game
        ts = [float(t) / num_punti for t in range(num_punti + 1)]
        self.particles: list[Particle] = []
        self.num_particles = num_punti
        self.desired_distance = a.distance_to(b) / num_punti
        self.a = Particle(a)
        self.b = Particle(b)
        for t in ts:
            self.particles.append(Particle(self.a.pos.lerp(self.b.pos, t)))

    def _jakobsen_particle_update(self):
        for i in range(1, self.num_particles - 2):
            # print(self.particles[i].pos, self.particles[i+1].pos)
            self.particles[i].relax_constraint(self.particles[i+1], self.desired_distance)

    def _verlet_forces_update(self, dt: float):
        for i, particle in enumerate(self.particles):
            if i == 0 or i == self.num_particles:
                pass
            else:
                position_copy = particle.pos.copy()
                particle.pos = 2 * particle.pos - particle.prev_pos + dt * dt * particle.get_accel()
                particle.prev_pos = position_copy

    def update(self, dt: float):
        self._verlet_forces_update(dt)
        self._jakobsen_particle_update()

    def render(self, surf: Surface):
        pygame.draw.lines(surf, pygame.Color("white"), closed=False, points=[p.pos for p in self.particles], width=3)

    def __str__(self):
        return f"Corda:\n{[(p.pos.x, p.pos.y) for p in self.particles]}"


if __name__ == '__main__':
    g = Game(basedir=os.getcwd())
    v1 = Vector2(100, 100)
    v2 = Vector2(200, 200)
    r = Rope(g, v1, v2)
    print(r)
