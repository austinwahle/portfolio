from bs4 import BeautifulSoup
import requests
import time

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
        html_text = requests.get(f'https://www.marketwatch.com/investing/fund/{symbol}').text
        soup = BeautifulSoup(html_text, 'lxml')
        price = soup.find('h3', class_="intraday__price").text.replace('$', '').strip()
        prices[symbol] = float(price)
    for symbol in positions:
        total_holdings += positions[symbol]*prices[symbol]

    return(f'Your portfolio is curently worth ${total_holdings}')

if __name__ == '__main__':
    while True:
        time_wait = .1
        print(get_value())
        time.sleep(time_wait*60)
