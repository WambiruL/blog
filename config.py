import os
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://lorraine:1234@localhost/blog'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql://pjclapijgymmvm:f88dd99bd8d0604d2dbcaa46e9168b89ede46838ff84013dd6d0ce64e518e337@ec2-35-171-250-21.compute-1.amazonaws.com:5432/d1kr1244i5niro'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}