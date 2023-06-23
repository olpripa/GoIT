from setuptools import setup

args_dict = {
    "name": 'schonemap',
    "version": '0.0.5',
    "description": 'A script for sorting files by etemsion in folder',
    "author": 'Oleksandr Pripa',
    "author_email": 'ol.pripa@gmail.com',
    "url": 'https://github.com/olpripa/clean_folder',
    "license": 'MIT',
    "packages": ["schonemap"],
}

print(args_dict.get('name'))


def do_setup(args_dict):
    return setup(
        name=args_dict.get('name'),
        version=args_dict.get('version'),
        description=args_dict.get('description'),
        author=args_dict.get('author'),
        author_email=args_dict.get('author_email'),
        url=args_dict.get('url'),
        license=args_dict.get('license'),
        packages=args_dict.get('packages')
    )
