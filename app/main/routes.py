from app.main import main

@main.route('/')
def index():
  return "Landing Page"