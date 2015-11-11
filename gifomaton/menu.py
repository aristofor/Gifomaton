# coding: utf-8

import pygame
from pygame.locals import *
from scene import Scene

class MenuScene(Scene):

    def __init__(self):
        super(MenuScene, self).__init__()
        self.font = pygame.font.SysFont('andalemono', 64)

    def render(self, screen):
        text1 = self.font.render('GIFOMATON', True, (255, 255, 255))
        screen.blit(text1, (450, 320))

    def update(self):
        pass

    def inlet(self, events):
        for e in events:
            if e.type == KEYDOWN and e.key == K_SPACE:
                self.manager.go_to(GameScene(0))
