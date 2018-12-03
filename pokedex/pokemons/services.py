import csv
import os

from pokemons.models import Pokemon
from pokemons.commands import list 


class PokemonsService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_pokemon(self, pokemon):
        with open(self.table_name, mode = 'a') as f:
            writer = csv.DictWriter(f, fieldnames=Pokemon.schema())
            writer.writerow(pokemon.to_dict())

    def update_pokemon (self,updated_pokemon):
        pokemons = self.list_pokemons()

        updated_pokemons = []
        for pokemon in pokemons:
            if pokemon['uid'] == updated_pokemon.uid:
                updated_pokemons.append(updated_pokemon.to_dict())
            else: updated_pokemons.append(Pokemon)

        self._save_to_disk(updated_pokemons)

    def _save_to_disk(self, pokemons):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name) as f:
            writer = csv.DictWriter(f, fieldnames=Pokemon.schema())
            writer.writerows(pokemons)
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
        
            