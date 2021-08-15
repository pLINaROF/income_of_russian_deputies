import pandas

df = pandas.read_json('data_with_income_rub.json')
df.to_csv('data_with_income_rub.csv', index=False)

df = pandas.read_json('data_with_income_rub_from_csv.json')
df.to_csv('data_with_income_rub_from_csv.csv', index=False)
