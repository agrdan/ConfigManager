from main import db
import uuid
from datetime import datetime as dt

class Configuration(db.Model):
    __tablename__ = 'configuration'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), unique=True)
    token = db.Column(db.String(255), unique=True)
    schema_name = db.Column(db.String(30))
    user = db.Column(db.String(20))
    password = db.Column(db.String(64))
    environment = db.Column(db.String(20))
    created = db.Column(db.String(20))


    @staticmethod
    def create(name, schema, user, password, environment):
        config = Configuration()
        config.name = name
        config.schema_name = schema
        config.user = user
        config.password = password
        config.environment = environment
        config.token = uuid.uuid4()
        config.created = str(int(dt.now().timestamp()))
        return config