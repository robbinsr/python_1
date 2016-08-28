#!/usr/bin/env python
_interpreters_ = ['Python 3.5.2 (CPython)']
__author__ = "Russ Robbins"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Russ Robbins"
__email__ = "russ.robbins@outlook.com"
__encoding__ = "UTF-8"
__acknowledgements = ['https://hg.python.org/peps/file/tip/pep-0020.txt']

def hello_world():
    print("Hello, World!")
    print("from a file callable at the operating system command prompt")
    print("and which has a hello_world function defined")
    print("or")
    print("or callable from the python repl using <hello_world()> after ")
    print("function has been imported with <from hello_world_as_module ")
    print('import hello_world')

if __name__ == '__main__':
    hello_world()

# run at os command prompt with python hello_world.py in the same directory
# as the file

# run at python repl with import hello_world, then call hello_world()
