from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import requests
import schedule
import smtplib
import time


statuses = {}


def get_response(application_numbers):
    url = "https://egov.uscis.gov/casestatus/mycasestatus.do"
    content = ''
    for application_number in application_numbers:
        response = requests.post(url, files=(
            ('appReceiptNum', (None, application_number)),
        ))

        if response.status_code != 200:
            content = content + application_number + ": error in response with status " + \
                      str(response.status_code) + "\n"
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        status_div = soup.find_all('div', class_='current-status-sec')

        if len(status_div) == 0:
            content = content + application_number + ": no status found\n"
            continue

        status = status_div[0].getText().replace('+', '').strip()
        status = status.split(":")[1].strip()

        if statuses.get(application_number) is None or statuses.get(application_number) != status:
            statuses[application_number] = status
            content = content + application_number + ": " + status + "\n"
            print("status added or changed for " + application_number + " application as '" + status + "'")
        else:
            print("no status change for " + application_number + " application")

    if content != '':
        send_email(content)


def send_email(content):
    username = '...'
    password = '...'
    sender = '...'
    receiver = '...'
    msg = MIMEText(content)
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'GC application statuses'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login(username, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


schedule.every(1).hours.do(get_response, ['...', '...', '...', '...'])

while True:
    schedule.run_pending()
    time.sleep(1)
