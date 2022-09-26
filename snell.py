import math
import stdio
import sys

# this receives the input and declares it into a variable
O1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# equation to find 02 in degrees
O1 = math.radians(O1)
μ = math.asin(n1 / n2 * math.sin(O1))
μ = str(math.degrees(μ))

# displays the output to the terminal
stdio.writeln(μ)
