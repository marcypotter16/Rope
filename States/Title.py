from pygame import Vector2, Surface, Rect

import Text
from Rope import Rope
from States.State import State


class Title(State):
    def __init__(self, game):
        super().__init__(game)
        self.rope = Rope(game, Vector2(200, 200), Vector2(500, 200), a_fixed=True)
        self.text_rect = Rect(400, 0, 1200, 50)
        print(self.rope)

    def render(self, surface: Surface):
        super().render(surface)
        Text.draw_centered_text(self.game.font, surface, "Drag mouse to move the red end of the rope", (255, 255, 255), self.text_rect)
        self.rope.render(surface)

    def update(self, delta_time):
        self.rope.update(delta_time)
        # pass
