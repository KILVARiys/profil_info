import requests

url = "https://api.stratz.com/graphql"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0IjoiNDM1MTcxMTEtOTI0NC00Y2EwLTkwNTAtZmMwZjJiYTBkN2JlIiwiU3RlYW1JZCI6IjExMzY4ODkzOTUiLCJuYmYiOjE3NTE1NjQwODgsImV4cCI6MTc4MzEwMDA4OCwiaWF0IjoxNzUxNTY0MDg4LCJpc3MiOiJodHRwczovL2FwaS5zdHJhdHouY29tIn0.xuTitlm6DC-hytX9m2npjNQLUEWM-qcokMMhNDcDLZw"  # Вставьте свой API-ключ
headers = {
    "User-Agent": "STRATZ_API",
    "Authorization": f"Bearer {token}",
}

# Поиск информации о матче

match_id = 8355606589  # Пример ID матча
query = """
query ($matchId: Long!) {
  match(id: $matchId) {
    id
    durationSeconds
    startDateTime 
    gameMode
    players {
      steamAccountId
      heroId
      kills
      deaths
      assists
    }
  }
}
"""

variables = {"matchId": match_id}

prepared = requests.Request('POST', url, json={"query": query, "variables": variables}, headers=headers).prepare()
for k, v in prepared.headers.items():
    print('{0}: {1}'.format(k, v))

response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    match_data = data["data"]["match"]
    
    print(f"id: {match_data['id']}")
    print(f"durationSeconds: {match_data['durationSeconds']}")
    print(f"startDateTime: {match_data['startDateTime']}")
    print(f"gameMode: {match_data['gameMode']}")
    
    for player in match_data["players"]:
        print("Player:")
        print(f"  AccountId: {player['steamAccountId']}")
        print(f"  heroId: {player['heroId']}")
        print(f"  kills: {player['kills']}")
        print(f"  deaths: {player['deaths']}")
        print(f"  assists: {player['assists']}")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)