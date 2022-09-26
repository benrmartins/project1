import math
import stdio
import sys

# this receives the input and declares it into a variable
lat = float(sys.argv[1])
log = float(sys.argv[2])

# uses the equations to find the rectangular coordinates
x = log
y = math.log((1 + math.sin(math.radians(lat)))/(1 - math.sin(math.radians(lat))))/2

x = str(x)
y = str(y)

# displays the output to the terminal
stdio.writeln(x + " " + y)
