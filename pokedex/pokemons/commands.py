import click

from pokemons.services import PokemonsService
from pokemons.models import Pokemon

@click.group()
def pokemons():
    '''Manages the pokemons lifecycle'''
    pass


@pokemons.command()
@click.option('-n', '--name',
    type=str,
    prompt=True,
    help='The pokemon name')

@click.option('-s', '--species',
    type=str,
    prompt=True,
    help='The pokemon specie')

@click.option('-ta', '--TypeA',
    type=str,
    prompt=True,
    help='The pokemon Type A')

@click.option('-tb', '--TypeB',
    type=str,
    prompt=True,
    help='The pokemon Type B')

@click.option('-w', '--weight',
    type=int,
    prompt=True,
    help='The pokemon weight')

@click.option('-h', '--height',
    type=int,
    prompt=True,
    help='The pokemon height')

@click.option('-a', '--abilities',
    type=str,
    prompt=True,
    help='The pokemon abilities')

@click.option('-d', '--description',
    type=str,
    prompt=True,
    help='The pokemon description')

@click.pass_context
def create(ctx, name, species, typea, typeb, weight, height, abilities, description):
    '''Create a new pokemon'''

    pokemon = Pokemon(name, species, typea, typeb, weight, height, abilities, description)
    pokemon_service = PokemonsService(ctx.obj['pokemons_table'])


    pokemon_service.create_pokemon(pokemon)


@pokemons.command()
@click.pass_context
def list(ctx):
    '''List all pokemon'''
    pass


@pokemons.command()
@click.pass_context
def update(ctx,pokemon_uid):
    '''Updates a pokemon'''
    pokemon_service = PokemonService(ctx.obj['pokemons_table'])

    pokemon_list = pokemon_service.list_pokemons()

    pokemon = [pokemon for pokemon in pokemon_list if pokemon['uid'] == pokemon_uid]

    if pokemon:
        Pokemon = _update_pokemon_flow(Pokemon(**pokemon[0]))
        pokemon_service.update_pokemon(pokemon)
    else:
        click.echo('Pokemon not found')


def _update_pokemon_flow(pokemon):
    click.echo('Leave empty if you dont want to modify the value')

    pokemon.name = click.prompt('New name', type=str, default=pokemon.name)
    pokemon.species = click.prompt('New species', type=str, default=pokemon.name)
    pokemon.typeA = click.prompt('New Type A', type=str, default=pokemon.name)
    pokemon.typeB = click.prompt('New Type B', type=str, default=pokemon.name)
    pokemon.weight = click.prompt('New weight', type=int, default=pokemon.name)
    pokemon.height = click.prompt('New height', type=int, default=pokemon.name)
    pokemon.abilities = click.prompt('New abilities', type=str, default=pokemon.name)
    pokemon.description = click.prompt('New description', type=str, default=pokemon.name)


@pokemons.command()
@click.pass_context
def delete(ctx, pokemon_uid):
    '''Deletes a pokemon'''
    pass

all = pokemons

