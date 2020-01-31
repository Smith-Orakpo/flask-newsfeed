from flask import Flask
from settings import config

def create_app(setting):
  app = Flask(__name__)

  app.config.from_object(config[setting])
  config[setting].init_app(app)

  from app.main.routes import main as main_routes
  from app.api.routes import api as api_routes
  app.register_blueprint(main_routes)
  app.register_blueprint(api_routes)

  return app

