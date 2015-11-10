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
