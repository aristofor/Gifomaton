# coding: utf-8

import pygame
import time
from pygame.locals import *
from scene import Scene
from os.path import dirname, join
from GIFImage import GIFImage

__all__ = ('DisplayHitboxScene','DisplayTimeoutScene')

class DisplayGifScene(Scene):

    """Affiche un .gif"""

    _pos = None

    def __init__(self, name, next_scene):
        super(DisplayGifScene,self).__init__()
        if name.endswith('.gif'):
            self.gif = GIFImage(join(dirname(__file__),'resources',name))
        self.next_scene = next_scene

    def update(self):
        pass

    def render(self, screen):
        if self.gif:
            if self._pos is None:
                r = screen.get_rect()
                self._pos = (int((r[2] - self.gif.image.size[0]) / 2),
                    int((r[3] - self.gif.image.size[1]) / 2))
            self.gif.render(screen,self._pos)

class DisplayHitboxScene(DisplayGifScene):

    """Affiche un .gif et attend un clic sur hitbox"""

    _hitbox = None

    def __init__(self, name, hitbox, next_scene):
        super(DisplayHitboxScene,self).__init__(name, next_scene)
        if name.endswith('.gif'):
            self.gif = GIFImage(join(dirname(__file__),'resources',name))
        self.hitbox = hitbox

    def inlet(self, events):
        for event in events:
            if self._hitbox and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self._hitbox.collidepoint(event.pos):
                    self.manager.go_to(self.next_scene)
                    break

    def render(self, screen):
        super(DisplayHitboxScene,self).render(screen)
        if self.gif:
            if self._hitbox is None:
                self._hitbox = self.hitbox.move(self._pos)
        #dessine hitbox
        #pygame.draw.rect(screen,(255,255,255), (self._hitbox),1)


class DisplayTimeoutScene(DisplayGifScene):

    """Affiche un .gif et attend timeout ou un clic sur l'écran"""

    _t0 = None
    _timeout = None

    def __init__(self, name, timeout, next_scene):
        super(DisplayTimeoutScene,self).__init__(name, next_scene)
        if name.endswith('.gif'):
            self.gif = GIFImage(join(dirname(__file__),'resources',name))
            self._timeout = timeout*1000

    def update(self):
        """handles timeout"""
        if self._t0:
            self._timeout -= time.time() - self._t0
            if self._timeout <= 0:
                self.manager.go_to(self.next_scene)
        else:
            self._t0 = time.time()

    def inlet(self, events):
        """click anywhere"""
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.manager.go_to(self.next_scene)
                break
