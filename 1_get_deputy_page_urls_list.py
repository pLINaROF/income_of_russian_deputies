import requests, json
from bs4 import BeautifulSoup

convocation_number = 7
host = 'http://duma.gov.ru'
deputies_convocation_url = f'{host}/duma/deputies/{convocation_number}/'

print(f'Этап 1. Получаем список всех депутатов {convocation_number} созыва')
q = requests.get(deputies_convocation_url)
result = q.content
soup = BeautifulSoup(result, 'lxml')
deputies = soup.find_all(class_='person__image-wrapper--s')

deputy_page_url_list = []

for deputy in deputies:
    deputy_page_url = host + deputy.get('href')
    deputy_page_url_list.append(deputy_page_url)

print('Сохраняем список депутатов в deputy_page_url_list.txt')
with open(f'deputy_page_urls_list.txt', 'a', encoding='utf-8') as file:
    for line in deputy_page_url_list:
        file.write(f'{line}\n')
