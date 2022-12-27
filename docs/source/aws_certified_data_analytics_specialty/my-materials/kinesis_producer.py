import requests
import socket
import time
import random
from faker import Faker

fake = Faker('pl-PL')
SLEEP_FACTOR = 1

OWN_IP = requests.get('https://ident.me', verify=False).text
OWN_HOSTNAME = socket.gethostname()

while True:
    time.sleep(random.random()/SLEEP_FACTOR)
    sex = ['M', 'K'][random.randrange(0, 1)]
    birth_date = fake.date_between(start_date='-100y', end_date='-1y')

    item = {
        'producer_ip': OWN_IP,
        'producer_hostname': OWN_HOSTNAME,
        'create_timestamp': int(time.time()),
        'name': fake.name_female() if sex == 'K' else fake.name_male(),
        'email': fake.email(),
        'city': fake.city(),
        'street': fake.street_address(),
        'age': random.randrange(18, 90),
        'iban': fake.iban(),
        'pracodawcy': [fake.company() for _ in range(random.randrange(5))],
        'data_urodzenia': int(birth_date.strftime('%Y%m%d')),
        'pesel': fake.pesel() if random.random() < 0.01 else fake.pesel(birth_date, sex),
        'telefon': fake.phone_number(),
        'method': fake.http_method(),
        'source_ip': fake.ipv4(),
        'result': round(random.random()*1000, 1)}

    print(item)

