import time
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pyautogui  # Импортируем библиотеку для автоматизации мыши

# Настройка Firefox
options = Options()
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Инициализация драйвера
driver = webdriver.Firefox(options=options)

# Открытие страницы
driver.get("https://csstats.gg/player/76561199097155123 ")
time.sleep(5)  # Ждём загрузки страницы

try:
    print("Клик по координатам (783, 787)")
    pyautogui.click(783, 787)  # Выполняем клик по указанным координатам
    print("Клик выполнен.")
except Exception as e:
    print(f"Ошибка при клике по координатам: {e}")
finally:
    # Закрытие браузера
    time.sleep(5)  # Задержка для просмотра результата
    driver.quit()