import stdio
import sys

# this receives the input and declares it into a variable
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# uses the equations to find the day
y0 = y - (14 - m)/12
x0 = (y0 + y0/4 - y0/100 + y0/400)
m0 = m + 12 * int(((14-m)/12)) - 2
dow = (d + x0 + 31 * (m0/12)) % 7

# displays the output to the terminal
stdio.writeln(str(int(dow)))
