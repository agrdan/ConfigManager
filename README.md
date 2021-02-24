# ConfigManager

Config manager is under heavy development, now only supports adapter for mysql database, but in the future it will support more database adapters.
Security is not provided at all, it's just idea project and can be used in hobby projects, but with some improvements it can be used in production, I guess. 

Config manager is part of the backend services which contains configuration for registered service.
For example, you register your application with basic database connection parameters (schema, user, password) and the service will 
return connection string for your database.
In architecture like this you dont have to worry about publishing your database information or ignore config.py file that you using as part of your project.

Simply prepare your config.json which is not public, in format:
{"appName": "your_app_name","baseUrl": "iot-smart-systems.eu:5001","endpoint": "/configuration", "secretKey":  "random_string"}

and request your configuration from ConfigManager:

code snippet which i use for example:

```python
import requests
from utils.JSONSerializator import JSONSerializator

class Config(JSONSerializator):
    
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = None

    def __init__(self):

        self.appName = None
        self.endpoint = None
        self.connectionUrl = None
        self.readBaseConfig()
        self.readRemoteConfiguration()


    def readBaseConfig(self):
        with open("config.json", "r") as reader:
            test = reader.readlines()
            print(test[0])
            model = JSONSerializator().serialize(test[0])
            self.baseUrl = model.baseUrl
            self.appName = model.appName
            self.endpoint = model.endpoint
            self.SECRET_KEY = model.secretKey


    def readRemoteConfiguration(self):
        url = "http://{}{}/{}".format(self.baseUrl, self.endpoint, self.appName)
        print(url)
        r = requests.get(url)
        response = JSONSerializator().serialize(r.text)
        self.SQLALCHEMY_DATABASE_URI = response.connectionString
```
        
