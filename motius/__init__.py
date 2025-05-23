from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def hello_motius():
        return 'Hello, Motius!'
    
    return app