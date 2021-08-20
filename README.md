# income_of_russian_deputies

Для парсинга нужно последовательно запустить файлы .py с 1 по 5 (6 опционально)

Используемые библиотеки: requests, json, bs4, os, keyboard, tkinter, pandas

Результаты парсинга доходов депутатов Государственной Думы 7 созыва за 2020 находятся в файлах:
https://github.com/pLINaROF/income_of_russian_deputies/blob/main/data_with_income_rub_7_2020.csv
https://github.com/pLINaROF/income_of_russian_deputies/blob/main/data_with_income_rub_7_2020.json


# Описание файлов
* 1_get_deputy_page_urls_list.py - получает список депутатов гос думы указанного созыва.
* 2_get_deputy_info.py - получает информацию по депутатам (id, ФИО, партия, ссылка на сведения о доходах (при наличии)).
* 3_get_income_details.py - добавляет в json из 2 скрипта ссылки на pdf со сведениями о доходах по годам.
* 4_pdf_downloader.py - скачивает в папку pdf pdf-файлы со сведениями о доходах за указанный год.
* 5_pdf_manual_parser.py - по очереди открывает все файлы из папки pdf в браузере и ожидает ручного выделения нужной суммы в pdf, после выделения ожидает нажатия клавиши f (английская раскладка), после чего эмулирует ctrl+c. Скопированные данные запишутся в доход депутата. При подобном подходе не учитывается доход супруг, имущество, ТС.
* 5_pdf_auto_parser.py - попытка прикрутить к предыдущему пункту библиотеку tabula. Результат парсинга 7 созыва после правки 3 записей совпадает с результатом ручного парсинга, но сделано костыльно.
* 6_json_to_csv.py - конвертирует json в csv.


# Donate
Если эта программа вам помогла, не стесняйтесь поддержать автора:
* USDT TRC20: TYvX3gNRghPo6prxVxB9G1pcuEdvCtNUM9 
* BTC: 1A4cCqEBD7U6YLtMFsmqJqZLnKS3g9bZGy
* ETH ERC20: 0xcc559ad9e92621555310d8f5e923ee7a3d914471
* BNB BEP20 (BSC): 0xcc559ad9e92621555310d8f5e923ee7a3d914471
