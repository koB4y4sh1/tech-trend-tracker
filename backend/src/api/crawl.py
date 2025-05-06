from fastapi import APIRouter
from src.services.rss_parser import fetch_rss_feed
router = APIRouter()

@router.post("/crawl")
def crawl_rss():
    qiita_url = "https://qiita.com/popular-items/feed.atom"
    zenn_url = "https://zenn.dev/feed"
    qiita_articles = fetch_rss_feed(qiita_url)
    zenn_articles = fetch_rss_feed(zenn_url)
    return {"qiita": qiita_articles, "zenn": zenn_articles}
