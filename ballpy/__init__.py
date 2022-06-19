

from flask import Flask, redirect


def create_app():
    app = Flask(__name__)



    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:VccVcc@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # index route
    @app.route('/')
    def index(): 
        return 'Hello, this is Ball App! Cool!!'


     # return the app 
    return app


