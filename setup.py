from setuptools import setup

import fnphat.cityweather

setup(name='fnphat.cityweather',
    version = fnphat.cityweather.__version__,
    license = "MIT",
    description = 'Get the weather of a canadian city.',
    author = 'fnphat',
    author_email = 'fnphat@gmail.com',
    url = 'https://github.com/fnphat/cityweather',
    packages=['fnphat', 'fnphat.cityweather'],
    install_requires = ['data-gc-ca-api >= 0.2.4'],
)      