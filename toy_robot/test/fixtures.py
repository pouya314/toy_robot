import pytest
from toy_robot.constants import DEFAULT_TABLE_SIZE, INITIAL_STATE


@pytest.fixture
def not_placed_state():
    return INITIAL_STATE


@pytest.fixture
def placed_state():
    return {
        'is_placed': True,
        'table_size': {'x': 5, 'y': 5},
        'coordinates': {'x': 0, 'y': 1},
        'direction': 'NORTH'
    }


@pytest.fixture
def placed_at_0_0_facing_west():
    return {
        'is_placed': True,
        'table_size': {'x': 5, 'y': 5},
        'coordinates': {'x': 0, 'y': 0},
        'direction': 'WEST'
    }


@pytest.fixture
def placed_at_0_0_facing_east():
    return {
        'is_placed': True,
        'table_size': {'x': 5, 'y': 5},
        'coordinates': {'x': 0, 'y': 0},
        'direction': 'EAST'
    }


@pytest.fixture
def default_table_size():
    return DEFAULT_TABLE_SIZE
