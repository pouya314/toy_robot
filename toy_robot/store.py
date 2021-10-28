#!/usr/bin/env python

import pydux

from toy_robot.reducers import simulator

# Create a Redux store holding the state of our app.
# Its API is { subscribe, dispatch, get_state }.
store = pydux.create_store(simulator)

# We can use subscribe() to update the UI in response to state changes.
# For example: this could be used to show error messages on the screen but
# this is not a requirement so skipping it for now to keep things simple.
#
# def handle_ui():
#     print(store.get_state())
# store.subscribe(handle_ui)
