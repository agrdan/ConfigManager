from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import ProdConfig

app = Flask(__name__)
app.config.from_object(ProdConfig)
db = SQLAlchemy(app)


from controller.ConfigController import config
app.register_blueprint(config, url_prefix="/configuration")