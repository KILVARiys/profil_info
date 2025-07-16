import asyncio
from playwright.async_api import async_playwright

async def get_csstats_profile(steam_id):
    url = f'https://csstats.gg/player/{steam_id}'

    async with async_playwright() as p:
        # Запускаем браузер (можно использовать chromium, firefox или webkit)
        browser = await p.chromium.launch(headless=True)  # headless=False для визуального режима
        page = await browser.new_page()

        try:
            # Переходим на страницу
            await page.goto(url)

            # Ждём загрузки элементов профиля
            await page.wait_for_selector("h1.player-name", timeout=10000)

            # Парсим нужные данные
            player_name = await page.text_content("h1.player-name")
            total_wins = await page.text_content(".wins")

            print(f"Имя игрока: {player_name.strip()}")
            print(f"Общее количество побед: {total_wins.strip()}")

        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

        finally:
            await browser.close()

if __name__ == "__main__":
    steam_id = 76561199097155123
    asyncio.run(get_csstats_profile(steam_id))