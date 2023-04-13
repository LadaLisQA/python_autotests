import requests
token='2ad8f12f23c1341f9dcb2bb9d049f848'
base_url='https://pokemonbattle.me:9104'
response = requests.post(f'{base_url}/pokemons', headers={"trainer_token": token, "Content-Type": "application/json"}, json={
    "name": "Киви",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response.text)

response = requests.put(f'{base_url}/pokemons', headers={"trainer_token": token, "Content-Type": "application/json"}, json={
    "pokemon_id": "9160",
    "name": "Карл",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
})
print(response.text)

response = requests.post(f'{base_url}/trainers/add_pokeball', headers={"trainer_token": token, "Content-Type": "application/json"}, json={
    "pokemon_id": "9160"
})
print(response.text)
