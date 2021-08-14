import requests
import json
from bs4 import BeautifulSoup

host = 'http://duma.gov.ru'
print('Этап 2. Получаем информацию по депутатам (id, ФИО, партия, ссылка '
      'на сведения о доходах (при наличии), номер созыва)')
data_dict = []
n = 0
with open('deputy_page_urls_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    print('Кол-во депутатов:', len(lines), 'шт.\n')
    for deputy_url in lines:
        n += 1
        print(f'#{n} {deputy_url}')
        q = requests.get(deputy_url)
        result = q.content
        soup = BeautifulSoup(result, 'lxml')

        person_menu = soup.find(class_='submenu__wrapper submenu__wrapper--border js-nav-mobile')
        if 'Сведения о доходах' not in person_menu.text:
            property_url = ''
        else:
            property_url = f'{deputy_url}property'

        try:
            deputy_name = soup.find(class_='article__title--person').contents
        except:
            deputy_name = soup.find(class_='person__title person__title--l').span.contents

        deputy_name = list(map(str, deputy_name))
        deputy_name.remove('<br/>')
        deputy_name = ' '.join(deputy_name)
        consignment_name = soup.find(class_='person__description__grid').a.text
        deputy_id = int(deputy_url.split('/')[-2])

        data = {
            'id': deputy_id,
            'deputy_name': deputy_name,
            'consignment_name': consignment_name,
            'property_url': property_url
        }
        data_dict.append(data)

print('\nСохраняем полученные данные в deputy_info.json')
with open('deputy_info.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
print('Готово')
