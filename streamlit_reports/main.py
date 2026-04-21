"""Main Streamlit Application for Daily Reports Agent"""

import streamlit as st
from config import WEBSITES
from scrapers.news_scraper import NewsScraper
from scrapers.weather_scraper import WeatherScraper
from scrapers.tech_scraper import TechScraper
from scrapers.market_scraper import MarketScraper
from reports.report_generator import ReportGenerator
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Daily Reports Agent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
    }
    h1 {
        color: #1f77e5;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_website' not in st.session_state:
    st.session_state.selected_website = None
if 'selected_report' not in st.session_state:
    st.session_state.selected_report = None
if 'report_data' not in st.session_state:
    st.session_state.report_data = None

# Initialize scrapers
news_scraper = NewsScraper()
weather_scraper = WeatherScraper()
tech_scraper = TechScraper()
market_scraper = MarketScraper()
report_generator = ReportGenerator()

def get_report_data(website: str, report_type: str):
    """Fetch data based on selected website and report type"""
    
    if website == "News":
        if report_type == "Top Stories":
            return news_scraper.get_hackernews_top_stories()
        elif report_type == "Latest News":
            return news_scraper.get_latest_news()
        elif report_type == "Most Discussed":
            return news_scraper.get_most_discussed()
    
    elif website == "Weather":
        if report_type == "Daily Forecast":
            return weather_scraper.get_daily_forecast()
        elif report_type == "Weekly Forecast":
            return weather_scraper.get_weekly_forecast()
        elif report_type == "Severe Weather":
            return weather_scraper.get_severe_weather()
    
    elif website == "Tech News":
        if report_type == "Latest Articles":
            return tech_scraper.get_latest_articles()
        elif report_type == "Featured Stories":
            return tech_scraper.get_featured_stories()
        elif report_type == "Startup Updates":
            return tech_scraper.get_startup_updates()
    
    elif website == "Market Data":
        if report_type == "Market Summary":
            return market_scraper.get_market_summary()
        elif report_type == "Top Gainers":
            return market_scraper.get_top_gainers()
        elif report_type == "Top Losers":
            return market_scraper.get_top_losers()
    
    return None

# Sidebar Navigation
with st.sidebar:
    st.title("📋 Report Configuration")
    st.divider()
    
    # Website Selection
    st.subheader("1️⃣ Select Website")
    selected_website = st.selectbox(
        "Choose a website:",
        options=list(WEBSITES.keys()),
        key="website_select"
    )
    
    # Report Type Selection
    st.subheader("2️⃣ Select Report Type")
    if selected_website:
        available_reports = list(WEBSITES[selected_website]['reports'].keys())
        selected_report = st.selectbox(
            "Choose a report:",
            options=available_reports,
            key="report_select"
        )
        
        report_description = WEBSITES[selected_website]['reports'][selected_report]
        st.caption(f"📌 {report_description}")
    else:
        selected_report = None
    
    st.divider()
    
    # Fetch Report Button
    if st.button("🔄 Fetch Report", use_container_width=True):
        if selected_website and selected_report:
            with st.spinner(f"Fetching {selected_report} from {selected_website}..."):
                data = get_report_data(selected_website, selected_report)
                st.session_state.report_data = data
                st.session_state.selected_website = selected_website
                st.session_state.selected_report = selected_report
                st.success(f"✅ Report fetched successfully!")
        else:
            st.warning("Please select both website and report type")

# Main Content Area
st.title("📊 Daily Reports Agent")
st.markdown("*Get curated daily reports from multiple sources*")

# Display fetched report
if st.session_state.report_data:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"### {st.session_state.selected_report}")
        st.markdown(f"**Source:** {st.session_state.selected_website}")
    
    with col2:
        st.caption(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    st.divider()
    
    # Generate and display formatted report
    html_report = report_generator.create_full_report(
        st.session_state.selected_website,
        st.session_state.selected_report,
        st.session_state.report_data
    )
    
    st.markdown(html_report, unsafe_allow_html=True)
    
    # Export options
    st.divider()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📧 Send via Email"):
            st.info("Email feature requires SMTP configuration. Update EMAIL_CONFIG in config.py")
    
    with col2:
        # Export as text
        if isinstance(st.session_state.report_data, list):
            df = pd.DataFrame(st.session_state.report_data)
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name=f"{st.session_state.selected_website}_{st.session_state.selected_report}.csv",
                mime="text/csv"
            )
    
    with col3:
        if st.button("🔄 Clear"):
            st.session_state.report_data = None
            st.rerun()

else:
    st.info("👈 Select a website and report type from the sidebar to get started!")
    
    # Show available options
    st.subheader("📚 Available Reports:")
    cols = st.columns(2)
    
    for idx, (website, config) in enumerate(WEBSITES.items()):
        with cols[idx % 2]:
            st.markdown(f"**{website}**")
            for report in config['reports'].keys():
                st.markdown(f"- {report}")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; margin-top: 3rem; color: #666;'>
    <p><small>Daily Reports Agent v1.0 | Built with Streamlit</small></p>
</div>
""", unsafe_allow_html=True)
