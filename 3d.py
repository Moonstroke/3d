#!/usr/bin/python3
#coding: utf-8

import lc, os
from getopt import gnu_getopt, GetoptError
from random import randint


######### I/O Functions ##########

fs_enc = os.sys.getfilesystemencoding()

def get_string(path):
    '''This function returns a string from the file which path is given as argument or from standard input if provided 'path' is a single hyphen.'''
    if path == '-':
        return os.sys.stdin.read()
    else:
        try:
            return open(path, mode='rt', encoding=fs_enc, newline=None).read()
        except (IOError, FileNotFoundError):
            err(lc.no_file[lc.lg].format(file = path))
            raise

def get_grid(string, nl):
    '''This function translate a string to a 3-dimensional grid.'''
    if string.endswith(nl):
        string = string[0:-1]
    return [xy.split(nl) for xy in string.split(nl * 2)]

def fancy(grid):
    '''This method returns a fancier way to print the grid on screen.'''
    w = len(grid[0][0])
    r = ''
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

err = os.sys.stderr.write
out = os.sys.stdout.write

def get(prompt, type):
    k = input(prompt)
    if len(k) == 0: return 0
    elif type == 'k': return ord(k[0])
    elif type == 'n': return eval(k)


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
        return lc.v_ip[lc.lg].format(pos = repr(self.pos), char = repr(self.char), dir = repr(self.dir), stack = repr(self.stack))
    
    def input(self, prompt):
        if self.act == 'i':
            return input(prompt)
        
    def get_char(self, grid):
        try:
            self.char = grid[self.pos[2]][self.pos[1]][self.pos[0]]
        except IndexError: err(red(lc.wrong_pos[lc.lg].format(pos = ip.pos), do_color)); raise
    
    def move(self):
        self.pos = [sum(x) for x in zip(self.pos, self.dir)]
    
    def dev(self, axis):
        n = 2* int(self.pop() > 0) - 1
        self.dir = [n * i for i in axis if bool(self.dir)]
    
    def push(self, n):
        self.stack.append(n)
    
    def push_char(self):
        self.stack.append(ord(self.char))
        self.act = 'i'
    
    def push_hex(self):
        try:
            self.push(eval('0x' + self.char))
        except SyntaxError:
            err(red(lc.wrong_hex[lc.lg].format(hex = ip.char), do_color))
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
        elif self.char == '_': self.dev([1, 0, 0])
        elif self.char == '|': self.dev([0, 1, 0])
        elif self.char == '.': self.dev([0, 0, 1])
        elif self.char == '?': self.push(self.input(dbg(prompt_k, do_color))[0])
        elif self.char == ':': self.push(eval(self.input(dbg(prompt_n, do_color))))
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


########## Initial parameters ##########

args = os.sys.argv
nl_char = os.linesep

x_name = args.pop(0)
opts, args = gnu_getopt(args, 'vpcbf:l:h', ['verbose', 'prompt', 'no-color', 'backslash', 'file=', 'locale=', 'help'])

path = None
verbose = False
prompt_k = prompt_n = ''
do_color = True

for o,a in opts:
    if o in '--verbose':
        verbose = True
    elif o in '--prompt':
        prompt_k = dbg('~ ', do_color)
        prompt_n = dbg('= ', do_color)
    elif o in '--no-color':
        do_color = False
    elif o in '--backslash':
        nl_char = '\\'
    elif o in '--file':
        path = a
    elif o in '--locale':
        lc.lg = a.lower()
    elif o in '--help':
        err(lc.usage[lc.lg])
        exit()
if path == None and len(args) == 1:
    path = args[0]
else: raise GetoptError


########## Interpreter core ##########

ip = IP()

grid = get_grid(get_string(path), nl_char)

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
