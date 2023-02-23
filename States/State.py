import pygame

from Generic.Stack import Stack
# from UI.Abstract import UICanvas


class State:
    def __init__(self, game):
        self.game = game
        # self.UI: list[UICanvas] = []
        self.render_stack = Stack()
        self.prev_state = None

    def render(self, surface: pygame.Surface):
        surface.fill((0,0,0))
        # for ui_element in self.UI:
        #     ui_element.render(surface)

    def update(self, delta_time):
        # for ui_element in self.UI:
        #     ui_element.update(delta_time)
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack.top()  # ossia l'ultimo elemento dello stack di stati
        self.game.state_stack.push(self)

    def exit_state(self):
        self.game.state_stack.pop()
