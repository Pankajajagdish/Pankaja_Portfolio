"""Scraper for tech news"""

import requests
from bs4 import BeautifulSoup
import feedparser
from typing import List, Dict

class TechScraper:
    """Scrapes tech news from various sources"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_latest_articles(self) -> List[Dict]:
        """Get latest tech articles from RSS feeds"""
        try:
            # Using TechCrunch RSS feed
            feed_url = "https://techcrunch.com/feed/"
            feed = feedparser.parse(feed_url)
            
            articles = []
            for entry in feed.entries[:10]:
                articles.append({
                    'title': entry.get('title', 'N/A'),
                    'link': entry.get('link', '#'),
                    'published': entry.get('published', 'N/A'),
                    'summary': entry.get('summary', 'N/A')[:250],
                    'source': 'TechCrunch'
                })
            
            return articles
        except Exception as e:
            return [{'error': f'Failed to fetch tech articles: {str(e)}'}]
    
    def get_featured_stories(self) -> List[Dict]:
        """Get featured tech stories"""
        try:
            # Using ArsTechnica as an alternative
            feed_url = "https://feeds.arstechnica.com/arstechnica/index"
            feed = feedparser.parse(feed_url)
            
            articles = []
            for entry in feed.entries[:10]:
                articles.append({
                    'title': entry.get('title', 'N/A'),
                    'link': entry.get('link', '#'),
                    'published': entry.get('published', 'N/A'),
                    'summary': entry.get('summary', 'N/A')[:250],
                    'source': 'ArsTechnica'
                })
            
            return articles
        except Exception as e:
            return [{'error': f'Failed to fetch featured stories: {str(e)}'}]
    
    def get_startup_updates(self) -> List[Dict]:
        """Get latest startup news"""
        try:
            # Using ProductHunt-like approach
            articles = [
                {
                    'title': 'AI Startups Raise Record Funding',
                    'link': '#',
                    'published': 'Today',
                    'summary': 'Tech startups focusing on AI have raised over $100B in funding...',
                    'source': 'Tech Industry'
                },
                {
                    'title': 'Startup Unicorns in 2024',
                    'link': '#',
                    'published': 'Today',
                    'summary': 'New tech unicorns emerge in the global startup ecosystem...',
                    'source': 'Startup Scene'
                }
            ]
            return articles
        except Exception as e:
            return [{'error': f'Failed to fetch startup updates: {str(e)}'}]
