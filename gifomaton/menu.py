# coding: utf-8

import pygame
from pygame.locals import *
from scene import Scene
from player import PlayerScene

from models import mock_seqs

class MenuScene(Scene):

    cols = 2
    rows = 2
    _screen_rect = None
    _location = None
    tiles = None
    item_size = (430,310)
    gut = 20

    def __init__(self):
        super(MenuScene, self).__init__()
        self.font = pygame.font.SysFont('andalemono', 64)

        seq = iter(mock_seqs)
        missing = False
        self.tiles = list()
        for y in range(self.rows):
            for x in range(self.cols):
                if not missing:
                    try:
                        i = seq.next()
                        self.tiles.append(
                                {
                                'name': i['name'],
                                'rect': pygame.Rect(
                                    x*(self.item_size[0]+self.gut), y*(self.item_size[1]+self.gut),
                                    self.item_size[0], self.item_size[1] )
                                })
                    except StopIteration:
                        missing = True
                        i = None
        #print self.tiles

    def render(self, screen):
        screen.fill((0,0,0))
        sr = screen.get_rect()
        if sr != self._screen_rect:
            self._screen_rect = sr
            self._location = (
                (sr[2]-( self.cols*(self.item_size[0]+self.gut)-self.gut ))/2,
                (sr[3]-( self.cols*(self.item_size[1]+self.gut)-self.gut ))/2,
            )
        title_gfx = self.font.render('GIFOMATON', True, (255, 255, 255))
        screen.blit(title_gfx, (470, 364))
        for z in self.tiles:
            pygame.draw.rect(screen,(255,0,0), (z['rect']).move(self._location),1)

    def update(self):
        pass

    def inlet(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for z in self.tiles:
                    if z['rect'].collidepoint(event.pos):
                        #print("go_to {}".format(z['name']))
                        self.manager.go_to(PlayerScene(z['name']))
                        break
