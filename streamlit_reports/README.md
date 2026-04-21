# Daily Reports Agent 📊

A Streamlit-based application that fetches and displays curated daily reports from multiple websites and data sources.

## Features

✨ **Multi-Source Support**
- News (HackerNews, BBC)
- Weather (Open-Meteo API)
- Tech News (TechCrunch, ArsTechnica)
- Market Data (Stocks & Indices)

🎯 **Multiple Report Types**
- Top Stories
- Latest Updates
- Featured Content
- Market Analysis

📧 **Report Distribution**
- Display in web UI
- Download as CSV
- Send via Email (configurable)

📅 **Scheduling** (Coming Soon)
- Daily report generation
- Automated email delivery
- Custom schedules

## Installation

1. **Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.py` to customize:
- Websites and report types
- Email settings (for sending reports)
- Scheduling times

### Email Setup (Gmail)
1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Update `config.py`:
```python
EMAIL_CONFIG = {
    "sender_email": "your_email@gmail.com",
    "sender_password": "your_app_password",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587
}
```

## Running the Application

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`

## Usage

1. **Select a Website** from the sidebar
2. **Choose a Report Type** based on available options
3. **Click "Fetch Report"** to retrieve data
4. **View the formatted report** in the main area
5. **Export or share** using the download/email buttons

## Project Structure

```
streamlit_reports/
├── main.py                    # Main Streamlit app
├── config.py                  # Configuration file
├── requirements.txt           # Dependencies
├── README.md                  # This file
├── scrapers/                  # Web scraping modules
│   ├── __init__.py
│   ├── news_scraper.py       # News scraping
│   ├── weather_scraper.py    # Weather data
│   ├── tech_scraper.py       # Tech news
│   └── market_scraper.py     # Market data
├── reports/                   # Report generation
│   ├── __init__.py
│   ├── report_generator.py   # Report formatting
│   └── email_sender.py       # Email delivery
└── data/                      # Local data storage
```

## Supported Data Sources

### News
- **HackerNews** - Tech news and discussions
- **BBC** - General news (RSS feed)

### Weather
- **Open-Meteo** - Free weather API (no key required)
  - Daily forecast
  - 7-day forecast
  - Weather alerts

### Tech News
- **TechCrunch** - Tech news (RSS feed)
- **ArsTechnica** - Tech articles (RSS feed)

### Market Data
- **Simulated data** (for demo purposes)
  - Replace with Alpha Vantage, IEX Cloud, or Finnhub API for production

## Adding New Sources

1. **Create a new scraper** in `scrapers/`:
```python
class NewSourceScraper:
    def fetch_data(self):
        # Your scraping logic
        pass
```

2. **Add to config.py**:
```python
WEBSITES = {
    "New Source": {
        "url": "https://example.com",
        "reports": {
            "Report Type": "Description"
        }
    }
}
```

3. **Import and use in main.py**

## Advanced Features

### Scheduling Daily Reports
The app is designed to work with APScheduler for automated daily report generation. Uncomment the scheduler section in main.py to enable.

### Custom Report Formats
Modify `report_generator.py` to create custom HTML/CSS for different report types.

### Database Integration
Add SQLite or PostgreSQL to store historical reports and user preferences.

## Troubleshooting

**Issue: "Connection Error" when fetching reports**
- Check internet connection
- Verify website is accessible
- Some websites may block web scrapers

**Issue: Email not sending**
- Verify Gmail app password is set correctly
- Check SMTP settings in config.py
- Enable "Less secure app access" if needed

**Issue: Streamlit not found**
- Ensure virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt`

## Future Enhancements

- 📊 Add more data sources (Crypto, Sports, Social Media)
- 🔐 User authentication and preferences
- 💾 Database for report history
- 🤖 AI summary generation
- 📱 Mobile app version
- 🔔 Push notifications

## License

MIT License - Feel free to use and modify!

## Support

For issues or feature requests, please create an issue in the repository.

---

**Made with ❤️ using Streamlit**
