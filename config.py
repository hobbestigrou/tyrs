import os
import ConfigParser

class Config:

    consumer_key = 'Eq9KLjwH9sJNcpF4OOYNw'
    consumer_secret = '3JoHyvBp3L6hhJo4BJr6H5aFxLhSlR70ZYnM8jBCQ'
    
    def __init__ (self):

        configFile = os.environ['HOME'] + '/.config/tyrsrc'
        conf = ConfigParser.RawConfigParser()
        conf.read(configFile)

        self.pseudo             = conf.get('account', 'pseudo')
        self.oauth_token        = conf.get('token', 'oauth_token')
        self.oauth_token_secret = conf.get('token', 'oauth_token_secret')
