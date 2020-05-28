import setuptools
from distutils.core import setup

setup(
    name='angrop',
    version='8.20.5.27',
    description='The rop chain builder based off of angr',
    packages=['angrop'],
    install_requires=[
        'progressbar',
        'angr==8.20.5.27',
    ],
)
