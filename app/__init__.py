from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    # Load environment variables from .env file
    load_dotenv()
    # Initialize CORS and allow all origins ( Only for dev environment )
    CORS(app, origins='*')
    # Importing the routes (views)
    from . import routes
    app.register_blueprint(routes.bp)

    return app
