from bs4 import BeautifulSoup
import requests
import time
import math

symbol = ' '
positions = {}
print('Enter the symbols and number of shares of the stocks in your portfolio')
while symbol != '':
    symbol = input('Enter a position. Enter nothing if you are done entering')
    if symbol != '':
        shares = float(input(f'How many shares of {symbol} do you own?'))
        positions[symbol] = shares

def get_value():
    prices = {}
    total_holdings = 0

    for symbol in positions:
        html_text = requests.get(f'https://www.marketwatch.com/investing/fund/{symbol}/download-data?mod=mw_quote_tab').text
        soup = BeautifulSoup(html_text, 'lxml')
        price_table = soup.find('table', class_="table table--overflow align--center")
        rows = price_table.find_all('tr')
        vals = [rows[1].text.replace('$', '').split(), rows[2].text.replace('$', '').split()]
        prices[symbol] = [float(vals[0][5]), float(vals[1][5])]
    for symbol in positions:
        total_holdings += positions[symbol]*prices[symbol][0]

    message = f'Your portfolio is curently worth ${round(total_holdings, 2)}'

    for symbol in positions:
        word = ''
        difference = prices[symbol][0] - prices[symbol][1]
        if difference>0:
            word = 'up'
        else:
            word = 'down'
        message = message + f'\n{symbol}: ${prices[symbol][0]} : {word} ${round(math.fabs(difference), 2)} from yesterday\'s close'

    return(message)

if __name__ == '__main__':
    print(get_value())
