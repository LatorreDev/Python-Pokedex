#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import os

POKEMON_SCHEMA = ['name', 'typeA', 'typeB', 'abilities']
POKEMON_TABLE = '.pokemons.csv'

pokemons = [
]


def create_pokemon(pokemon):
    global pokemons

    if pokemon not in pokemons:
        pokemons.append(pokemon)
    else:
        print('Pokemon already exist in pokemon\'s pokedex')


def retrieve_Pokemon():
    pass


def update_pokemon(pokemon_id, updated_pokemon):
    global pokemons

    if len(pokemons) - 1 >= pokemon_id:
        pokemons[pokemon_id] = updated_pokemon
    else:
        print('Pokemon is not in pokedex')
    

def delete_pokemon(pokemon_id):
    global pokemons

    for idx, pokemon in enumerate(pokemons):
        if idx == pokemon_id:
            del pokemons[idx]
            break

def search_pokemon(pokemon_name):

    for pokemon in pokemons:
        if pokemon['name'] != pokemon_name:
            continue
        else:
            return True

def list_pokemons():
    _space_line()
    print ('*             Kanto National Pokedex             *' )
    _space_line()
    print ('index | name      | TypeA | TypeB | abilities')
    for idx, pokemon in enumerate(pokemons):
        print('{uid}     | {name} | {typeA} | {typeB} | {abilities}'.format(
            uid = idx,
            name = pokemon['name'],
            typeA = pokemon['typeA'],
            typeB = pokemon['typeB'],
            abilities = pokemon['abilities']
        ))

def _initialize_pokemons_from_storage():
    with open(POKEMON_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=POKEMON_SCHEMA)

        for row in reader:
            pokemons.append(row)

def _save_pokemons_to_storage():
    tmp_table_name = '{}.tmp'.format(POKEMON_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=POKEMON_SCHEMA)
        writer.writerows(pokemons)

        os.remove(POKEMON_TABLE)
        os.rename(tmp_table_name, POKEMON_TABLE)


def _space_line():
    print ('*' * 50)


def not_in_pokemons():
    print('pokemon is not in pokemons list')

def _get_pokemon_field(field_name):
    field = None

    while not field:
        field = input('What\'s the pokemon {}?: '.format(field_name))

    return field


def _get_pokemon_name():
    pokemon_name = None

    while not pokemon_name:
        pokemon_name = input('What is the pokemon name?: ')

        if pokemon_name == 'exit':
            pokemon_name = None
            break

    if not pokemon_name:
        sys.exit()

    return pokemon_name


def _get_pokemon_from_user():
    pokemon = {
        'name': _get_pokemon_field('name'),
        'typeA': _get_pokemon_field('typeA'),
        'typeB': _get_pokemon_field('typeB'),
        'abilities': _get_pokemon_field('abilities')
    }

    return pokemon

def _print_welcome():
    _space_line()
    print('Welcome to Dave\'s Pokedex')
    _space_line()
    print ('what would you want to do today?')
    print ('[C]reate pokemon')
    print ('[R]etrieve pokemon')
    print ('[U]pdate pokemon')
    print ('[D]elete pokemon')
    print ('[L]ist pokemon')
    print ('[S]earch pokemon')
    print ('[E]xit')

if __name__ == '__main__':

    _initialize_pokemons_from_storage()

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        pokemon = _get_pokemon_from_user()

        create_pokemon(pokemon)
       

    elif command == 'R':
        pass

    elif command == 'U':
        pokemon_id = int(_get_pokemon_field('id'))
        updated_pokemon = _get_pokemon_from_user()

        update_pokemon = (pokemon_id, updated_pokemon)
       

    elif command == 'D':
        pokemon_id = int(_get_pokemon_field('id'))
        delete_pokemon(pokemon_id)

      

    elif command == 'L':
        print(list_pokemons()) 
     

    elif command == 'S':

        pokemon_name = _get_pokemon_field('name')
        found =  search_pokemon(pokemon_name)

        if found:
            print('pokemon is in the pokemon\'s list')
        else:
            print('The pokemon: {} is not in the pokedex'.format(pokemon_name))

    elif command == 'E':
        _space_line
        print('Thanks for using Dave\'s pokedex')
        exit()
    else:
        print ('Invalid command')

_save_pokemons_to_storage()
