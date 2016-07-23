#!/usr/bin/python3
#coding: utf-8

import sys, getopt, codecs, lc
from random import randint


######### I/O Functions ##########

def get_string(path):
    '''This function returns a string from the file which path is given as argument or from standard input if provided 'path' is a single hyphen.'''
    if path == '-':
        return sys.stdin.read()
    else:
        try:
            return codecs.open(path, 'r', 'utf-8').read()
        except (IOError, FileNotFoundError):
            err(lc.no_file[lc.lg].format(file = path))
            raise

def get_grid(string):
    '''This function translate a string to a 3-dimensional grid.'''
    return [xy.split('\n') for xy in string.split('\n\n')][0:-1]

def fancy(grid):
    '''This method returns a fancier way to print the grid on screen.'''
    w = len(grid[0][0])
    r = '\n'
    for z in grid:
        r += '+' + '-' * (w + 2) + '+\n'
        for y in z:
            r += '| '
            for x in y:
                r += x 
            r += ' |\n'
        r += '+' + '-' * (w + 2) + '+\n\n'
    return r

red = lambda s, c: c * '\033[91m' + s + c * '\033[0m'
dbg = lambda s, c: c * '\033[95m' + s + c * '\033[0m'

err = sys.stderr.write
out = sys.stdout.write

def get(prompt):
    k = input(prompt)
    if len(k) == 0: return 0
    else: return ord(k[0])

neg = lambda l: [-l[i] for i in range(0, len(l))]
l_abs = lambda l: [abs(l[i]) for i in range(0,len(l))]


########## Instruction Pointer ##########

class IP(object):
    '''This class instantiates an instruction pointer. Not more than one IP must be created.'''
    
    def __init__(self, path):
        '''This method instantiates the attributes of the IP:
'act' is the action the IP performs on the character.
Possible values can be: 'i' default, interpret char as command
                        'k' push on stack as a character
                        'n' push on stack as an hex number
                        'x' stop program

'pos' is the position of the IP on the grid.

'dir' is the direction the IP moves towards.

'char' is the current character the IP is reading.

'stack' is the stack the IP performs actions to.'''
    
        self.act = 'i'
        self.pos = [0, 0, 0]
        self.dir = [0, 0, 0]
        self.char = None
        self.stack = []
    
    def __repr__(self):
        return lc.v_ip[lc.lg].format(pos = repr(self.pos), char = repr(self.char), dir = repr(self.dir), stack = repr(self.stack))
    
    def get_char(self, grid):
        try:
            self.char = grid[self.pos[2]][self.pos[1]][self.pos[0]]
        except IndexError: err(red(lc.wrong_pos[lc.lg].format(pos = ip.pos), do_color)); raise
    
    def move(self):
        self.pos = [sum(x) for x in zip(self.pos, self.dir)]
    
    def dev(self, axis):
        n = 2* int(self.pop() > 0) - 1
        self.dir = [n * axis[i] for i in range(0, len(axis)) if bool(self.dir)]
    
    def push(self, n):
        self.stack.append(n)
    
    def push_char(self):
        self.stack.append(ord(self.char))
        self.act = 'i'
    
    def push_hex(self):
        try:
            self.stack.append(eval('0x' + self.char))
        except SyntaxError:
            err(red(lc.wrong_hex[lc.lg].format(hex = ip.char), do_color))
        else:
            self.act = 'i'
    
    def pop(self, n = None):
        try:
            if n == None:
                return self.stack.pop()
            else:
                return self.stack.pop(n)
        except IndexError:
            return 0
    
    def command(self):
        '''This method binds every character to its corresponding instruction.'''
        if   self.char == '<': self.dir = [-1, 0, 0]
        elif self.char == '>': self.dir = [ 1, 0, 0]
        elif self.char == '^': self.dir = [ 0,-1, 0]
        elif self.char == 'v': self.dir = [ 0, 1, 0]
        elif self.char == 'x': self.dir = [ 0, 0,-1]
        elif self.char == 'o': self.dir = [ 0, 0, 1]
        elif self.char == '_': self.dev([1, 0, 0])
        elif self.char == '|': self.dev([0, 1, 0])
        elif self.char == '.': self.dev([0, 0, 1])
        elif self.char == '?': self.push(get(dbg(prompt, do_color)))
        elif self.char == ',': self.pop()
        elif self.char == '!': out(chr(self.stack.pop()))
        elif self.char == '&': self.push(self.stack[len(self.stack[1:])])
        elif self.char == '$': self.push(self.pop(-2))
        elif self.char == '+': self.push(self.pop(-2) + self.pop())
        elif self.char == '-': self.push(self.pop(-2) - self.pop())
        elif self.char == '*': self.push(self.pop(-2) * self.pop())
        elif self.char == '∕': self.push(self.pop(-2)// self.pop())
        elif self.char == '%': self.push(self.pop(-2) % self.pop())
        elif self.char == '`': self.push(self.pop(-2)** self.pop())
        elif self.char == '@': self.push(randint(0, self.pop()))
        elif self.char == "'": self.act = 'k'
        elif self.char == '#': self.act = 'n'
        elif self.char == '"': self.char = chr(self.pop()); self.command()
        elif self.char == ';': self.act = 'x'
        else: pass


########## Initial parameters ##########

args = sys.argv
x_name = args.pop(0)
opts, args = getopt.gnu_getopt(args, 'vpcf:l:h', ['verbose', 'prompt', 'no-color', 'file=', 'language=', 'help'])

path = None
verbose = False
prompt = ''
do_color = True

for o,a in opts:
    if o in '--verbose':
        verbose = True
    elif o in '--prompt':
        prompt = dbg('~ ', do_color)
    elif o in '--no-color':
        do_color = False
    elif o in '--file':
        path = a
    elif o in '--language':
        lc.lg = a
    elif o in '--help':
        err(lc.usage[lc.lg])
if path == None and len(args) == 1:
    path = args[0]
else: raise getopt.GetoptError


########## Interpreter core ##########

ip = IP(path)

grid = get_grid(get_string(path))

if verbose: err(dbg(lc.v_init[lc.lg].format(path = path, grid = fancy(grid)), do_color)) #

while ip.act != 'x':
    try:
        if verbose: err(dbg(repr(ip), do_color)) #
        ip.get_char(grid)
        if ip.act == 'i':
            ip.command()
        elif ip.act == 'k':
            ip.push_char()
        elif ip.act == 'n':
            ip.push_hex()
        else:
            raise ValueError(red(lc.err_script[lc.lg].format(x_name), do_color))
        ip.move()
    except (KeyboardInterrupt, EOFError):
        if verbose: print(dbg(lc.end[lc.lg], do_color)) #
        break
else:
    if ip.stack != []: raise IndexError(red(lc.err_stack[lc.lg], do_color))
#END
