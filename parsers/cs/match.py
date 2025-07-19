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
driver.get(f"https://csstats.gg/player/{full_steam_id}#/matches")
time.sleep(10)  # Ждём загрузки страницы

try:
    # Извлечение данных: поиск элемента по CSS-селектору
    print("Извлечение данных со страницы...")
    matchs_element = driver.find_elements(By.CSS_SELECTOR, ".p-row.js-link")
    
    limited_matches = matchs_element[:8]
        
    # Вывод количества найденных элементов
    print(f"Найдено элементов: {len(matchs_element)}")

    # Вывод текста каждого элемента
    for i, element in enumerate(limited_matches, start=1):
        print(f"Матч {i}: {element.text}")

except Exception as e:
    print(f"Ошибка при извлечении данных: {e}")
finally:
    # Закрытие браузера
    driver.quit()