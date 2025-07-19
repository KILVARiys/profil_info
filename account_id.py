import requests
import re
from bs4 import BeautifulSoup

full_url_steam = input("Введите url steam: ")
# Извлечение ID профиля из ссылки
result = ''.join(c if c.isdigit() else ' ' for c in full_url_steam).split()
short_url_steam = [int(item) for item in result]
id_steam = short_url_steam[0]
print(id_steam)

url_steam = f'https://steamid.pro/lookup/{id_steam}'
response = requests.get(url_steam)
    
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    account_id_finder = soup.findAll('td')[3].text  # Преобразуем Tag в строку
    numbers = re.findall(r'\d+', account_id_finder)
    print(numbers[0])
else:
    print(f"Ошибка: {response.status_code}")