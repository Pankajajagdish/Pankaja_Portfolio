"""Scraper for HackerNews and general news sources"""

import requests
from bs4 import BeautifulSoup
import feedparser
from typing import List, Dict

class NewsScraper:
    """Scrapes news from HackerNews and other RSS feeds"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_hackernews_top_stories(self) -> List[Dict]:
        """Fetch top stories from HackerNews"""
        try:
            url = "https://news.ycombinator.com/"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            stories = []
            rows = soup.find_all('tr', class_='athing')
            
            for i, row in enumerate(rows[:10]):  # Top 10
                title_cell = row.find('span', class_='titleline')
                if title_cell:
                    link = title_cell.find('a')
                    if link:
                        stories.append({
                            'rank': i + 1,
                            'title': link.text,
                            'url': link.get('href', '#'),
                            'source': 'HackerNews'
                        })
            
            return stories
        except Exception as e:
            return [{'error': f'Failed to fetch HackerNews: {str(e)}'}]
    
    def get_latest_news(self) -> List[Dict]:
        """Fetch latest news using RSS feed"""
        try:
            # Using BBC News RSS feed as example
            feed_url = "http://feeds.bbc.co.uk/news/rss.xml"
            feed = feedparser.parse(feed_url)
            
            articles = []
            for entry in feed.entries[:10]:
                articles.append({
                    'title': entry.get('title', 'N/A'),
                    'link': entry.get('link', '#'),
                    'published': entry.get('published', 'N/A'),
                    'summary': entry.get('summary', 'N/A')[:200],
                    'source': 'BBC News'
                })
            
            return articles
        except Exception as e:
            return [{'error': f'Failed to fetch news: {str(e)}'}]
    
    def get_most_discussed(self) -> List[Dict]:
        """Get most discussed stories"""
        try:
            url = "https://news.ycombinator.com/best"
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            stories = []
            rows = soup.find_all('tr', class_='athing')
            
            for i, row in enumerate(rows[:10]):
                title_cell = row.find('span', class_='titleline')
                if title_cell:
                    link = title_cell.find('a')
                    if link:
                        stories.append({
                            'rank': i + 1,
                            'title': link.text,
                            'url': link.get('href', '#'),
                            'source': 'HackerNews - Most Discussed'
                        })
            
            return stories
        except Exception as e:
            return [{'error': f'Failed to fetch most discussed: {str(e)}'}]
