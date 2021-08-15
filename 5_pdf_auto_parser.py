import re
import json
import tabula
import pandas
import glob


pdf_files = glob.glob(r'pdf/*.pdf')
n = 1
for pdf_file in pdf_files:
    csv_file = str(pdf_file).replace('.pdf', '.csv')
    print(f'#{n}', f'"{pdf_file}"', '\tto\t', f'"{csv_file}"', 'done')
    tabula.convert_into(pdf_file, csv_file, output_format="csv", pages='all')
    n += 1
print('Смена формата завершена')


print('Получаем доход из csv')
data_dict = []
problem_dict = []
csv_files = glob.glob(r'pdf/*.csv')
for csv_file in csv_files:
    deputy_id, deputy_name, consignment_name, income_year = csv_file.split('; ')
    deputy_id = int(str(deputy_id).split('\\')[1])
    df = pandas.read_csv(csv_file, encoding='windows-1251', index_col=False)

    try:
        income_sum = df.iloc[0].values[1]
        income_sum = int(re.sub(r'(\..+|,.+)', '', income_sum))
        # print(csv_file, income_sum, 'руб')
    except TypeError:
        income_sum = 'требуется проверить вручную'
        print('Не получилось достать доход из файла')
        print(csv_file)
        problem_dict.append([deputy_id, deputy_name, f'http://duma.gov.ru/duma/persons/{deputy_id}/property/'])

    data = {
        'id': deputy_id,
        'deputy_name': deputy_name,
        'consignment_name': consignment_name,
        'url': f'http://duma.gov.ru/duma/persons/{deputy_id}/',
        'income_sum': income_sum
    }
    data_dict.append(data)

    with open('data_with_income_rub_from_csv.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_dict, json_file, indent=4, ensure_ascii=False)

print('\n', '=' * 100)
print('Не удалось получить доход по депутатам, нужно проверить руками и добавить в json\n'
      'в json проблемные записи искать по "требуется проверить вручную"')
for p in problem_dict:
    print(p)

