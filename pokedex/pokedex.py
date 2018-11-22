import click

from pokemons import commands as pokemons_commands

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

cli.add_command(pokemons_commands.all)
