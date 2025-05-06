import feedparser

def fetch_rss_feed(url: str):
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'summary': entry.summary,
            'url': entry.link,
            'published': entry.published
        })
    return articles
