from flask import request, jsonify, Blueprint, render_template, flash, redirect, url_for, session, json, Response, send_from_directory, send_file, make_response
from service.ConfigService import ConfigService

config = Blueprint('config', __name__)

class Config:

    @staticmethod
    @config.route('/home')
    def test():
        test = {
            'data': 'data'
        }
        return jsonify(test)


    @staticmethod
    @config.route('/register', methods=['POST', 'GET'])
    def register():
        if request.method == 'POST':
            name = request.args.get('name')
            schema = request.args.get('schema')
            username = request.args.get('username')
            password = request.args.get('password')
            env = request.args.get('environment')
            print("{} {} {} {} {}".format(name, schema, username, password, env))
            exists = ConfigService.checkIfConfigurationExists(name)
            if exists:
                response = {
                    'code': 409,
                    'message': 'Conflict',
                    'data': {
                        'info': 'Configuration not created due to error!',
                        'model': 'Already exists!'

                    }
                }
                return json.dumps(response)
            else:
                return ConfigService.createConfiguration(name, schema, username, password, env)
        else:
            response = {
                'code': 404,
                'message': 'Not Found!',
                'data': {
                    'info': '404',
                    'model': 'Not Found!'

                }
            }
            return json.dumps(response)

    @staticmethod
    @config.route('/<string:name>', methods=['POST', 'GET'])
    def getConfiguration(name):
        return json.dumps(ConfigService.getConfigurationByName(name))
