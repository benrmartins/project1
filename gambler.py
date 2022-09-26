import stdio
import sys

# this receives the input and declares it into a variable
n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
p = float(sys.argv[3])
q = 1 - p

# uses the equations to find the probabilities
p1 = (1 - (p/q) ** n2) / (1 - (p/q) ** (n1 + n2))
p2 = (1 - (q/p) ** n1) / (1 - (q/p) ** (n1 + n2))

# displays the output to the terminal
stdio.writeln(str(p1) + " " + str(p2))
