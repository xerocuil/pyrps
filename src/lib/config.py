import os
import random
import string
from configparser import ConfigParser
import utils as utils

''' Create config file if absent '''
if not os.path.exists(utils.CONFIG_PATH):
  utils.init_config()

''' Load config file '''
conf = ConfigParser()
conf.read(utils.CONFIG_PATH)

''' Create Config class '''
class Config:
  apptitle = conf['EMPR']['apptitle']
  appdir = conf['EMPR']['appdir']
  debug = conf['EMPR']['debug']
  key = conf['EMPR']['key']
  profile = conf['EMPR']['PROFILE']
  db = conf['EMPR']['db']
