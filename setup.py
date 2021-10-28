#!/usr/bin/env python

from setuptools import setup

setup(name='toy_robot',
      version='1.0',
      # list folders, not files
      packages=['toy_robot',
                'toy_robot.test'],
      scripts=['toy_robot/bin/run.py'],
      install_requires=['pytest', 'pydux'],
      )
