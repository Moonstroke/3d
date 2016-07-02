#!/usr/bin/python3.5
#coding: utf-8

import params_3d as p3d
from random import randint
import sys, codecs


########### Exceptions ##########

class CommandError(Exception):
    '''Error in 3D script: invalid command'''


########### I/O Functions ##########

string_to_grid = lambda string: [k.split('\n') for k in string.split('\n\n')]

def get_grid(arg):
    if arg == '-':
        return string_to_grid(sys.stdin.read())
    elif p3d.ext * int(p3d.files_have_ext) in arg:
        return string_to_grid(codecs.open(arg, 'r', 'utf-8').read())
    else:
        raise Exception('Invalid argument')


########## Instructions ##########

deviate = lambda n, axis: [(1 - 2 * int(not bool(n))) * axis[k] for k in range(0, len(axis))]

sum_ = lambda stack: stack.pop() + stack.pop()

diff = lambda stack: max(stack.pop() - stack.pop(), 0)

prod = lambda stack: stack.pop() * stack.pop()

quot = lambda stack: stack.pop() // stack.pop()

remd = lambda stack: stack.pop() % stack.pop()

powr = lambda stack: stack.pop() ** stack.pop()

rand = lambda stack: randint(0, stack.pop())

def ivrt(stack):
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n1)
    stack.append(n2)
    
move = lambda pos, axis: [pos[i] + axis[i] for i in range(0, len(pos))]

get_char = lambda grid, pos: grid[pos[2]][pos[1]][pos[0]]
