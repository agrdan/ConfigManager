from utils.DBUtil import DBUtil
from datasource.entity.Configuration import Configuration
from datasource.dto.ConfigurationDto import ConfigurationDto
import json

class ConfigService:

    @staticmethod
    def createConfiguration(name, schema, username, password, environment):
        entity = Configuration.create(name, schema, username, password, environment)
        status, data = DBUtil.insert(entity)
        if status:
            response = {
                'code': 200,
                'message': 'OK',
                'data': {
                    'info': 'Configuration created!',
                    'model': ConfigurationDto.fromEntity(data).getJson()

                }
            }
            return json.dumps(response)
        else:
            response = {
                'code': 500,
                'message': 'Internal server error',
                'data': {
                    'info': 'Configuration not created due to error!',
                    'model': data

                }
            }
            return json.dumps(response)


    @staticmethod
    def checkIfConfigurationExists(name):
        configEntity = DBUtil.findByName(Configuration, name)
        if configEntity is None:
            return False
        else:
            return True


    @staticmethod
    def getConfigurationByName(name):
        entity = DBUtil.findByName(Configuration, name)
        if entity is not None:
            dto = ConfigurationDto.fromEntity(entity).getJson()
            return dto
        else:
            response = {
                'code': 404,
                'message': 'Not Found',
                'data': {
                    'info': 'Configuration not found!',
                    'model': None

                }
            }
            return response