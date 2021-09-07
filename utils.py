import requests


def currency_rates(val):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.content.decode(encoding=response.encoding)
    result = None
    if val not in content:
        return result
    else:
        for el in content.split(f'{val}')[1:]:
            for elem in el.split(f'</Value>')[:1]:
                result = round(float(elem.split('<Value>')[1].replace(',', '.')), 2)
        return f'Курс {val}: {result} RUR.'


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))
