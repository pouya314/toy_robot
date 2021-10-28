#!/usr/bin/env python

from toy_robot.actions import left, move, place, report, right
from toy_robot.constants import INITIAL_STATE, LEFT, MOVE, PLACE, REPORT, RIGHT


def simulator(state, action):
    if state is None:
        state = INITIAL_STATE

    if action is None:
        return state
    elif action['type'] == PLACE:
        return place(state, action['position'])
    elif action['type'] == LEFT:
        return left(state)
    elif action['type'] == RIGHT:
        return right(state)
    elif action['type'] == MOVE:
        return move(state)
    elif action['type'] == REPORT:
        return report(state)
    else:
        return state
