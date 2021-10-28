#!/usr/bin/env python

import functools

from toy_robot.constants import EAST, NORTH, SOUTH, VALID_DIRECTIONS, WEST


def is_valid_direction(direction):
    return direction in VALID_DIRECTIONS


def is_integerable(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def is_coordinates_within_table(table_size, x, y):
    return 0 <= int(x) < table_size['x'] and 0 <= int(y) < table_size['y']


def is_valid_coordinates(table_size, x, y):
    return is_integerable(x) and is_integerable(y) and \
           is_coordinates_within_table(table_size, x, y)


def validate_place(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        state, position = args
        if not is_valid_direction(position['d']):
            return state
        if not is_valid_coordinates(state['table_size'], position['x'], position['y']):
            return state
        return func(*args, **kwargs)

    return wrapper_decorator


def validate_robot_is_placed(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        state = args[0]
        if not state['is_placed']:
            return state
        return func(*args, **kwargs)

    return wrapper_decorator


def coordinates_after_move(state):
    curr_dir = state['direction']
    curr_x = state['coordinates']['x']
    curr_y = state['coordinates']['y']
    after_move_def = {
        NORTH: lambda x, y: (x, y + 1),
        SOUTH: lambda x, y: (x, y - 1),
        EAST: lambda x, y: (x + 1, y),
        WEST: lambda x, y: (x - 1, y)
    }
    return after_move_def[curr_dir](curr_x, curr_y)


def validate_move(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        state = args[0]
        future_x, future_y = coordinates_after_move(state)
        if not is_coordinates_within_table(state['table_size'], future_x, future_y):
            return state
        return func(*args, **kwargs)

    return wrapper_decorator
