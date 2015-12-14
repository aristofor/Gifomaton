# coding: utf-8

import pygame
from pygame.locals import *
from scene import Scene
from os.path import dirname, join
from GIFImage import GIFImage
class DisplayScene(Scene):

    """Affiche un .gif et attend un clic sur hitbox"""

    _pos = None
    _hitbox = None

    def __init__(self, name, hitbox, next_scene):
        super(DisplayScene,self).__init__()
        if name.endswith('.gif'):
            self.gif = GIFImage(join(dirname(__file__),'resources',name))
        self.hitbox = hitbox
        self.next_scene = next_scene

    def inlet(self, events):
        from menu import MenuScene
        for event in events:
            if self._hitbox and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self._hitbox.collidepoint(event.pos):
                    self.manager.go_to(self.next_scene)
                    break



    def update(self):
        pass

    def render(self, screen):
        if self.gif:
            if self._pos is None:
                r = screen.get_rect()
                self._pos = (int((r[2] - self.gif.image.size[0]) / 2),
                    int((r[3] - self.gif.image.size[1]) / 2))
                self._hitbox = self.hitbox.move(self._pos)
            self.gif.render(screen,self._pos)
        #dessine hitbox
        #pygame.draw.rect(screen,(255,255,255), (self._hitbox),1)
