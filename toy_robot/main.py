#!/usr/bin/env python

from __future__ import print_function

import fileinput

from toy_robot.parser import handle_command
from toy_robot.store import store


def main():
    """
    Startup function for running the toy robot simulator
    """
    for line in fileinput.input():
        action = handle_command(line)
        store.dispatch(action)
