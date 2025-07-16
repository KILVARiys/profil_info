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
    matches(request: { take: 15 }) {
      series {
        node {
          matches {
            id
            gameMode
            actualRank
            averageRank
            winRates
            players {
              hero {
                id
                name
                displayName
              }
              kills
              deaths
              assists
              goldPerMinute
              experiencePerMinute
            }
          }
        }
      }
    }
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

    print(f"Player ID: {player_data['id']}")
    print(f"Name: {player_data['name']}")
    print(f"Steam ID: {player_data['steamAccountId']}")
    print(f"Rank Tier: {player_data['rankTier']}")
    print(f"Competitive Rank: {player_data['competitiveRank']}")

    for match in player_data['matches']['edges']:
        print("\nMatch:")
        print(f"  Match ID: {match['node']['matchId']}")
        print(f"  Hero: {match['node']['hero']['name']}")
        print(f"  Kills: {match['node']['player']['kills']}")
        print(f"  Deaths: {match['node']['player']['deaths']}")
        print(f"  Assists: {match['node']['player']['assists']}")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)