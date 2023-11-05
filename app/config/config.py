
class Config:
    DEBUG = False
    JSONIFY_PRETTYPRINT_REGULAR = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True


# Load all possible configurations
config_dict = {
    'prod': ProductionConfig,
    'dev': DevelopmentConfig,
    'test': TestingConfig
}
