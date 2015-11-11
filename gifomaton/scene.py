# coding: utf-8
"""
Scene et Manager vite faits, basés sur:
http://stackoverflow.com/questions/14700889/pygame-level-menu-states
TODO : MenuScene affiche le titre, ce sera le menu
"""

import pygame
from pygame.locals import *

__all__ = ('Scene','SceneManager')

class Scene(object):

    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def inlet(self, events):
        raise NotImplementedError



class SceneManager(object):

    def __init__(self, start_scene):
        self.go_to(start_scene)

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
