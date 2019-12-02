class Config(object):
    '''
    common configurations
    '''

class DevelopmentConfig(Config):
    '''
    development configurations
    '''
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    '''
    production configuration
    '''
    DEBUG = False

app_config ={
    'development':DevelopmentConfig,
    'production':ProductionConfig
}