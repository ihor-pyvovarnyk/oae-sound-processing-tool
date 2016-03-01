from setuptools import setup

with open('README.md') as f:
    readme = f.read();

with open('LICENSE') as f:
    license = f.read()

setup(
    name = 'oae-sound-processing-tool',
    version = '0.0.1',
    description = 'OAE Sound Processing Tool',
    long_description = readme,
    url = 'https://github.com/ihor-pyvovarnyk/oae-sound-processing-tool',
    author = 'Ihor Pyvovarnyk',
    author_email = 'igor.pivovarnik@gmail.com',
    license = license,
    install_requires = [
        'scipy',
        'numpy'
    ]
)