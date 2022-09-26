import math
import stdio
import sys

# this receives the input and declares it into a variable
λ = float(sys.argv[1])
t = float(sys.argv[2])

# uses the equations to find the probability
p = math.exp(-λ * t)

# displays the output to the terminal
stdio.writeln(str(p))
