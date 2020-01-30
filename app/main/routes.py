from app.main import main
from flask import render_template, request
import feedparser

RSS_FEEDS = {
  'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
  'cnn': 'http://rss.cnn.com/rss/edition.rss',
  'fox': 'http://feeds.foxnews.com/foxnews/latest',
  'ioc': 'http://www.iol.co.za/cmlink/1.640'
}

@main.route('/')
def index():
  return render_template('index.html')

@main.route('/feed/<string:publication>')
def feeds(publication):
  return get_news(publication)

def get_news(publication):
  feed = feedparser.parse(RSS_FEEDS[publication])
  articles = feed['entries']
  return render_template('news.html', articles=articles, publication=publication)

