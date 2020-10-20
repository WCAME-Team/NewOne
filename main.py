import requests
import bs4

link = "http://icanhazip.com/"
responce = requests.get('https://browser-info.ru/').text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id = '')

with open('1.html', 'w', encoding='utf-8') as file:
    file.write(responce)