from toy_robot import validations
from toy_robot.test.fixtures import default_table_size
from toy_robot.test.fixtures import placed_at_0_0_facing_west
from toy_robot.test.fixtures import placed_at_0_0_facing_east


def test_is_valid_direction():
    assert validations.is_valid_direction('SOUTH') == True
    assert validations.is_valid_direction('NORTH') == True
    assert validations.is_valid_direction('EAST') == True
    assert validations.is_valid_direction('WEST') == True
    assert validations.is_valid_direction('SOUTHWEST') == False
    assert validations.is_valid_direction('FOOBAR') == False


def test_is_integerable():
    assert validations.is_integerable(1) == True
    assert validations.is_integerable('1') == True
    assert validations.is_integerable('one') == False
    assert validations.is_integerable('foobar') == False


def test_is_coordinates_within_table(default_table_size):
    assert validations.is_coordinates_within_table(
        default_table_size, '1', '1') == True
    assert validations.is_coordinates_within_table(
        default_table_size, '-1', '6') == False


def test_is_valid_coordinates(default_table_size):
    assert validations.is_valid_coordinates(
        default_table_size, '1', '1') == True
    assert validations.is_valid_coordinates(
        default_table_size, '-1', '6') == False
    assert validations.is_valid_coordinates(
        default_table_size, '0', 'six') == False


# validate_move, validate_place and validate_robot_is_placed
# are tested as part of test_actions


def test_coordinates_after_move(placed_at_0_0_facing_west):
    assert validations.coordinates_after_move(
        placed_at_0_0_facing_west) == (-1, 0)


def test_coordinates_after_move(placed_at_0_0_facing_east):
    assert validations.coordinates_after_move(
        placed_at_0_0_facing_east) == (1, 0)
