"""Scraper for weather information"""

import requests
from typing import List, Dict

class WeatherScraper:
    """Fetches weather data using Open-Meteo API (no API key required)"""
    
    def __init__(self):
        self.api_url = "https://api.open-meteo.com/v1/forecast"
    
    def get_daily_forecast(self, latitude: float = 40.7128, longitude: float = -74.0060) -> Dict:
        """Get daily weather forecast (NYC by default)"""
        try:
            params = {
                'latitude': latitude,
                'longitude': longitude,
                'daily': 'temperature_2m_max,temperature_2m_min,precipitation,weather_code',
                'temperature_unit': 'fahrenheit',
                'timezone': 'auto'
            }
            
            response = requests.get(self.api_url, params=params, timeout=10)
            data = response.json()
            
            forecast = []
            daily = data.get('daily', {})
            
            for i in range(min(1, len(daily.get('time', [])))):
                forecast.append({
                    'date': daily['time'][i],
                    'max_temp': daily['temperature_2m_max'][i],
                    'min_temp': daily['temperature_2m_min'][i],
                    'precipitation': daily['precipitation'][i],
                    'location': f"({latitude}, {longitude})"
                })
            
            return {'daily_forecast': forecast}
        except Exception as e:
            return {'error': f'Failed to fetch weather: {str(e)}'}
    
    def get_weekly_forecast(self, latitude: float = 40.7128, longitude: float = -74.0060) -> Dict:
        """Get 7-day weather forecast"""
        try:
            params = {
                'latitude': latitude,
                'longitude': longitude,
                'daily': 'temperature_2m_max,temperature_2m_min,precipitation,weather_code',
                'temperature_unit': 'fahrenheit',
                'timezone': 'auto'
            }
            
            response = requests.get(self.api_url, params=params, timeout=10)
            data = response.json()
            
            forecast = []
            daily = data.get('daily', {})
            
            for i in range(min(7, len(daily.get('time', [])))):
                forecast.append({
                    'date': daily['time'][i],
                    'max_temp': daily['temperature_2m_max'][i],
                    'min_temp': daily['temperature_2m_min'][i],
                    'precipitation': daily['precipitation'][i]
                })
            
            return {'weekly_forecast': forecast}
        except Exception as e:
            return {'error': f'Failed to fetch weekly forecast: {str(e)}'}
    
    def get_severe_weather(self) -> List[Dict]:
        """Get severe weather alerts (simulated)"""
        return [
            {
                'location': 'NYC',
                'alert': 'No severe weather alerts',
                'severity': 'Low'
            }
        ]
