import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())     # template object
email = EmailMessage()      # email object
email["from"] = "German" 
email["to"] = "<email adress>" 
email["subject"] = "You won a 1,000,000 dollars!"

email.set_content(html.substitute(name= "Andrei"), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()     # initial hey this is a server
    smtp.starttls()     # tls is an encription mechanism to connect securily to the server
    smtp.login("<your email address>", "<your app password>")
    smtp.send_message(email)
    print("All good boss!")