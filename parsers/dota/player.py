import requests

url = "https://api.stratz.com/graphql"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0IjoiNDM1MTcxMTEtOTI0NC00Y2EwLTkwNTAtZmMwZjJiYTBkN2JlIiwiU3RlYW1JZCI6IjExMzY4ODkzOTUiLCJuYmYiOjE3NTE1NjQwODgsImV4cCI6MTc4MzEwMDA4OCwiaWF0IjoxNzUxNTY0MDg4LCJpc3MiOiJodHRwczovL2FwaS5zdHJhdHouY29tIn0.xuTitlm6DC-hytX9m2npjNQLUEWM-qcokMMhNDcDLZw"
headers = {
    "User-Agent": "STRATZ_API",
    "Authorization": f"Bearer {token}",
}

full_url_steam = 'https://steamcommunity.com/profiles/76561199097155123'
# Извлечение ID профиля из ссылки
result = ''.join(c if c.isdigit() else ' ' for c in full_url_steam).split()
short_url_steam = [int(item) for item in result]
id_steam = short_url_steam[0]
print(id_steam)
def lookup_steam_id(id_steam):
    url_steam = f'https://steamid.pro/lookup/{id_steam}'
    response = requests.get(url_steam)
    
    if response.status_code == 200:
        return response.json()  # Предполагается, что ответ в формате JSON
    else:
        return f"Ошибка: {response.status_code}"

steam_id = 1136889395  # Ваш Steam ID

query = """
query ($steamAccountId: Long!) {
  player(steamAccountId: $steamAccountId) {
    matches(request: {take: 10}) {
      id
      gameMode
      players(steamAccountId: $steamAccountId) {
        hero {
          id
          displayName
        }
        kills
        deaths
        assists
        goldPerMinute
        experiencePerMinute
      }
    }
    firstMatchDate
    lastMatchDate
  }
}
"""

variables = {"steamAccountId": steam_id}

prepared = requests.Request('POST', url, json={"query": query, "variables": variables}, headers=headers).prepare()
for k, v in prepared.headers.items():
    print('{0}: {1}'.format(k, v))

response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)

if response.status_code == 200:
    data = response.json()
    player_data = data["data"]["player"]

    print(f"Player ID: {player_data.get('id', 'N/A')}")
    print(f"Steam ID: {player_data.get('steamAccountId', 'N/A')}")

    matches = player_data.get("matches", [])
    for match in matches:
        print("\nMatch:")
        print(f"  Match ID: {match.get('id', 'N/A')}")
        print(f"  Game Mode: {match.get('gameMode', 'N/A')}")


        player_stats = match.get("players", [{}])[0]
        hero_info = player_stats.get("hero", {})
        print(f"  Hero: {hero_info.get('displayName', 'N/A')}")
        print(f"  Kills: {player_stats.get('kills', 'N/A')}")
        print(f"  Deaths: {player_stats.get('deaths', 'N/A')}")
        print(f"  Assists: {player_stats.get('assists', 'N/A')}")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)