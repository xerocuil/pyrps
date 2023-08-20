import os
from configparser import ConfigParser

CONFLIB = os.path.dirname(os.path.realpath(__file__))
APPLIB = os.path.dirname(CONFLIB)
APPDIR = os.path.dirname(APPLIB)
ENGINEDIR = os.path.join(APPDIR, 'engine')
# USERDIR = os.path.expanduser('~')
# CONFIGDIR = os.path.join(USERDIR, '.config/pyrepg')
CONFIGPATH = os.path.join(APPDIR, 'config.ini')

# Functions

## Init Config.ini
def init_conf():
  conf = ConfigParser()
  conf["SYSTEM"] = {
      "APPTITLE": "PyRPS",
      "DEBUG": False,
      "ENGINE": "dnd5",
      "KEY": os.urandom(24).hex(),
    }
  conf["FILES"] = {
      "APPDIR": APPDIR,
      "ENGINEDIR": ENGINEDIR,
    }

  ### Write to config.ini

  # if not os.path.exists(CONFIGPATH):
    # os.makedirs(CONFIGDIR)

  with open(CONFIGPATH, 'w') as conf_data:
    conf.write(conf_data)
    
## Init config if not exists
if not os.path.exists(CONFIGPATH):
  init_conf()
else:
  print("Config file found.")

## Load Config.ini
settings = ConfigParser()
settings.read(CONFIGPATH)

# ## Init Config class
# class Config:
#   APPTITLE=settings['SYSTEM']['APPTITLE']
#   DEBUG=settings['SYSTEM']['debug']
#   ENGINEDIR=settings['FILES']['ENGINEDIR']
#   KEY=settings['SYSTEM']['KEY']