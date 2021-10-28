# Toy Robot Code Challenge

## Description and Requirements:
The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.
Create a ​console application​ that can read in commands of the following form -
```
PLACE X,Y,F
MOVE 
LEFT
RIGHT
REPORT
```
PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner. It is required that the first command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.
MOVE will move the toy robot one unit forward in the direction it is currently facing.
LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. REPORT will announce the X,Y and F of the robot. This can be in any form, but standard output is sufficient.
A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands.
Input can be from a file, or from standard input, as the developer chooses.
Provide test data to exercise the application.
It is not required to provide any graphical output showing the movement of the toy robot.
The application should handle error states appropriately and be robust to user input.

### Constraints:
The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any move that would cause the robot to fall must be ignored.

### Example Input and Output:
```
a)----------------
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH

b)----------------
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST

c)----------------
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
```


## Environments:
This application was developed on Mac OS X, version 11.4 (Big Sur), however it should run on all Unix-like operating systems.

Another (better) way to distribute this project would be to use `Docker` (which I am familiar with). However I decided it was outside of the scope of this coding challenge, so in the interest of saving time I went with a standard python and virtual environment setup (as described below).


## Installation & Usage:
(Assuming when you run this command `python --version` you will see the following output
``Python 3.9.6``)

In the root directory invoke:
```bash
python -m venv venv
source venv/bin/activate
pip install -e .
```

(the dot at the end of pip install command is important)

Then run the app with one of the sample input files, like so:
```bash
run.py input_a.txt
run.py input_b.txt
run.py input_c.txt
```
Or use your own input file. 

Or you can also give it a list of files (chain filenames). 

Or just invoke `run.py` and use standard input to enter commands manually. 


## Tests:
To run the tests:
```bash
pytest
```
All tests are located in `test` directory under `toy_robot` package.


## Code Structure and Overall flow:
The project is structured like most other standard python projects. Install requirements and script runner are defined in `setup.py`. All business logic is located within the `toy_robot` package. 

I have implemented this program in a functional style. This is a paradigm supported by Python and is one of my favorite programming styles because, in my experience, it usually results in a clean, predictable, testable and robust implementation. I have tried to use immutable data structures and side-effect-free and stateless functions throughout the implementation as much as practically possible. The report command for example prints which is a side effect. This, and other UI updates (validation messages) for example, could be achieved through subscribing to the store and responding to state changes, but I felt that was all outside of the scope of this code test, so I decided not to go down that path.

I have used `pydux` which is `redux` implemented in Python. This is basically to help manage application state. The nice thing about `pydux` is that you can structure the state (and application) in any way you want which makes it very scalable and extendable.

General flow of the application is as follows:

Invoking `run.py` in `bin` folder calls the `main` function. From there, input is captured from an input file (or a list of files) or from the user and commands are sent to `parser` for parsing obviously. The resulting action is then dispatched to the `store`. It's worth mentioning that the store is created based on the `reducer` which is a pure function with (state, action) => state signature. It describes how an `action` transforms the state into the next state. Each action basically contains the core functionality of the application. `Validations` are done through the decorator feature of Python to keep business logic & validation codes separate.


## License:
The MIT License (MIT)

Copyright (c) 2021 Pouya Arvandian

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
