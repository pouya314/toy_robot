#!/usr/bin/env python

from toy_robot.constants import MULTI_PART_COMMANDS, SINGLE_PART_COMMANDS


def handle_multi_part_command(command):
    command_bits = [bit for bit in command.split(' ') if bit]
    action_type = command_bits[0]
    action_args = [bit for bit in command_bits[1].split(',') if bit]
    if not(action_type in MULTI_PART_COMMANDS and len(action_args) == 3):
        return {'type': 'UNKNOWN'}
    x, y, d = action_args
    return {'type': action_type, 'position': {'x': x, 'y': y, 'd': d}}


def handle_single_part_command(command):
    return {'type': command if command in SINGLE_PART_COMMANDS else 'UNKNOWN'}


def handle_command(line):
    cleaned_command = line.strip().upper()
    if not cleaned_command:
        return {'type': 'UNKNOWN'}
    is_multipart_command = len(cleaned_command.split(' ')) > 1
    if is_multipart_command:
        return handle_multi_part_command(cleaned_command)
    else:
        return handle_single_part_command(cleaned_command)
