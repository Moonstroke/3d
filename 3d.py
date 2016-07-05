#!/usr/bin/python3.5
#coding: utf-8

from random import randint
import sys, codecs
#from string import printable as ascii_printable
from sys import argv as args

ext = '.x3d'
files_have_ext = False
prompt = '~ '


########### Exceptions ##########

class Error(Exception):
    '''Error in 3D script: '''

class Exec(Exception):
    '''Interpret top of the stack as a command'''

class EndOfProgram(Exception):
    '''End Of Program: Stop'''

########### I/O Functions ##########

string_to_grid = lambda string: [k.split('\n') for k in string.split('\n\n')]

def get_grid(arg):
    if arg == '-':
        return string_to_grid(sys.stdin.read())
    elif ext * int(files_have_ext) in arg:
        return string_to_grid(codecs.open(arg, 'r', 'utf-8').read())
    else:
        raise Error('Invalid argument')


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

def command(char):
    
    try:
        return cmd[char]
    except KeyError:
        pass

def quine(pos, char, run):
    if pos == [0,0,0]:
        print(char)
        raise EndOfProgram

def do_raise(Except):
    raise Except


########## Initial parameters ##########

position = [0,0,0] #Initial position at (0, 0, 0) North-West-Down corner
axis = [0,0,0] #Initial displacement direction is empty.
#First character of the program must be a directional instruction, or else the pointer won't move across the grid

stack = []

if len(args[1:]) == 0:
    args.append('-')
else:
    if '-d' in args[1:]:
        debug = True
        args.remove('-d')
    else:
        debug = False
        grid = get_grid(args[1])

if debug: print(grid) #

run = True
action = 'interpret'


########## Syntactic dictionary ##########

# Change it ad libitum and change the language
# It will ruin my work, go ahead

cmd = {'<': deviate(axis, 0, [1,0,0]),           #Movement West
       '>': deviate(axis, 1, [1,0,0]),           #         East
       '^': deviate(axis, 0, [0,1,0]),           #         North
       'v': deviate(axis, 1, [0,1,0]),           #         South
       'x': deviate(axis, 0, [0,0,1]),           #         Upwards
       'o': deviate(axis, 1, [0,0,1]),           #         Downwards
       '_': deviate(axis, stack.pop(), [1,0,0]), #Deviator W/E
       '|': deviate(axis, stack.pop(), [0,1,0]), #         N/S
       '.': deviate(axis, stack.pop(), [0,0,1]), #         D/U
       '?': stack.append(ord(input(prompt)[0])), #Input and push ascii code
       ',': stack.pop(),                         #Pop silently
       '!': print(chr(stack.pop()),end=''),      #Pop and print as ASCII
       '@': action('assign'),                    # Assign to variable
       '=': action('return'),                    # Return value of variable
       '+': stack.append(sum_(stack)),           #Operators (pop 2 numbers, operate on them and push result): sum
       '-': stack.append(diff(stack)),           #                                                            difference
       '*': stack.append(prod(stack)),           #                                                            product
       '∕': stack.append(quot(stack)),           #                                                            quotient
       '%': stack.append(remd(stack)),           #                                                            remainder
       '`': stack.append(powr(stack)),           #                                                            power
       '$': ivrt(stack),                         #Invert top two items of the stack
       "'": action('read'),                      #Push as character: 1 character
       '\\':action('count'),                     #     as hexadecimal number: 1 character
       '#': stack.append(rand(stack)),           #     random integer
       '"': do_raise(Exec),                      #Interpreter
       '&': stack.append(stack[len(stack) - 1]), #Duplicate top of the stack
       'q': quine(position, run),                #Quine (little Easter egg)
       ';': do_raise(EndOfProgram)               #End of program
}                                                #Every other characters are NOPs.


########## Interpreter core ##########

while True:
    try:
        character = get_char(grid, position)
        if debug:
            print(position) #
            print(character) #
        if action == 'interpret':
            try:
                eval(command(character))
            except IndexError:
                stack.append(0)
        elif action == 'read':
            stack.append(ord(character))
        elif action == 'count':
            try:
                stack.append(eval('0x' + character))
            except SyntaxError:
                sys.stderr.write(character + ' is not a valid hex number\n')
                break
        elif action == 'assign':
            pass
        elif action == 'return':
            pass
        else:
            raise ValueError('unsupported action')
        position = move(position, axis)
    except (KeyboardInterrupt, EOFError):
        print()
        break
    except IndexError:
        sys.stderr.write('Empty input pushes 0')
    except Exec:
        character = stack.pop()
    except EndOfProgram:
        break
    else:
        if debug: print(stack, '\n') #
