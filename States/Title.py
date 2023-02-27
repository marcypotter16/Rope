from pygame import Vector2, Surface

from Rope import Rope
from States.State import State


class Title(State):
    def __init__(self, game):
        super().__init__(game)
        self.rope = Rope(game, Vector2(200, 200), Vector2(500, 200), a_fixed=True)
        print(self.rope)

    def render(self, surface: Surface):
        super().render(surface)
        self.rope.render(surface)

    def update(self, delta_time):
        self.rope.update(delta_time)
        # pass
