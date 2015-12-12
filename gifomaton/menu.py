# coding: utf-8

import pygame
from pygame.locals import *
from scene import Scene
from player import PlayerScene
from capture import CaptureScene

from models import mock_seqs

class MenuScene(Scene):

    cols = 3
    rows = 3
    _screen_rect = None
    _location = None
    item_size = (430,310)
    gut = 10

    # Play hitboxes
    tiles = None
    # Capture command
    captr = None

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
        self.captr = Rect(0,0,0,0)
        #print self.tiles

    def render(self, screen):
        """
        FIXME: hitboxes et rectangles pas alignés (move fautif)
        """
        screen.fill((0,0,0))
        sr = screen.get_rect()
        if sr != self._screen_rect:
            self._screen_rect = sr
            self._location = (
                (sr[2]-( self.cols*(self.item_size[0]+self.gut)-self.gut ))/2,
                (sr[3]-( self.cols*(self.item_size[1]+self.gut)-self.gut ))/2,
            )
            self.captr = Rect(sr[2]/2-60, sr[3]/2-50, 120, 100)
        for z in self.tiles:
            pygame.draw.rect(screen,(255,0,0), (z['rect']).move(self._location),1)

        pygame.draw.rect(screen, (33,31,31), self.captr, 0)
        pygame.draw.circle(screen, (255,0,0), (sr[2]/2, sr[3]/2), 40, 0)
        title_gfx = self.font.render('GIFOMATON', True, (255, 255, 255))
        screen.blit(title_gfx, (470, 364))

    def update(self):
        pass

    def inlet(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.captr.collidepoint(event.pos):
                    self.manager.go_to(CaptureScene())
                    break
                else:
                    for z in self.tiles:
                        if z['rect'].collidepoint(event.pos):
                            #print("go_to {}".format(z['name']))
                            self.manager.go_to(PlayerScene(z['name']))
                            break
