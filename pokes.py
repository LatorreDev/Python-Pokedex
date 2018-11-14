#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


pokemons = [

    {
        'name': 'Missigno',
        'typeA': 'bird',
        'typeB': 'normal',
        'abilities': 'unknown'
    },

    {
        'name': 'Bulbasaur',
        'typeA': 'grass',
        'typeB': 'poison',
        'abilities': 'overgrow' 
    },

    {
        'name': 'Squirtle',
        'typeA': 'water',
        'typeB': 'none',
        'abilities': 'torrent'   

    },

    {
        'name': 'Charmander',
        'typeA': 'fire',
        'typeB': 'none',
        'abilities': 'blaze' 
    }


]


def create_pokemon(pokemon):
    global pokemons

    if pokemon not in pokemons:
        pokemons.append(pokemon)
    else:
        print('Pokemon already exist in pokemon\'s pokedex')


def retrieve_Pokemon():
    pass


def update_pokemon(pokemon_name, updated_pokemon_name):
    global pokemons

    if pokemon_name in pokemons:
        index = pokemons.index(pokemon_name)
        pokemons[index] = updated_pokemon_name
    else:
        not_in_pokemons()


def delete_pokemon(pokemon_name):
    global pokemons

    if '{name}' in pokemons:
        pokemons.remove(pokemon_name)
        list_pokemons()
    else:
        not_in_pokemons()


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

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        pokemon = {
            'name' : _get_pokemon_field('name'),
            'typeA' : _get_pokemon_field('typeA'),
            'typeB' : _get_pokemon_field('typeB'),
            'abilities' : _get_pokemon_field('abilities')
        }

        create_pokemon(pokemon)
        list_pokemons()

    elif command == 'R':
        pass

    elif command == 'U':
        pokemon_name = _get_pokemon_name()
        updated_pokemon_name = input('Whats is the updated pokemon name?: ')
        update_pokemon (pokemon_name, updated_pokemon_name)
        list_pokemons()

    elif command == 'D':
        pokemon_name = _get_pokemon_name()
        delete_pokemon(pokemon_name)

    elif command == 'L':
        list_pokemons()

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
