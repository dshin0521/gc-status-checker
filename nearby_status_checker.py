from bs4 import BeautifulSoup
from collections import defaultdict
import requests

statuses = defaultdict(list)


def get_statuses(application_type, pivot_application_number, count):
    url = "https://egov.uscis.gov/casestatus/mycasestatus.do"
    content = ''

    prefix = pivot_application_number[:3]
    numbers = int(pivot_application_number[3:])
    for n in range(count):
        application_number = prefix + str(numbers)

        print(application_number)

        response = requests.post(url, files=(
            ('appReceiptNum', (None, application_number)),
        ))

        if response.status_code != 200:
            content = content + application_number + ": error in response with status " + \
                      str(response.status_code) + "\n"
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        status = soup.find('div', class_='rows text-center').find("h1").get_text()
        description = soup.find('div', class_='rows text-center').find("p").get_text()

        if application_type.upper() in description.upper():
            statuses[status].append(application_number)
        numbers -= 1

    for key in statuses.keys():
        print(key + " - " + str(len(statuses[key])))
        statuses[key].sort()
        print(statuses[key])

    print(content)


get_statuses('I-485', '...', 10)