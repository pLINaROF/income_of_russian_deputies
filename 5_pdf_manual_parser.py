import os
from selenium import webdriver
from tkinter import Tk
import json
import keyboard

DRIVER = 'chromedriver.exe'
pdf_dir = 'pdf'
pdfs_list = os.listdir(path=f"./{pdf_dir}")
project_dir = os.getcwd()
data_dict = []

n = 0
print('Этап 5. Ручной парсинг pdf файлов с элементами автоматизации')
print('Всего файлов:', len(pdfs_list))
print('\nРешение сомнительное, но работает'
      '\nВам предстоит дважды кликать на сумму в столбце "Общая сумма декларированного годового дохода" '
      'в открывшемся документе и после выделения суммы нажимать клавишу f (английская раскладка)'
      '\nСкопированная сумма запишется в доход депутата и добавится в json'
      '\nНужно выполнить несколько прогонов для исключения ошибок '
      'предварительно переименовав файл data_with_income_rub.json чтобы потом сравнить '
      '(хватило одного; один ручной прогон занимает примерно 40 минут)'
      '\nПри подобном подходе не учитывается доход супруг, имущество, ТС (попадаются интересные примеры)\n')

for p in pdfs_list:
    deputy_id, deputy_name, consignment_name, income_year = p.split('; ')
    deputy_id = int(deputy_id.split('.')[0])
    driver = webdriver.Chrome(DRIVER)
    driver.get(rf'{project_dir}\{pdf_dir}\{p}')
    n += 1
    keyboard.wait('f')
    keyboard.send("ctrl+c")
    income_sum = int(Tk().clipboard_get())
    print(f'#{n}', deputy_id, deputy_name, income_year, "\t{:,}".format(income_sum).replace(",", " "), 'руб')
    driver.close()

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
print('\nГотово')
print('Сохраняем полученные данные в data_with_income_urls.json')
