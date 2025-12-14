import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail(mail):
  try:
    # Email configuration
    sender_email = "studentsgrienvancesystem@gmail.com"
    receiver_email = mail + ", gayatriburande5503@gmail.com"
    password = "hrvq mwei appk yfsi"
    subject = "Complain Raised"
    body = "Hi, \n\nThank you for using students grienvance system, your complain is registered and send for further action. please do not reply on this mail. \n\n\n\n\n Thank & Regards."

    # Create a MIMEText object to represent the email body
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
    
  except Exception as error:
     print(error)

def sendMailAdmin(studentName):
  try:
    # Email configuration
    sender_email = "studentsgrienvancesystem@gmail.com"
    receiver_email = "gayatriburande5503@gmail.com"
    password = "hrvq mwei appk yfsi"
    subject = "Complain Raised by "+studentName
    body = "Hi, \n\n Complain is raised by "+studentName+" . please take appropriate action on complain. \n\n\n\n\n Thank & Regards."

    # Create a MIMEText object to represent the email body
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
  except Exception as error:
     print(error)