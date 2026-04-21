"""Scraper for market data"""

import requests
from typing import List, Dict
import random

class MarketScraper:
    """Fetches market and stock data"""
    
    def __init__(self):
        # Using free APIs - consider upgrading for production
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_market_summary(self) -> Dict:
        """Get market summary"""
        try:
            # Simulated market data - in production use real APIs like Alpha Vantage, IEX Cloud, etc.
            summary = {
                'indices': [
                    {'name': 'S&P 500', 'value': 4783.45, 'change': 1.23, 'change_pct': 0.026},
                    {'name': 'NASDAQ', 'value': 15234.12, 'change': 2.34, 'change_pct': 0.015},
                    {'name': 'DOW', 'value': 37476.67, 'change': -0.45, 'change_pct': -0.001}
                ],
                'timestamp': 'Market Close'
            }
            return summary
        except Exception as e:
            return {'error': f'Failed to fetch market summary: {str(e)}'}
    
    def get_top_gainers(self) -> List[Dict]:
        """Get top gaining stocks"""
        try:
            # Simulated data - replace with real API
            gainers = [
                {'symbol': 'NVDA', 'name': 'NVIDIA', 'price': 875.43, 'change': 12.56, 'change_pct': 1.45},
                {'symbol': 'TSLA', 'name': 'Tesla', 'price': 242.84, 'change': 8.32, 'change_pct': 3.54},
                {'symbol': 'AMD', 'name': 'AMD', 'price': 198.67, 'change': 6.21, 'change_pct': 3.23},
                {'symbol': 'MSFT', 'name': 'Microsoft', 'price': 378.91, 'change': 5.45, 'change_pct': 1.46},
                {'symbol': 'META', 'name': 'Meta', 'price': 445.32, 'change': 4.23, 'change_pct': 0.96}
            ]
            return gainers
        except Exception as e:
            return [{'error': f'Failed to fetch top gainers: {str(e)}'}]
    
    def get_top_losers(self) -> List[Dict]:
        """Get top losing stocks"""
        try:
            # Simulated data - replace with real API
            losers = [
                {'symbol': 'GE', 'name': 'General Electric', 'price': 87.23, 'change': -3.45, 'change_pct': -3.81},
                {'symbol': 'IBM', 'name': 'IBM', 'price': 178.92, 'change': -2.34, 'change_pct': -1.29},
                {'symbol': 'T', 'name': 'AT&T', 'price': 18.45, 'change': -0.67, 'change_pct': -3.51},
                {'symbol': 'F', 'name': 'Ford', 'price': 8.92, 'change': -0.45, 'change_pct': -4.80},
                {'symbol': 'BAC', 'name': 'Bank of America', 'price': 32.15, 'change': -0.89, 'change_pct': -2.70}
            ]
            return losers
        except Exception as e:
            return [{'error': f'Failed to fetch top losers: {str(e)}'}]
