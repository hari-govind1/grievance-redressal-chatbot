import smtplib 
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(recipient_email, tracking_number, summary):
    try:
        subject = "Grievance Submission Confirmation"
        
        # Email body with tracking number and grievance summary
        body = f"""
        Dear User,

        Your grievance has been successfully submitted.

        Your unique Tracking Number is : {tracking_number}
        Your Grievance Summary is : {summary}

        Please keep this tracking number for future reference.

        Regards,  
        Grievance Redressal System
        """

        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS 
        msg['To'] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
            print("Email sent successfully!")
    
    except Exception as e:
        print(f"Error sending mail: {e}")

# Example Usage
if __name__ == "__main__":
    recipient = "21csa19@karpagamtech.ac.in"
    tracking_number = 123456  # Example tracking number
    summary = "The internet in the library is not working properly."
    
    send_email(recipient, tracking_number, summary)
