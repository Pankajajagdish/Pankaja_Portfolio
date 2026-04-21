"""Web scraper modules for different websites"""

from .news_scraper import NewsScraper
from .weather_scraper import WeatherScraper
from .tech_scraper import TechScraper
from .market_scraper import MarketScraper

__all__ = ['NewsScraper', 'WeatherScraper', 'TechScraper', 'MarketScraper']
