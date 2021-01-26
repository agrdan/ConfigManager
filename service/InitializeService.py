from main import db
from datasource.entity.Configuration import Configuration

class InitializeService:

    def __init__(self):
        pass

    @staticmethod
    def initialize():
        db.create_all()