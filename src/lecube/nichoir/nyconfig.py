import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/pi/nichoir-pobot.cfg')


def github_email():
   return config.get('github','email')

def github_login():
   return config.get('github','login')

def github_projet():
   return config.get('github','projet')

def github_password():
   return config.get('github','password')

def consumer_key():
   return config.get('tumblr','consumer_key')

def consumer_secret():
   return config.get('tumblr','consumer_secret')

def oauth_token():
   return config.get('tumblr','oauth_token')

def oauth_secret():
   return config.get('tumblr','oauth_secret')

def tumblr_account():
   return config.get('tumblr','account')
