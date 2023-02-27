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
    def __init__(self, pos: Vector2, vel: Vector2 = Vector2(0, 0), is_fixed: bool = False, mass: float = 1,
                 forces: list[Vector2] = [Vector2(0, 100)]):
        self.is_fixed = is_fixed
        self.forces = forces
        self.prev_pos = pos
        self.mass = mass
        self.pos, self.vel = pos, vel

    def relax_constraint(self, other, desired_distance):
        direction = other.pos - self.pos
        # print(self.pos, other.pos, desired_distance)
        delta_d = self.pos.distance_to(other.pos) - desired_distance
        aux = .5 * delta_d * direction.normalize()
        if self.is_fixed:
            other.pos -= 2 * aux
        elif other.is_fixed:
            self.pos += 2 * aux
        else:
            self.pos += aux
            other.pos -= aux

    def get_accel(self):
        return vector_sum(self.forces) / self.mass


class Rope:
    def __init__(self, game: Game, a: Vector2, b: Vector2, a_fixed=True, b_fixed=True, num_punti: int = 200):
        self.game = game
        ts = [float(t) / num_punti for t in range(num_punti + 1)]
        self.particles: list[Particle] = []
        self.num_particles = num_punti
        self.desired_distance = a.distance_to(b) / num_punti
        self.a = Particle(a, is_fixed=a_fixed)
        self.b = Particle(b, is_fixed=b_fixed)
        self.particles.append(self.a)
        for t in ts[1:len(ts) - 1]:
            self.particles.append(Particle(self.a.pos.lerp(self.b.pos, t), mass=1))
        self.particles.append(self.b)

    def _jakobsen_particle_update(self):
        for i in range(0, self.num_particles):
            # print(self.particles[i].pos, self.particles[i+1].pos)
            self.particles[i].relax_constraint(self.particles[i + 1], self.desired_distance)
            # direction = self.particles[i].pos - self.particles[i + 1].pos
            # # print(self.pos, other.pos, desired_distance)
            # delta_d = self.particles[i].pos.distance_to(self.particles[i + 1].pos) - self.desired_distance
            # aux = .5 * delta_d * direction.normalize()
            # self.particles[i].pos += aux
            # self.particles[i + 1].pos -= aux

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
