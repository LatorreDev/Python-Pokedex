import click

@click.group()
def pokemons():
    '''Manages the pokemons lifecycle'''
    pass


@pokemons.command()
@click.pass_context
def create(ctx, name, species, typeA, typeB, weight, height, abilities, description):
    '''Create a new pokemon'''


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

