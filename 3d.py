#!/usr/bin/python3.5
#coding: utf-8

import cmd_3d as x3d


class Exec(Exception):
    '''Interpret top of the stack as a command)'''


########## Initial parameters ##########

position = [0,0,0] #Initial position at (0, 0, 0) North-West-Down corner
axis = [0,0,0] #Initial displacement direction is empty.
#First character of the program must be a directional instruction, or else the pointer won't move across the grid

stack = []

if len(x3s.args[1:]) == 0:
    x3d.args.append('-')
else:
    if '-t' in x3d.args[1:]:
        test = True
        x3d.args.remove('-t')
    else:
        test = False
        grid = x3d.get_grid(x3d.args[1])

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
            if character not in x3d.ascii_printable:
                raise x3d.Command_Error('Invalid instruction at position: ' + position)
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
                stack.append(ord(input(x3d.prompt)[0]))
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
                stack.append(x3d.x3d.quot(stack))
            elif character == '%': # remainder
                stack.append(x3d.remd(stack))
            elif character == '`': # power
                stack.append(x3d.powr(stack))
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
        elif action == 'read':
            stack.append(ord(character))
        elif action == 'count':
            try:
                stack.append(eval('0x' + character))
            except SyntaxError:
                x3d.stderr.write(character + ' is not a valid hex number\n')
                break
        elif action == 'file':
            pass
        else:
            raise ValueError('unsupported action')
        position = x3d.move(position,  axis)
    except (KeyboardInterrupt, EOFError):
        print('')
        break
    except IndexError:
        x3d.stderr.write('Empty input pushes 0')
    except Exec:
        character = stack.pop()
    else:
        if test: print(stack,'\n') #
