import requests

# Конфигурация
steam_id = "76561199016042530"
api_key = "fca0aeb0-56d5-433a-b6f1-a79d67fb9e26"
URL = "https://ruststats.io/public-api/user/statistics?steam_id=steam_id&api_key=api_key"

def get_user_statistics(steam_id, api_key):
    # Формирование запроса
    params = {
        "steam_id": steam_id,
        "api_key": api_key
    }

    # Отправка GET-запроса
    response = requests.get(URL, params=params)

    # Проверка статуса ответа
    if response.status_code == 200:
        try:
            # Получение JSON-данных
            data = response.json()
            return data
        except requests.exceptions.JSONDecodeError:
            print("Ошибка: Некорректный формат JSON в ответе.")
            return None
    else:
        print(f"Ошибка запроса: Статус {response.status_code}")
        print("Ответ сервера:", response.text)
        return None

def main():
    # Получение статистики пользователя
    statistics = get_user_statistics(steam_id, api_key)

    if statistics:
        # Вывод данных
        print("Полученные данные:")
        print(statistics)
    else:
        print("Не удалось получить данные.")

if __name__ == "__main__":
    main()