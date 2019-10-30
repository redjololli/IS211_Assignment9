import urllib.request as request
from bs4 import BeautifulSoup
import json

url = 'https://finance.yahoo.com/quote/AAPL/history?ltr=1'
webPage = request.urlopen(url)
soup = BeautifulSoup(webPage.read(), "html.parser")
table = soup.find_all('table', attrs={"cols":"4"})


def yahoo_apple_stock():
    data = []
    fhandler = soup.find_all('tr')

    for rows in fhandler:
        try:
            if len(rows.find_all(('td', {'class': 'span data-reactid'}))) == 7:
                date = rows.contents[0].get_text()
                close = rows.contents[5].get_text()
                data.append((date, close))
                json_string = {
                    "Date": date,
                    "Closed Stock Price": close,
                }
                print(json.dumps(json_string))
        except:
            print('bad url')
            continue
    return yahoo_apple_stock


if __name__ == "__main__":
    yahoo_apple_stock()
