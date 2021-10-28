# End to end testing that will cover main, store and reducers.

import fileinput

from toy_robot import main


def test_sample_valid_input_file(monkeypatch, capsys):
    def input_a_txt():
        yield "PLACE 0,0,NORTH\n"
        yield "MOVE\n"
        yield "REPORT\n"

    monkeypatch.setattr(fileinput, 'input', input_a_txt)

    main.main()
    out, err = capsys.readouterr()
    assert out == "0,1,NORTH\n"

    def input_b_txt():
        yield "PLACE 0,0,NORTH\n"
        yield "LEFT\n"
        yield "REPORT\n"

    monkeypatch.setattr(fileinput, 'input', input_b_txt)

    main.main()
    out, err = capsys.readouterr()
    assert out == "0,0,WEST\n"

    def input_c_txt():
        yield "PLACE 1,2,EAST\n"
        yield "MOVE\n"
        yield "MOVE\n"
        yield "LEFT\n"
        yield "MOVE\n"
        yield "REPORT\n"

    monkeypatch.setattr(fileinput, 'input', input_c_txt)

    main.main()
    out, err = capsys.readouterr()
    assert out == "3,3,NORTH\n"


def test_sample_valid_input_file_with_multiple_place_commands(monkeypatch, capsys):
    def sample_input():
        yield "PLACE 0,0,NORTH\n"
        yield "MOVE\n"
        yield "PLACE 1,1,EAST\n"
        yield "MOVE\n"
        yield "MOVE\n"
        yield "REPORT\n"

    monkeypatch.setattr(fileinput, 'input', sample_input)

    main.main()
    out, err = capsys.readouterr()
    assert out == "3,1,EAST\n"


def test_sample_valid_input_file_ignoring_moves_causing_fall(monkeypatch, capsys):
    def sample_input():
        yield "PLACE 0,0,WEST\n"
        yield "MOVE\n"
        yield "REPORT\n"

    monkeypatch.setattr(fileinput, 'input', sample_input)

    main.main()
    out, err = capsys.readouterr()
    assert out == "0,0,WEST\n"


def test_sample_valid_input_file_ignoring_fall_off_on_place(monkeypatch, capsys):
    def sample_input():
        yield "PLACE -2,7,WEST\n"
        yield "PLACE 0,0,WEST\n"
        yield "REPORT\n"

    monkeypatch.setattr(fileinput, 'input', sample_input)

    main.main()
    out, err = capsys.readouterr()
    assert out == "0,0,WEST\n"
