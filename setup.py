import os
import sys
import contextlib

from distutils.spawn import find_executable
from setuptools import setup, find_packages


setup(name='talon',
      version='1.0.2',
      description=("Mailgun library "
                   "to extract message quotations and signatures."),
      long_description=open("README.rst").read(),
      author='Mailgun Inc.',
      author_email='admin@mailgunhq.com',
      url='https://github.com/mailgun/talon',
      license='APACHE2',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "lxml==2.3.3",
          "regex==0.1.20110315",
          "chardet==1.0.1",
          "dnspython==1.11.1",
          "html2text",
          "nose==1.2.1",
          "setuptools>=17.1",
          "mock",
          "coverage",
          "flanker"
          ]
      )
