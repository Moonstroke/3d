#!/usr/bin/python3.5
#coding: utf-8


from random import randrange
from string import printable as ascii_printable
from sys import argv as args

cr_lf = "\n\r\n"
prompt = "~"
test = bool("-t" in args)


########### Exceptions ##########

class CommandError(Exception):
    """Error in 3D script: invalid command"""


########### I/O Functions ##########

get_file = lambda path: open(path, 'r').read()

def get_stdin():
    return ""

string_to_grid = lambda string: [k.split('\n') for k in string.split('\n\n')]

def get_string(arg):
    if arg == "-":
        return get_stdin()
    else:
        return get_file(arg)


########## Instructions ##########

deviate = lambda n, axis: [(1 - 2 * int(not bool(n)))*axis[k] for k in range(0,len(axis))]

sum_ = lambda stack: stack.pop() + stack.pop()

diff = lambda stack: max(stack.pop() - stack.pop(), 0)

prod = lambda stack: stack.pop() * stack.pop()

quot = lambda stack: stack.pop() // stack.pop()

mod_ = lambda stack: stack.pop() % stack.pop()

pow_ = lambda stack: stack.pop() ** stack.pop()

rdom = lambda stack: randint(0,stack.pop())

def ivrt(stack):
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n1)
    stack.append(n2)
    
move = lambda pos,axis: [pos[i] + axis[i] for i in range(0,len(pos))]

get_char = lambda grid,pos: grid[pos[2]][pos[1]][pos[0]]


