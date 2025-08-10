import smtlib, ssl
from .env import my_email, password, target_email
port = 465 # for ssl
smtp_server = "smtp.gmail.com"
def send_alert(message):
  context =ssl.create_default_context()

with   g
