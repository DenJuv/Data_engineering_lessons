import requests
from datetime import datetime

api_key = '5f8926889b22493da19dd7fef13fed60'
curr = 'RUB,EUR'
sd = '2025-03-03'
ed = '2025-03-05'
URL = f'http://currencylayer.com/change?access_key={api_key}&currencies={curr}&start_date={sd}&end_date={ed}'
r=requests.get(url=URL)
result = r.json()
print(result)
#dt = datetime.fromtimestamp(result.get('timestamp'))
#dt = dt.strftime('%Y-%m-%d')
#print(dt)
print(result.get('quotes').get('USDRUB'))
print(result.get('quotes').get('USDEUR'))
