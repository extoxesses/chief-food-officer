#!/usr/bin/env python

#   _____ ______ ____  
#  / ____|  ____/ __ \ 
# | |    | |__ | |  | |
# | |    |  __|| |  | |
# | |____| |   | |__| |
#  \_____|_|    \____/ 
#
# Chief Food Officer for Java-- dev team


# Python modules
import sys

# Bot modules
from src.cfobot import CfoBot
from src.modules.config import Config

import src.constants.constants as Const

import logging
logging.basicConfig(format=Const.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger('main')


# --- Script ---------

def getEnvPath() :
  path = str(sys.argv[1])
  LOGGER.info('Environment .env file path: ' + path)
  return path


def main():
  if (len(sys.argv) != 2) :
    LOGGER.error('Invalid number of parameter: .env file is required!')
    return

  env_path = getEnvPath()
  config = Config(env_path)
  
  # Start bot
  LOGGER.info('Bot creation')
  cfo = CfoBot(config)
  cfo.startBot()


if __name__ == '__main__':
  main()