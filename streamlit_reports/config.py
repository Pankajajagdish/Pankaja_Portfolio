"""Configuration for websites and report types"""

WEBSITES = {
    "News": {
        "url": "https://news.ycombinator.com",
        "reports": {
            "Top Stories": "Fetch top 10 trending stories",
            "Latest News": "Get most recent news updates",
            "Most Discussed": "Show most discussed articles"
        }
    },
    "Weather": {
        "url": "https://weather.com",
        "reports": {
            "Daily Forecast": "Get today's weather forecast",
            "Weekly Forecast": "7-day weather forecast",
            "Severe Weather": "Alerts for severe weather"
        }
    },
    "Tech News": {
        "url": "https://techcrunch.com",
        "reports": {
            "Latest Articles": "Most recent tech articles",
            "Featured Stories": "Editor's featured stories",
            "Startup Updates": "Latest startup news"
        }
    },
    "Market Data": {
        "url": "https://finance.yahoo.com",
        "reports": {
            "Market Summary": "Daily market overview",
            "Top Gainers": "Best performing stocks",
            "Top Losers": "Worst performing stocks"
        }
    }
}

# Email configuration for sending reports
EMAIL_CONFIG = {
    "sender_email": "your_email@gmail.com",
    "sender_password": "your_app_password",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587
}

# Schedule configuration
SCHEDULE_TIMES = {
    "Morning": "08:00",
    "Afternoon": "12:00",
    "Evening": "18:00",
    "Night": "21:00"
}
