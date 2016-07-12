# 3d
## Version 0.1
3d is a 3-dimensionnal-array-based esolang.
It is based upon the same principle as *Befunge* or *><>*, but extrapolates the concept to bring the third dimension of space into consideration. (yayy!)

The interpreter can either use on-the-fly input (pipes is a WIP) or be given a file as argument.

In order to correctly read the file, it must be structured as following:  
  Each (X,Y) plan is separated from the next by *two newlines*.
  Plans must have the same numbers of rows.
  Rows must have the same number of elements (for now).
  Each element is an ASCII character. (non-ASCII characters might bring errors, if not escaped!)

The commands are:  
Movement:  
   `^` move North  
   `v` move South  
   `<` move West  
   `>` move East  
   `x` move Down  
   `o` move Up  

Deviators: (Top of stack: =0 / >0)  
  `|` N/S  
  `_` W/E  
  `.` D/U  

Input/Output:  
  `?` input and push (prompt is `~ `)  
  `!` pop and print  
  `,` pop silently  

Operators:  
  `+` sum  
  `-` difference (pushes 0 if result < 0)
  `*` product  
  `/` quotient  
  `%` remainder  
  ` power  

Other:  
  ` ` NOP  
  `$` invert top two items on the stack  
  `#` psuhes random integer in range [0-top] on the stack  
  `\` pushes next character on the grid as hexadecimal digit  
  `'` pushes next character on the grid as char  
  `"` executes top of the stack as a character  
  `&` duplicate top of the stack  
  `;` end of program  
  `q` just prints "q" (little *quine*)
