import os
from main import app, db
from service.InitializeService import InitializeService


def initialize():
    print("initializing")
    InitializeService.initialize()


if __name__ == '__main__':
    initialize()
    app.run(debug=True, host='0.0.0.0')#, port=8080)

