#!/usr/bin/env python

import itertools

from toy_robot.constants import EAST, NORTH, SOUTH, WEST
from toy_robot.validations import (coordinates_after_move, validate_move,
                                   validate_place, validate_robot_is_placed)


@validate_place
def place(state, position):
    updates = {
        'is_placed': True,
        'coordinates': {'x': int(position['x']), 'y': int(position['y'])},
        'direction': position['d']
    }
    return dict(itertools.chain(state.items(), updates.items()))


@validate_robot_is_placed
def left(state):
    curr_dir = state['direction']
    left_turn_def = {NORTH: WEST, SOUTH: EAST, EAST: NORTH, WEST: SOUTH}
    updates = {'direction': left_turn_def[curr_dir]}
    return dict(itertools.chain(state.items(), updates.items()))


@validate_robot_is_placed
def right(state):
    curr_dir = state['direction']
    right_turn_def = {NORTH: EAST, SOUTH: WEST, EAST: SOUTH, WEST: NORTH}
    updates = {'direction': right_turn_def[curr_dir]}
    return dict(itertools.chain(state.items(), updates.items()))


@validate_robot_is_placed
@validate_move
def move(state):
    new_x, new_y = coordinates_after_move(state)
    updates = {'coordinates': {'x': new_x, 'y': new_y}}
    return dict(itertools.chain(state.items(), updates.items()))


@validate_robot_is_placed
def report(state):
    print('{x},{y},{direction}'.format(
        x=state['coordinates']['x'],
        y=state['coordinates']['y'],
        direction=state['direction']))
    return state
