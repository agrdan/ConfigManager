class Config(object):
    pass



class ProdConfig(Config):
    DEBUG = True
    DBNAME = 'ConfigManager'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:!Lunarstrain123!@localhost:3306/{}'.format(DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "ef98ab76c09s8dfa0s9d8f"
