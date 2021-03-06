#!/usr/bin/env python
_interpreters_ = ['Python 3_instructions.5.3_instructions (CPython)']
__author__ = "Russ Robbins"
__license__ = "MIT"
__version__ = "0.0.4_resources"
__maintainer__ = "Russ Robbins"
__email__ = "russ.robbins@outlook.com"
__encoding__ = "UTF-8"
__acknowledgements = ['https://hg.python.org/peps/file/tip/pep-0020.txt']


def hello_world():
    print("Hello, World!")
    print("from a file callable at the operating system command prompt")
    print("and which has a hello_world function defined")
    print("or ")
    print("from a function callable from the python REPL using ")
    print("'hello_world()' after function has been imported with ")
    print("'from hello_world_as_module import hello_world'")


if __name__ == '__main__':
    hello_world()

# run at os command prompt with python 1a_hello_world.py in the same directory
# as the file

# run at python repl with import hello_world, then call hello_world()
