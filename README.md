# Qb
## Version 0.1
`Qb` is a 3-dimensionnal-array-based esolang.
It is based upon the same principle as *Befunge* or *><>*, but extrapolates the concept to bring the third dimension of space into consideration. (yayy!)

The interpreter can either use on-the-fly input (pipes is a WIP) or be given a file as argument.

In order to correctly read the file, it must be structured as following:  
  Each (X,Y) plan is separated from the next by *two newlines*: `'\n\n'`.
  Plans have the same numbers of rows.
  Rows have the same number of characters (yet).
  Rows are separated by a *single newline*: `'\n'`

The commands are:  
Movement:  
   `^` move North  
   `v` move South  
   `<` move West  
   `>` move East  
   `x` move Down  
   `o` move Up  

Deviators (test clauses): (Top of stack: `=0` / `>0)  
  `|` N/S  
  `_` W/E  
  `.` D/U  

Input/Output:  
  `?` input and push  
  `!` pop and print  
  `,` pop silently  

Operators (pop 2 numbers and push back result):  
  `+` sum  
  `-` difference (push 0 if result < 0)  
  `*` product  
  `/` quotient  
  `%` remainder  
  ` power  

Stack operations:
  `&` duplicate top of the stack  
  `$` invert top two items on the stack  
  `#` pop and push random integer lower or equal to it  
  `\` push next character as hexadecimal digit  
  `'` push next character as char  
  `"` pop and execute it as a command character

Other:  
  ` ` (`SPACE`) NO-OP (technically every character that is not a command is a NOP)  
  `;` end of program  
