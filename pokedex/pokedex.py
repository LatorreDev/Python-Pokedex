import click

from pokemons import commands as pokemons_commands

POKEMONS_TABLE = '.pokemons.csv'
@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['pokemons_table'] = POKEMONS_TABLE

cli.add_command(pokemons_commands.all)
