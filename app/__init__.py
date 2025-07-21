
from flask import Flask
from flask_cors import CORS
from app.routes import api_bp

def create_app():
    app = Flask(__name__)

    CORS(app, origins=["http://localhost:3000"])

    app.register_blueprint(api_bp)

    return app
