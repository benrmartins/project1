import math

import stdio
import sys

# this receives the input and declares it into a variable
t = float(sys.argv[1])
v = float(sys.argv[2])

# uses the equations to find the wind speed
w = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * (v ** 0.16)

# displays the output to the terminal
stdio.writeln(w)
