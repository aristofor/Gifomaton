# coding: utf-8
"""
Scene et Manager vite faits, basés sur:
http://stackoverflow.com/questions/14700889/pygame-level-menu-states
TODO : MenuScene affiche le titre, ce sera le menu
"""

import pygame
from pygame.locals import *

class Scene(object):

    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def inlet(self, events):
        raise NotImplementedError


class MenuScene(object):

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


class SceneMananger(object):

    def __init__(self):
        self.go_to(MenuScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
