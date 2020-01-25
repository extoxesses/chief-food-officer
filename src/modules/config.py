#!/usr/bin/env python
#
# This class allows to load env configuration variables

from os import environ
from dotenv import load_dotenv


class Config :

  def __init__(self, path) :
    load_dotenv(path)

    self.BOT_NAME = environ['CFO_BOT_NAME']
    self.TOKEN = environ['CFO_TOKEN']
        
    self.API_ID = environ['CFO_API_ID']
    self.API_HASH = environ['CFO_API_HASH']
    
    self.CLIENT_API_ID = environ['CFO_CLIENT_API_ID']
    self.CLIENT_API_HASH = environ['CFO_CLIENT_API_HASH']