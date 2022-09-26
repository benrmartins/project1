import stdio
import sys

# this receives the input and declares it into a variable
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# uses the equations to find the gravitational force in newtons
G = 6.674 * (10 ** -11)
f = G * (m1 * m2 / r ** 2)

# displays the output to the terminal
stdio.writeln(f)
