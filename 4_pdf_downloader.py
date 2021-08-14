import json
import requests
import os

income_year = 2020
pdf_dir = 'pdf'
project_dir = os.getcwd()

try:
    os.makedirs(project_dir + '\\' + pdf_dir, mode=0o777, exist_ok=False)
    print(f'Папки {pdf_dir} не существует, создал')
except FileExistsError:
    pass

print(f'Этап 4. Скачиваем pdf файлы со сведениями о доходах за {income_year}')
print('Открываем deputy_info_with_income_urls.json')
with open('deputy_info_with_income_urls.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

print('\nКол-во депутатов:', len(data), 'шт.')
n = 0
for d in data:
    n += 1
    deputy_id = d['id']
    deputy_name = d['deputy_name']
    consignment_name = d['consignment_name']
    try:
        income_url = d['income_urls'][f'{income_year}']
        print(f"#{n} {deputy_id} {income_url}")
        pdf = requests.get(income_url, allow_redirects=True)
        open(f'{pdf_dir}/{deputy_id}; {deputy_name}; {consignment_name}; '
             f'{income_year}.pdf', 'wb').write(pdf.content)
    except:
        print(f"#{n} {deputy_id} {deputy_name} Ссылка на сведения о доходах отсутствует, "
              f"в итоговой таблице этого депутата не будет")

print(f'\nСкачивание сведений о доходах депутатов за {income_year} год завершено')
