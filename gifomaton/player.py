# coding: utf-8

import pygame
from pygame.locals import *
from scene import Scene

class PlayerScene(Scene):

    def __init__(self, name):
        super(PlayerScene,self).__init__()
        self.name = name
        self.font = pygame.font.SysFont('andalemono', 32)

    def inlet(self, events):
        from menu import MenuScene
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.manager.go_to(MenuScene())

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0,0,0))
        title_gfx = self.font.render(self.name, True, (255, 255, 255))
        screen.blit(title_gfx, (470, 364))
