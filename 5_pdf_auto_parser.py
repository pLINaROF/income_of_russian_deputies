import re
import json
import tabula
import pandas
import glob


pdf_files = glob.glob(r'pdf/*.pdf')
n = 1
data_dict = []
problem_dict = []

for pdf_file in pdf_files:
    pdf_df = tabula.read_pdf(pdf_file, pages='all', lattice=False)
    deputy_id, deputy_name, consignment_name, income_year = pdf_file.split('; ')
    deputy_id = int(str(deputy_id).split('\\')[1])
    try:
        income_sum = pdf_df[0].iloc[0].values[1]
        income_sum = int(re.sub(r'(\..+|,.+)', '', income_sum))
        # print(f'#{n}', pdf_file, income_sum, 'руб')
    except TypeError:
        income_sum = 'требуется проверить вручную'
        print(f'#{n}, {pdf_file} \tНе получилось достать доход из файла. '
              f'Требуется проверить вручную и добавить в json')
        problem_dict.append([deputy_id, deputy_name, f'http://duma.gov.ru/duma/persons/{deputy_id}/property/'])
    finally:
        print(f'#{n}', pdf_file, income_sum)
    data = {
        'id': deputy_id,
        'deputy_name': deputy_name,
        'consignment_name': consignment_name,
        'url': f'http://duma.gov.ru/duma/persons/{deputy_id}/',
        'income_sum': income_sum
    }
    data_dict.append(data)
    with open('data_with_income_rub.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
    n += 1

print('\n', '=' * 100)
print('Не удалось получить доход по депутатам, нужно проверить руками и добавить в json\n'
      'в json проблемные записи искать по "требуется проверить вручную"')
for p in problem_dict:
    print(p)
