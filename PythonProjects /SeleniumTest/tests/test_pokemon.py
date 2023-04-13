import requests
import pytest
base_url='https://pokemonbattle.me:9104'

def test_status_code():
    response=requests.get(f'{base_url}/trainers')
    assert response.status_code == 200

def test_part_of_body():
    response = requests.get(f'{base_url}/trainers', params={'trainer_id' : 3982})
    assert response.json()['trainer_name'] == 'Тэд'