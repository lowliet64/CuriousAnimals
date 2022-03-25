
from django.core.management.base import BaseCommand
from ...models import Pokemon
import datetime
import requests
import json
def populate_pokemons():
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1126')
        pokemons = response.json()['results']
        for pokemon in pokemons:
            pokemon_response = requests.get(pokemon.get('url'))
            pokemon_data = pokemon_response.json()
            new_pokemon ={
                'id':pokemon_data['id'],
                'name':pokemon_data['name'],
                'types':[pokemon_data['types'][i]['type']['name'] for i in range(len(pokemon_data['types']))],
                'sprite':pokemon_data['sprites']['front_shiny']
            }
            product = Pokemon(name=new_pokemon['name'],types=json.dumps(new_pokemon['types']),sprite=new_pokemon['sprite'])
            product.save()
class Command(BaseCommand):
  def handle(self, *args, **options):
    populate_pokemons()
    # clear_data()
    print("completed")