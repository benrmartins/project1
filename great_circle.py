import math
import stdio
import sys

# this receives the input and declares it into a variable
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# converts the inputs to radians
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)

# uses the equations to find the distance
d0 = 6359.83
d1 = (math.acos((math.sin(x1) * math.sin(x2)) + (math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))))
d = d0 * d1

stdio.writeln(str(d))
