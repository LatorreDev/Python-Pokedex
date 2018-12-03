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
    pass


@pokemons.command()
@click.pass_context
def delete(ctx, pokemon_uid):
    '''Deletes a pokemon'''
    pass

all = pokemons

