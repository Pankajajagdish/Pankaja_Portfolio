"""Send reports via email"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from config import EMAIL_CONFIG
except ImportError:
    EMAIL_CONFIG = {
        'sender_email': 'your_email@gmail.com',
        'sender_password': 'your_app_password',
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587
    }

class EmailSender:
    """Sends reports via email"""
    
    def __init__(self, sender_email=None, sender_password=None):
        self.sender_email = sender_email or EMAIL_CONFIG['sender_email']
        self.sender_password = sender_password or EMAIL_CONFIG['sender_password']
        self.smtp_server = EMAIL_CONFIG['smtp_server']
        self.smtp_port = EMAIL_CONFIG['smtp_port']
    
    def send_report(self, recipient_email: str, subject: str, html_content: str) -> bool:
        """Send a report via email"""
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            
            # Attach HTML content
            msg.attach(MIMEText(html_content, 'html'))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False
    
    def send_batch_reports(self, recipient_emails: List[str], subject: str, html_content: str) -> Dict:
        """Send reports to multiple recipients"""
        results = {}
        for email in recipient_emails:
            results[email] = self.send_report(email, subject, html_content)
        return results
