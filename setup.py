import os

from setuptools import setup, find_packages


setup(
    name='claw',
    version='1.3.0',
    description='Library to extract message quotations and signatures.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Tictail',
    author_email='tech+pip-claw@gmail.com',
    url='https://github.com/tictail/claw',
    license='APACHE2',
    packages=find_packages(exclude=['tests']),
    zip_safe=True,
    install_requires=[
        'lxml==2.3.3',
        'regex>=2015.07.19',
        'html2text',
        'setuptools>=17.1',
    ],
    extras_require={
        'tests': [
            'pytest==2.7.2',
            'nose==1.3.7',
            'mock==1.3.0',
            'coverage==3.7.1',
            'flanker',
            'tox',
        ],
        'dev': [
            'twine',
        ]
    },
)
