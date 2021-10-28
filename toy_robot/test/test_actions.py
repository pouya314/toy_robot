from toy_robot import actions
from toy_robot.test.fixtures import not_placed_state, placed_state
from toy_robot.test.fixtures import placed_at_0_0_facing_west
from toy_robot.test.fixtures import placed_at_0_0_facing_east


def test_place_valid(not_placed_state):
    position = {'x': '1', 'y': '2', 'd': 'NORTH'}
    got = actions.place(not_placed_state, position)
    expected = {
        'is_placed': True,
        'table_size': {'x': 5, 'y': 5},
        'coordinates': {'x': 1, 'y': 2},
        'direction': 'NORTH'
    }
    assert got == expected


def test_place_invalid(not_placed_state):
    position = {'x': '1', 'y': 'FOOBAR', 'd': 'NORTH'}
    got = actions.place(not_placed_state, position)
    assert got == not_placed_state

    position = {'x': '1', 'y': '0', 'd': 'SOUTHWEST'}
    got = actions.place(not_placed_state, position)
    assert got == not_placed_state

    position = {'x': '-1', 'y': '23', 'd': 'NORTH'}
    got = actions.place(not_placed_state, position)
    assert got == not_placed_state


def test_left_invalid(not_placed_state):
    got = actions.left(not_placed_state)
    assert got == not_placed_state


def test_left_valid(placed_state):
    got = actions.left(placed_state)
    expected = placed_state
    expected['direction'] = 'WEST'
    assert got == expected

    got = actions.left(placed_state)
    expected = placed_state
    expected['direction'] = 'SOUTH'
    assert got == expected

    got = actions.left(placed_state)
    expected = placed_state
    expected['direction'] = 'EAST'
    assert got == expected

    got = actions.left(placed_state)
    expected = placed_state
    expected['direction'] = 'NORTH'
    assert got == expected


def test_right_valid(placed_state):
    got = actions.right(placed_state)
    expected = placed_state
    expected['direction'] = 'EAST'
    assert got == expected

    got = actions.right(placed_state)
    expected = placed_state
    expected['direction'] = 'SOUTH'
    assert got == expected

    got = actions.right(placed_state)
    expected = placed_state
    expected['direction'] = 'WEST'
    assert got == expected

    got = actions.right(placed_state)
    expected = placed_state
    expected['direction'] = 'NORTH'
    assert got == expected


def test_right_invalid(not_placed_state):
    got = actions.right(not_placed_state)
    assert got == not_placed_state


def test_move_valid(placed_at_0_0_facing_east):
    got = actions.move(placed_at_0_0_facing_east)
    expected = placed_at_0_0_facing_east
    expected['coordinates']['x'] += 1
    assert got == expected


def test_move_invalid(not_placed_state):
    got = actions.move(not_placed_state)
    assert got == not_placed_state


def test_move_invalid_outside_table(placed_at_0_0_facing_west):
    got = actions.move(placed_at_0_0_facing_west)
    assert got == placed_at_0_0_facing_west


def test_report_invalid(not_placed_state):
    got = actions.report(not_placed_state)
    assert got == not_placed_state


def test_report_valid(placed_state):
    got = actions.report(placed_state)
    expected = placed_state
    assert got == expected
