import requests
from bs4 import BeautifulSoup

full_url_steam = 'https://steamcommunity.com/profiles/76561199097155123'
# Извлечение ID профиля из ссылки
result = ''.join(c if c.isdigit() else ' ' for c in full_url_steam).split()
short_url_steam = [int(item) for item in result]
id_steam = short_url_steam[0]
print(id_steam)

url_steam = f'https://steamid.pro/lookup/{id_steam}'
response = requests.get(url_steam)
    
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    account_id_finder = soup.find('td', class_='span2').find_next('td').get_text(strip=True)
    print('Найдено')
    print(account_id_finder)
else:
    print(f"Ошибка: {response.status_code}")
    
from bs4 import BeautifulSoup

def parse_account_id(html):
    soup = BeautifulSoup(html, 'html.parser')
    for row in soup.find_all('tr'):
        tds = row.find_all('td')
        if len(tds) >= 2 and tds[0].get_text(strip=True) == 'AccountID':
            return tds[1].get_text(strip=True).split()[0]
    return None