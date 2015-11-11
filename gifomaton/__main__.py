# coding: utf-8

from os import environ
from os.path import join, isdir
import toml
import logging
logging.basicConfig(level=logging.DEBUG)

###############################################################################
# Trouve le dossier de données
try:
    VAR_DIR = environ['GIFOMATON_DATA']
except KeyError:
    from os.path import dirname, realpath
    VAR_DIR = join(dirname(dirname(realpath(__file__))),'var')

if not isdir(VAR_DIR):
    logging.critical("Data directory is missing : {}".format(VAR_DIR))
    raise RuntimeError()

###############################################################################
# Lit la config

_conf_dir = join(VAR_DIR,'conf')
_conf_fname = join(_conf_dir,'frontend.toml')

try:
    with open(_conf_fname) as fp:
        config = toml.load(fp)
except:
    logging.critical("Error reading {}".format(_conf_fname))
    raise


###############################################################################
# main

import pygame
import pygame.camera
from pygame.locals import *
from scene import SceneManager
from menu import MenuScene

black = (0,0,0)

pygame.init()
pygame.camera.init()
screen_size = config['screen_size']
pygame.display.set_caption('Gifomaton')

mode_args = DOUBLEBUF | HWSURFACE
if config['fullscreen']:
    mode_args |= FULLSCREEN
screen = pygame.display.set_mode(screen_size, mode_args)
screen.fill(black)

clock = pygame.time.Clock()

manager = SceneManager(MenuScene())

running = True
while running:
    events = pygame.event.get()
    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
           running = False
    manager.scene.inlet(events)
    manager.scene.update()
    manager.scene.render(screen)
    pygame.display.flip()
    clock.tick()
    #print(clock.get_fps())

pygame.camera.quit()
pygame.quit()
