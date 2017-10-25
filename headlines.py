# -*- coding: utf-8 -*-

import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {"bbc": {"name": "BBC News", "url": "http://feeds.bbci.co.uk/news/rss.xml"},
             "desnivel": {"name": "Desnivel", "url": "http://www.desnivel.com/services/rss"}}
    
@app.route("/")
@app.route("/<publication>")

def get_news(publication="bbc"):
    if not publication in RSS_FEEDS.iterkeys():
        publication = "bbc"
    url = RSS_FEEDS.get(publication).get("url")
    feed = feedparser.parse(url)
    first_article = feed['entries'][0]
    page = u"""<html>
      <body>
        <h1>{0} Headlines</h1>
        <b>{1}</b> <br/>
        <i>{2}</i> <br/>
        {3} <br/>
      </body>
    </html>""".format(RSS_FEEDS.get(publication).get("name"),
                      first_article.get("title"),
                      first_article.get("published"),
                      first_article.get("summary"))
    return page

if __name__ == '__main__':
    app.run(port=5000, debug=True)
