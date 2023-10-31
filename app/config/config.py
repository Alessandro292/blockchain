
class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False


# Load all possible configurations
config_dict = {
    'prod': ProductionConfig,
    'dev': DevelopmentConfig
}
