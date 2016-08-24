#!/usr/bin/python3
#coding: utf-8

import os, sys
from getopt import gnu_getopt, GetoptError
from random import randint

try:
    import fr as lc
except ImportError:
    try: import en as lc
    except ImportError:
        ans = ('You do not have any locale file. Continue anyway? (Errors might appear!) [y/n]')
        if ans in 'Yy': pass
        else: exit()


######### I/O Functions ##########

fs_enc = sys.getfilesystemencoding()

def get_string(path):
    '''This function returns a string from the file which path is given as argument or from standard input if provided 'path' is a single hyphen.'''
    if path == '-':
        return sys.stdin.read()
    else:
        try:
            return open(path, mode='rt', encoding=fs_enc, newline=None).read().split('\n~')[0]
        except (IOError, FileNotFoundError):
            err(red(lc.no_file.format(file = path), color)); raise

def get_grid(string, nl):
    '''This function translate a string to a 3-dimensional grid.'''
    return [xy.strip(nl).split(nl) for xy in string.split(nl * 2)]

def fancy(grid):
    '''This method returns a fancier grid to print.'''
    w = len(grid[0][0])
    r = ''
    for z in grid:
        r += '+' + '—' * w + '+\n'
        for y in z:
            r += '|'
            for x in y:
                r += x 
            r += '|\n'
        r += '+' + '—' * w + '+\n\n'
    return r

red = lambda s, c: c * '\033[91m' + s + c * '\033[0m'
dbg = lambda s, c: c * '\033[95m' + s + c * '\033[0m'

err = lambda *s: print(*s, sep = '\n', file=sys.stderr)
out = lambda *s: print(*s, sep = '', end = '')

########## Instruction Pointer ##########

class IP(object):
    '''This class instantiates an instruction pointer. Not more than one IP must be created.'''
    
    def __init__(self):
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
        self.pos = self.dir = [0, 0, 0]
        self.char = None
        self.stack = []
    
    def __repr__(self):
        return lc.v_ip.format(pos = repr(self.pos), char = repr(self.char), dir = repr(self.dir), stack = repr(self.stack))
    
    def get_char(self, grid):
        try:
            self.char = grid[self.pos[2]][self.pos[1]][self.pos[0]]
        except IndexError: err(red(lc.err_pos.format(pos = self.pos), color)); raise
    
    def move(self):
        self.pos = [sum(x) for x in zip(self.pos, self.dir)]
        if self.pos[0] < 0 or self.pos[1] < 0 or self.pos[2] < 0:
            raise IndexError(red(lc.err_pos.format(pos = self.pos), color))
    
    def dev(self, axis):
        n = 2* int(self.pop() > 0) - 1
        self.dir = [n * i for i in axis if bool(self.dir)]
    
    def push(self, n):
        self.stack.append(n)
    
    def push_char(self):
        self.push(ord(self.char))
        self.act = 'i'

    def _input(self, prompt):
        try:
            k = ord(input(prompt)[0])
        except IndexError:
            k = 0
        else:
            return k
    
    def push_hex(self):
        try:
            self.push(eval('0x' + self.char))
        except SyntaxError:
            err(red(lc.err_hex.format(hex = ip.char)))
        else:
            self.act = 'i'
    
    def pop(self, n = -1):
        try:
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
        elif self.char == '—': self.dev([1, 0, 0])
        elif self.char == '|': self.dev([0, 1, 0])
        elif self.char == '⋅': self.dev([0, 0, 1])
        elif self.char == '?': self.push(self._input(prompt_k))
        elif self.char == ':': self.push(eval(input(prompt_n)) or 0)
        elif self.char == ',': self.pop()
        elif self.char == '!': out(chr(self.pop()))
        elif self.char == '=': out(str(self.pop()))
        elif self.char == '&': self.push(self.stack[-1])
        elif self.char == '$': self.push(self.pop(-2))
        elif self.char == '+': self.push(self.pop(-2) + self.pop())
        elif self.char == '-': self.push(self.pop(-2) - self.pop())
        elif self.char == '×': self.push(self.pop(-2) * self.pop())
        elif self.char == '∕': self.push(self.pop(-2)// self.pop())
        elif self.char == '%': self.push(self.pop(-2) % self.pop())
        elif self.char == '*': self.push(self.pop(-2)** self.pop())
        elif self.char == '.': self.push(1)
        elif self.char == '@': self.push(randint(0, self.pop()))
        elif self.char == "'": self.act = 'k'
        elif self.char == '#': self.act = 'n'
        elif self.char == '`': self.char = chr(self.pop()); self.command()
        elif self.char == ';': self.act = 'x'


########## Initial parameters ##########

x_name, *args = sys.argv

try:
    opts, args = gnu_getopt(args, 'vpcbf:h', ['verbose', 'no-prompt', 'no-color', 'backslash', 'file=', 'help'])
except GetoptError:
    err(red(lc.oops, color)); raise
    
path = None
verbose = False

prompt_k = '~ '
prompt_n = '= '
color = False
nlchar = os.linesep

for o,a in opts:
    if o in '--verbose':
        verbose = True
    elif o in '--no-prompt':
        prompt_k = ''
        prompt_n = ''
    elif o in '--color':
        color = True
    elif o in '--backslash':
        nlchar = '\\'
    elif o in '--file':
        path = a
    elif o in '--help':
        err(lc.usage)
        exit()

if path == None and len(args) == 1:
    path = args[0]

ip = IP()
string = get_string(path)
grid = get_grid(string, nlchar)


########## Interpreter core ##########

if verbose: err(dbg(lc.v_path_grid.format(path = path, grid = fancy(grid)), color)) #
while ip.act != 'x':
    try:
        ip.get_char(grid)
        if ip.act == 'i':
            ip.command()
        elif ip.act == 'k':
            ip.push_char()
        elif ip.act == 'n':
            ip.push_hex()
        else:
            raise ValueError(red(lc.err_script.format(x_name), color))
        if verbose: err(dbg(repr(ip), color)) #
        ip.move()
    except (KeyboardInterrupt, EOFError):
        if verbose: print(dbg(lc.end, color)) #
        break
else:
    if ip.stack != []: raise IndexError(red(lc.err_stack, color))
