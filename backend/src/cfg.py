class BaseConfig():
    """App configurations"""
    # todo: use host specific config
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = ''

    """Database configurations"""
    # todo: use host specific config
    DB_NAME = 'travel'
    DB_HOST = 'localhost'
    DB_USER = 'yw'
    DB_PASS = 't3iMfiRVm6'

    @property
    def DATABASE_URI(self):
        return 'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'


class DevConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'pValbRtVMBpUrg'

    @property
    def DATABASE_URI(self):
        return 'sqlite:///:memory:'


class ProdConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = 'B6DE2v8q8tXA6A'


def init():
    # TODO: read environment from settings.cfg, then return the corresponding config class
    return DevConfig()
