import pandas

df = pandas.read_json('data_with_income_rub.json')
df.to_csv('data_with_income_rub.csv')
