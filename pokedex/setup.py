from setuptools import setup

setup(
    name = 'Dave_pokedex',
    version = '0.1',
    py_modules =['pokedex.py'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pokedex=pokedex:cli
        ''',
)