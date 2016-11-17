from subprocess import call
import shlex
import os
import pip

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

links = []
requires = []

try:
    requirements = pip.req.parse_requirements('./requirements.txt')
except:
    # new versions of pip requires a session
    requirements = pip.req.parse_requirements('./requirements.txt', session=pip.download.PipSession())

for item in requirements:
    # we want to handle package names and also repo urls
    if getattr(item, 'url', None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, 'link', None): # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))

setup(name='JFE',
      version='1.0',
      packages=['jfe'],
      install_requires=requires
      )

call(shlex.split('bash install_jfe_linux.sh'))
