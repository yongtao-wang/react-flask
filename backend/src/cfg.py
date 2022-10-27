class BaseConfig():
    """App configurations"""
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = ''

    """Database configurations"""
    DB_NAME = 'major'
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = 'yael'

    @property
    def DATABASE_URI(self):
        return 'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'


class DevConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 't3iMfiRVm6'
    DATABASE_URI = 'sqlite:///:memory:'


def init():
    # TODO: read environment from settings.cfg, then return the corresponding config class
    return DevConfig()
