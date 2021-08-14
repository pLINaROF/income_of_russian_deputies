import requests, json
from bs4 import BeautifulSoup

host = 'http://duma.gov.ru'

print('Этап 3. Добавляем в json ссылки на pdf со сведениями о доходах по годам')
print('Открываем deputy_info.json')
with open('deputy_info.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

data_dict = []
print('Получаем ссылки на pdf из раздела "Сведения о доходах"')
print('\nКол-во депутатов:', len(data), 'шт.')
n = 0
for d in data:
    n += 1
    if d['property_url'] == '':
        income_pdf_dict = {}
        print(f'#{n} Ссылка на сведения о доходах отсутствует')
    else:
        print(f"#{n} {d['property_url']}")
        q = requests.get(d['property_url'])
        result = q.content
        soup = BeautifulSoup(result, 'lxml')
        income_details = soup.find_all(class_='download__item')
        income_pdf_dict = {}
        for detail in income_details:
            income_pdf_link = f"{host}{detail.a.get('href')}"
            income_pdf_year = detail.span.text
            income_urls_dict = {
                'income_pdf_link': income_pdf_link,
                'income_pdf_year': income_pdf_year
            }
            income_pdf_dict[income_pdf_year] = income_pdf_link

    data = {
        'id': d['id'],
        'deputy_name': d['deputy_name'],
        'consignment_name': d['consignment_name'],
        'property_url': d['property_url'],
        'income_urls': income_pdf_dict
    }
    data_dict.append(data)

print('\nСохраняем полученные данные в deputy_info_with_income_urls.json')
with open('deputy_info_with_income_urls.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
print('Готово')
