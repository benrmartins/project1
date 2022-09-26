import stdio
import sys

# this receives the input and declares it into a variable
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# organize the variables in order
z0 = max(x, y, z)
x0 = min(x, y, z)
y0 = x+y+z-x0-z0

# displays the output to the terminal
stdio.writeln(str(x0) + " " + str(y0) + " " + str(z0))
