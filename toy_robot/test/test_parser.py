from toy_robot.parser import handle_command


def test_handle_command_with_proper_place_command():
    line = 'PLACE 1,1,NORTH'
    got = handle_command(line)
    expected = {'type': 'PLACE', 'position': {'x': '1', 'y': '1', 'd': 'NORTH'}}
    assert got == expected


def test_handle_command_with_proper_move_command():
    line = 'MOVE'
    got = handle_command(line)
    expected = {'type': 'MOVE'}
    assert got == expected


def test_handle_command_with_proper_left_command():
    line = 'LEFT'
    got = handle_command(line)
    expected = {'type': 'LEFT'}
    assert got == expected


def test_handle_command_with_proper_right_command():
    line = 'RIGHT'
    got = handle_command(line)
    expected = {'type': 'RIGHT'}
    assert got == expected


def test_handle_command_with_proper_report_command():
    line = 'REPORT'
    got = handle_command(line)
    expected = {'type': 'REPORT'}
    assert got == expected


def test_handle_command_with_bad_command():
    for line in ['', '    ', 'FOOBAR', 'PLACE', 'PLACE 0  0,NORTH']:
        got = handle_command(line)
        expected = {'type': 'UNKNOWN'}
        assert got == expected


def test_handle_command_strips_and_up_cases_valid_command():
    line = '          repoRt           '
    got = handle_command(line)
    expected = {'type': 'REPORT'}
    assert got == expected


def test_multi_part_command_valid():
    for line in ['  place 0,0,north     ,,,', 'PLACE            0,0,NORTH,,,,']:
        got = handle_command(line)
        expected = {'type': 'PLACE', 'position': {'x': '0', 'y': '0', 'd': 'NORTH'}}
        assert got == expected


def test_multi_part_command_invalid():
    for line in ['  place 0,0,   north     ,,,', 'PLACE    1,', 'put 1,1,north']:
        got = handle_command(line)
        expected = {'type': 'UNKNOWN'}
        assert got == expected
