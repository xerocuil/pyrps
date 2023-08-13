import os
from configparser import ConfigParser

CONFLIB = os.path.dirname(os.path.realpath(__file__))
APPLIB = os.path.dirname(CONFLIB)
APPDIR = os.path.dirname(APPLIB)
ENGINE_DIR = os.path.join(APPDIR, 'engine')
USERDIR = os.path.expanduser('~')
CONFIGDIR = os.path.join(USERDIR, '.config/pyttrpg')
CONFIGPATH = os.path.join(CONFIGDIR, 'config.ini')

## Init Config.ini
def init_conf():
  conf = ConfigParser()
  conf["SYSTEM"] = {
      "app_title": "PYTTRPG",
      "app_dir": APPDIR,
      "engine": "dnd",
      "debug": True
    }
  conf["FILES"] = {
      "campaigns": os.path.join(CONFIGDIR,'campaigns'),
      "characters": os.path.join(CONFIGDIR,'characters'),
      "engine_dir": ENGINE_DIR,
      "img": os.path.join(CONFIGDIR,'img')
    }

  ### Write to config.ini
  if not os.path.exists(CONFIGDIR):
    os.makedirs(CONFIGDIR)

  with open(CONFIGPATH, 'w') as conf_data:
    conf.write(conf_data)
    
## Init config if not exists
if not os.path.exists(CONFIGPATH):
  init_conf()
else:
  print("Config file found.")

## Load Config.ini
conf = ConfigParser()
conf.read(CONFIGPATH)

## Init Config class
class Config:
  APP_TITLE=conf['SYSTEM']['app_title']
  ENGINE=conf['SYSTEM']['engine']
  DEBUG=conf['SYSTEM']['debug']
  CAMPAIGNS=conf['FILES']['campaigns']
  CHARACTERS=conf['FILES']['characters']
  ENGINE_DIR=conf['FILES']['engine_dir']
  IMG=conf['FILES']['img']