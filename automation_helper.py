
import smtplib

# Function to send an email notification
def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, recipient_email, email_message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    send_email("your_email@gmail.com", "your_password", "recipient_email@gmail.com",
               "Weekly Update", "Here is your weekly performance update!")
