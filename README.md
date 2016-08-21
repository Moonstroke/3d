# 3d
## Version 1.1
`3d`, as its name suggests, is a 3-dimensionnal-array-based esolang.  
It is based upon the same principle as *Befunge* or *><>*, but extrapolates the concept to bring the third dimension of space into consideration. (yayy!)

The interpreter can either use on-the-fly input (pipes is a WIP) or be given a file as argument.
The interpreter isentirely written in the `3d.py` file. Any `??.py` file is for language support; for now, only *English*, *French* and *Italian* are supported.  
The `scripts` folder contains scripts I already made. They work just fine, hopefully.

### Terminal options
Several options are available for use within a terminal:  
  `-v`, `--verbose`          print debugging information during execution  
  `-f FILE`, `--file=FILE`   use FILE as file to execute  
  `-c`, `--no-color`          displays info in the default terminal color  
  `-h`, `--help`             print this message and exit  


Feel free to download the files and send feedback for errors handling — if any — and improvements.

In order to correctly read the file, it must be structured as following:  
  > Each (X,Y) plan is separated from the next by *two newlines*: `'\n\n'`.  
  > Plans have the same numbers of rows.  
  > Rows have the same number of characters (yet).  
  > Rows are separated by a *single newline*: `'\n'`.  
  > Uninterpreted section (comments) can be added, at the end of the file, and must begin with a `~`.  

### Commands
Movement:  
  `^` move North  
  `v` move South  
  `<` move West  
  `>` move East  
  `x` move Down  
  `o` move Up  
Deviators (test clauses): (Top of stack: `=0`)  
  `|` N/S  
  `—` W/E (Unicode `0x2104`)  
  `⋅` D/U (Unicode `0x22C5`)  
Input/Output:  
  `?` input and push Unicode ordinal (prompt is `'~ '`)  
  `:` input and push as integer (multichar input allowed, prompt is `'= '`)  
  `!` pop and print as Unicode char  
  `=` pop and print as integer
  `,` pop silently (discard)   
Operators (pop 2 numbers and push back result):  
  `+` sum  
  `-` difference (supports negative numbers)  
  `×` product (Unicode `0xD7`)  
  `∕` quotient (Unicode `0x2215`)  
  `%` remainder  
  `*` power (might change in a future version)  
Stack operations:  
  `.` push 1  (unit)
  `&` duplicate top of the stack  
  `$` invert top two items on the stack  
  `@` pop and push random integer lower or equal to it  
  `#` push next character as hexadecimal digit  
  `'` push next character as char  
  ` pop and execute it as a command character  
Other:  
  ` ` (`SPACE`) NO-OP (technically every character that is not a command is a NOP)  
  `;` end of program  
