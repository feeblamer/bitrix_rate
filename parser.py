import requests
import lxml.html
from datetime import  date 
import json
import os.path 

DATA_FILE = 'currency.json'

def get_url():
    base_url = "http://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={}"
    return base_url.format(current_date())

def get_html(url):    
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        return None

def parse(html):
    tree = lxml.html.fromstring(html)
    rows = tree.xpath(".//table//tr//td[contains(text(), 'USD')" 
        "or contains(text(), 'EUR')" 
        "or contains(text(), 'KZT')"
        "or contains(text(), 'PLN') ]/..")
    
    list_currencies = []
    for row in rows:
        numeric_code = row.getchildren()[0].text
        alphabetical_code = row.getchildren()[1].text
        currency = row.getchildren()[3].text
        units = row.getchildren()[2].text
        rate = row.getchildren()[-1].text

        list_currencies.append(
                {
                 'numeric_code':numeric_code,
                 'alphabetical_code': alphabetical_code,
                 'rate':  rate,
                 'units': units,
                 'currency':currency,
                  },
            )
    return list_currencies

def current_date():
    return date.today().strftime('%d.%m.%Y')

def update_currencies(url):
    html = get_html(url)
    list_currencies = parse(html)
    data = {
        'date':current_date(),
        'currencies': list_currencies,
        }
    with open(DATA_FILE, 'w') as fp:
        json.dump(data, fp)
    
    return data

def is_update(from_json_date:date):
    return date.today() > from_json_date

def get_date_from_string(date_as_string):
    date_as_int = list(map(int, date_as_string.split('.')))
    return date(*date_as_int[::-1])

def read_json():
    with open(DATA_FILE, 'r') as fp:
        data = json.load(fp)     
        return data 


def get_currencies():
    if not os.path.exists(DATA_FILE):
        return update_currencies(get_url())
    else:
        data = read_json()
        from_json_date = get_date_from_string(data['date'])
        if is_update(from_json_date):
            data = update_currencies(get_url())
        return data

if __name__ == "__main__":
    data = get_currencies()
    print(data)