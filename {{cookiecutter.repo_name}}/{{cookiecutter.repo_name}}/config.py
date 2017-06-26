import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = os.urandom(24)
    WTF_CSRF_ENABLED = True

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    DEBUG = True
                
config = {
"development": DevelopmentConfig,
"production": ProductionConfig
}
