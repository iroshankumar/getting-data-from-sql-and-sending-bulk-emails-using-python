import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor
import getpass
from day3_1 import Dbs # Import your existing script or class for SQL operations

def send_email(email_info):
    sender_email, sender_password, to_email, subject, body = email_info

    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    body_text = body.format(recipient=to_email)
    message.attach(MIMEText(body_text, 'plain'))

    # Set up the SMTP server
    smtp_server = smtplib.SMTP('smtp.office365.com', 587) # i am using hotmail servers and port
    smtp_server.starttls()

    # Log in to the email account
    smtp_server.login(sender_email, sender_password)

    # Send the email
    smtp_server.sendmail(sender_email, to_email, message.as_string())

    # Quit the server
    smtp_server.quit()

if __name__ == "__main__":
    db = Dbs()
    db.useDatabase("day2")
    recipient_list1 = db.sendingList("Selection")
    # Your email credentials
    sender_email = 'YourUserName@outlook.com'
    #sender_password = getpass.getpass("Enter password: ")
    sender_password = 'Your password Password'

    # Mail details
    subject = 'Bulk Email Test3'
    body_template = 'Hello {recipient},\n\nThis is a test email sent from Python.'
    recipient_list = recipient_list1

    # Create a ThreadPoolExecutor with 100 threads
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Map the send_email function to the list of email information
        executor.map(send_email, [(sender_email, sender_password, to_email, subject, body_template) for to_email in recipient_list])

    print('Done. Emails sent successfully!')
    print(recipient_list1)