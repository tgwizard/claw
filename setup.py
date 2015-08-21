import os

from setuptools import setup, find_packages


setup(
    name='claw',
    version='1.0.0rc4',
    description="Library to extract message quotations and signatures.",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    author='Adam Renberg',
    author_email='tgwizard@gmail.com',
    url='https://github.com/tgwizard/claw',
    license='APACHE2',
    packages=find_packages(exclude=['tests']),
    zip_safe=True,
    install_requires=[
        "lxml==2.3.3",
        "regex==0.1.20110315",
        "html2text",
        "setuptools>=17.1",
    ],
    extras_require={
        'tests': [
            "nose==1.2.1",
            "mock",
            "coverage",
            "flanker",
        ],
        'dev': [
            'twine'
        ]
    },
)
