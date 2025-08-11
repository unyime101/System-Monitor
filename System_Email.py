import smtplib, ssl
import os

# Manually load .env file
def load_env():
  env_vars = {}
  with open('.env', 'r') as f:
    for line in f:
      if '=' in line and not line.startswith('#'):
        key, value = line.strip().split('=', 1)
        env_vars[key] = value
  return env_vars

env = load_env()

def send_email(message):
  port = 465 #ssl
  smtp_server = "smtp.gmail.com"
  context = ssl.create_default_context()
    
  # Get credentials from parsed .env
  my_email = env.get("MY_EMAIL")
  password = env.get("PASSWORD")
  target_email = env.get("TARGET_EMAIL")
  print(message)  #Message formatted how i want
  with smtplib.SMTP_SSL(smtp_server,port,context=context) as server: #sends the passed through message 
    server.login(my_email, password)
    server.sendmail(my_email,target_email,message)




