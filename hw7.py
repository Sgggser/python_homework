s = '05.17.2016'

american_date_splitted = s.split('.')

month = american_date_splitted[0]
day = american_date_splitted[1]
year = american_date_splitted[2]

euro_date = day + '.' + month + '.' + year
print(euro_date)