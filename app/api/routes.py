from app.api import api
from app.main.routes import RSS_FEEDS
from flask import jsonify
import feedparser

@api.route('/')
def index():
  return jsonify({ "message": "welcome" })

@api.route('/cnn')
def cnn():
  return get_news('cnn')

@api.route('/fox')
def fox():
  return get_news('fox')

@api.route('/bbc')
def bbc():
  return get_news('bbc')

@api.route('/ioc')
def ioc():
  return get_news('ioc')

def get_news(publication):
  feed = feedparser.parse(RSS_FEEDS[publication])
  articles = feed['entries']
  return jsonify({ "articles": articles })
