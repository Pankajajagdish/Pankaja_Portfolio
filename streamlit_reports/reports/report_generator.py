"""Generate and format reports"""

import pandas as pd
from typing import Dict, List, Any
from datetime import datetime

class ReportGenerator:
    """Generates formatted reports from scraped data"""
    
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def format_news_report(self, stories: List[Dict], report_type: str) -> str:
        """Format news report as HTML/Text"""
        html = f"""
        <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
            <h2>📰 {report_type} Report</h2>
            <p><small>Generated: {self.timestamp}</small></p>
            <hr>
        """
        
        if stories and 'error' not in stories[0]:
            for story in stories:
                html += f"""
                <div style='margin: 15px 0; padding: 10px; background-color: white; border-left: 4px solid #1f77e5;'>
                    <h4>{story.get('rank', '•')}. {story.get('title', 'N/A')}</h4>
                    <p><a href="{story.get('url', '#')}" target="_blank">Read more</a></p>
                    <small>Source: {story.get('source', 'Unknown')}</small>
                </div>
                """
        else:
            html += "<p>Unable to fetch news data.</p>"
        
        html += "</div>"
        return html
    
    def format_weather_report(self, data: Dict, report_type: str) -> str:
        """Format weather report"""
        html = f"""
        <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
            <h2>🌤️ {report_type} Report</h2>
            <p><small>Generated: {self.timestamp}</small></p>
            <hr>
        """
        
        if 'error' not in data:
            if 'daily_forecast' in data:
                for forecast in data['daily_forecast']:
                    html += f"""
                    <div style='margin: 15px 0; padding: 10px; background-color: white; border-radius: 5px;'>
                        <h4>📅 {forecast.get('date', 'N/A')}</h4>
                        <p>
                            High: {forecast.get('max_temp', 'N/A')}°F | 
                            Low: {forecast.get('min_temp', 'N/A')}°F<br>
                            Precipitation: {forecast.get('precipitation', 0)}%
                        </p>
                    </div>
                    """
            elif 'weekly_forecast' in data:
                html += "<table style='width: 100%; border-collapse: collapse;'>"
                html += "<tr><th>Date</th><th>High</th><th>Low</th><th>Precip</th></tr>"
                for forecast in data['weekly_forecast']:
                    html += f"""
                    <tr style='border: 1px solid #ddd;'>
                        <td>{forecast.get('date', 'N/A')}</td>
                        <td>{forecast.get('max_temp', 'N/A')}°F</td>
                        <td>{forecast.get('min_temp', 'N/A')}°F</td>
                        <td>{forecast.get('precipitation', 0)}%</td>
                    </tr>
                    """
                html += "</table>"
        else:
            html += f"<p>{data.get('error', 'Unable to fetch weather data')}</p>"
        
        html += "</div>"
        return html
    
    def format_market_report(self, data: Dict, report_type: str) -> str:
        """Format market report"""
        html = f"""
        <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
            <h2>📈 {report_type} Report</h2>
            <p><small>Generated: {self.timestamp}</small></p>
            <hr>
        """
        
        if isinstance(data, list):
            html += "<table style='width: 100%; border-collapse: collapse;'>"
            if data and 'symbol' in data[0]:
                html += "<tr><th>Symbol</th><th>Name</th><th>Price</th><th>Change</th><th>%Change</th></tr>"
                for stock in data:
                    change_color = 'green' if stock.get('change', 0) >= 0 else 'red'
                    html += f"""
                    <tr style='border: 1px solid #ddd;'>
                        <td><strong>{stock.get('symbol', 'N/A')}</strong></td>
                        <td>{stock.get('name', 'N/A')}</td>
                        <td>${stock.get('price', 0):.2f}</td>
                        <td style='color: {change_color};'>${stock.get('change', 0):.2f}</td>
                        <td style='color: {change_color};'>{stock.get('change_pct', 0):.2f}%</td>
                    </tr>
                    """
            html += "</table>"
        elif isinstance(data, dict) and 'indices' in data:
            html += "<h3>Market Indices</h3>"
            for idx in data['indices']:
                color = 'green' if idx['change'] >= 0 else 'red'
                html += f"""
                <div style='margin: 10px 0; padding: 10px; background-color: white; border-radius: 5px;'>
                    <h4>{idx['name']}</h4>
                    <p>
                        <strong>{idx['value']:.2f}</strong>
                        <span style='color: {color};'>
                            {'+' if idx['change'] >= 0 else ''}{idx['change']:.2f} ({idx['change_pct']:.2f}%)
                        </span>
                    </p>
                </div>
                """
        
        html += "</div>"
        return html
    
    def create_full_report(self, website: str, report_type: str, data: Any) -> str:
        """Create a complete formatted report"""
        if website == "News":
            return self.format_news_report(data, report_type)
        elif website == "Weather":
            return self.format_weather_report(data, report_type)
        elif website == "Tech News":
            return self.format_news_report(data, report_type)
        elif website == "Market Data":
            return self.format_market_report(data, report_type)
        else:
            return "<p>Unknown report type</p>"
