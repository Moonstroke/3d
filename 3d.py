#!/usr/bin/python3.5
#coding: utf-8

import cmd_3d as x3d

from string import printable as ascii_printable
from sys import argv as args

class Exec(Exception):
    '''Interpret top of the stack as a command)'''


########## Initial parameters ##########

cr_lf = '\n\r\n'
prompt = '~ '
position = [0,0,0] #Initial position at (0, 0, 0) North-West-Down corner
axis = [0,0,0] #Initial displacement direction is empty.
#First character of the program must be a directional instruction, or else the pointer won't move across the grid

stack = []
if '-t' in args:
    test = True
    args.remove('-t')
else:
    test = False
try:
    grid = x3d.string_to_grid(x3d.get_string(args[1]))
except IndexError:
    x3d.print_err('Script Error: Wrong arguments')

if test: print(grid) #
run = True
action = 'interpret'


########## Interpreter core ##########

while run:
    try:
        character = x3d.get_char(grid, position)
        if test:
            print(position) #
            print(character) #
        if action == 'interpret':
            if character not in ascii_printable:
                raise x3d.Command_Error('Invalid instruction at position ' + position)
            elif character == '<': #IP movement blocks WEST
                axis = [-1,0,0]
            elif character == '>': # EAST
                axis = [1,0,0]
            elif character == '^': # NORTH
                axis = [0,-1,0]
            elif character == 'v': # SOUTH
                axis=[0,1,0]
            elif character == 'x': # DOWN
                axis = [0,0,-1]
            elif character == 'o': # UP
                axis = [0,0,1]
            elif character == '_': #Deviator E/W
                axis = x3d.deviate(stack.pop(), [1,0,0])
            elif character == '|': # N/S
                axis = x3d.deviate(stack.pop(), [0,1,0])
            elif character == '.': # D/U
                axis = x3d.deviate(stack.pop(), [0,0,1])
            elif character == '?': #Input and push ascii code
                stack.append(ord(input(prompt)[0]))
            elif character == ',': #Pop silently
                stack.pop()
            elif character == '!': #Pop and print as ASCII
                print(chr(stack.pop()),end='')
            elif character == '@': # Assigner
                action = 'assign'
            elif character == '+': #Operators (pop 2 numbers, operate on them and push result): sum
                stack.append(x3d.sum_(stack))
            elif character == '-': # difference
                stack.append(x3d.diff(stack))
            elif character == '*': # product
                stack.append(x3d.prod(stack))
            elif character == '/': # quotient
                stack.append(x3d.quot(stack))
            elif character == '%': # remainder
                stack.append(x3d.mod_(stack))
            elif character == '`': # power
                stack.append(x3d.pow_(stack))
            elif character == '@': #Random number pushed onto the stack
                stack.append(x3d.rand(stack))
            elif character == '$': #Invert top two items of the stack
                x3d.ivrt(stack)
            elif character == '\'': #Pusher as character: 1 character
                interpret = 'read'
            elif character == '\\': #Pusher as hexadecimal number: 1 character
                interpret = 'count'
            elif character == '"': #Interpreter
                raise Exec
            elif character == '&': #Duplicate top of the stack
                stack.append(stack[len(stack) - 1])
            elif position == [0,0,0] and character == 'q': #Quiner
                print('q')
                run=False
            elif character == ';': #End of program
                run = False
            else: #Every other characters are NOPs.
                pass
        elif character == '?':
            for k in input(prompt)[::-1]:
                stack.append(k)
        elif action == 'read' and character != ')':
            stack.append(ord(character))
        elif action == 'count' and character != ']':
            try:
                stack.append(eval('0x' + character))
            except SyntaxError:
                x3d.print_err(character + ' is not a valid hex number')
                break
        elif action == 'file' and character != '}':
            pass
        elif character in ')]}':
            action = 'interpret'
        else:
            raise ValueError
        position = x3d.move(position,  axis)
    except (KeyboardInterrupt, EOFError):
        print('')
        break
    except IndexError:
        print_err('Empty input pushes 0')
    except Exec:
        character = stack.pop()
    else:
        if test: print(stack,'\n') #
