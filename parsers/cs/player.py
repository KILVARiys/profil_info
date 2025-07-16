import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Настройка Firefox
options = Options()
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Инициализация драйвера
driver = webdriver.Firefox(options=options)

full_steam_id = 76561199097155123

# Открытие страницы
driver.get(f"https://csstats.gg/player/{full_steam_id}")
time.sleep(5)  # Ждём загрузки страницы

try:
    # Извлечение данных: поиск элемента по классу
    print("Извлечение данных со страницы...")
    kd_element = driver.find_element(By.CLASS_NAME, "stat-large")
    winrate_elements = driver.find_elements(By.CLASS_NAME, "stat-panel")  # Получаем все элементы с этим классом
    winrate_element = winrate_elements[2]  # Берём третий элемент (индекс 2)
    #Полученные даные
    winrate = winrate_element.text
    kd = kd_element.text

    # Вывод данных
    print(f"Статистика игрока (KD): {kd}")
    print(f"Статистика игрока (Winrate): {winrate}")

except Exception as e:
    print(f"Ошибка при извлечении данных: {e}")
finally:
    # Закрытие браузера
    time.sleep(5)  # Задержка для просмотра результата
    driver.quit()