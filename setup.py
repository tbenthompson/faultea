from setuptools import setup

version = open('VERSION').read()

try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = open('README.md').read()

setup(
    packages = ['faultea'],

    install_requires = ['numpy'],
    zip_safe = False,

    name = 'faultea',
    version = version,
    description = '',
    long_description = description,

    url = 'https://github.com/tbenthompson/faultea',
    author = 'T. Ben Thompson',
    author_email = 't.ben.thompson@gmail.com',
    license = 'MIT',
    platforms = ['any']
)
