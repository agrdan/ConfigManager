from datasource.entity.Configuration import Configuration
import json


class ConfigurationDto:

    def __init__(self):
        self.name = None
        self.schema = None
        self.user = None
        self.password = None
        self.environment = None
        self.connectionString = None



    @staticmethod
    def fromEntity(entity: Configuration):
        configDto = ConfigurationDto()
        configDto.name = entity.name
        configDto.schema = entity.schema_name
        configDto.user = entity.user
        configDto.password = entity.password
        configDto.environment = entity.environment
        configDto.connectionString = 'mysql+pymysql://{}:{}@localhost:3306/{}'.format(configDto.user, configDto.password, configDto.schema)
        return configDto


    def getJson(self):
        configDto = {
            'name': self.name,
            'schema': self.schema,
            'environment': self.environment,
            'connectionString': self.connectionString
        }

        return configDto

    def __repr__(self):
        return str(self.__dict__)