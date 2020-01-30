import os
from dotenv import load_dotenv
load_dotenv

class BaseSettings:
  SECRET_KEY=os.environ.get('SECRET_KEY')

  @staticmethod
  def init_app(app):
    pass

class Development(BaseSettings):
  pass

class Production(BaseSettings):
  pass

config = {
  'development': Development,
  'production': Production
}
