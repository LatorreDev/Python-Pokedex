import csv

from pokemons.models import Pokemon


class PokemonsService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, pokemon):
        with open(self.table_name, mode = 'a') as f:
            writer = csv.DictWriter(f, fieldnames=Pokemon.schema())
            writer.writerow(pokemon.to_dict())
            