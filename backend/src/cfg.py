class BaseConfig():
    """App configurations"""
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = ''

    """Database configurations"""
    DB_NAME = 'travel'
    DB_HOST = 'localhost'  # TODO: use remote uri
    DB_USER = 'yongtao'
    DB_PASSWORD = 't3iMfiRVm6'

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4'


class DevConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'pValbRtVMBpUrg'

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProdConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = 'B6DE2v8q8tXA6A'


def init():
    return DevConfig()
