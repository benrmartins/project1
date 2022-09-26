import stdio
import stdrandom
import sys

# this receives the input and declares it into a variable
n = int(sys.argv[1])

# roles the die and add the result together
die = stdrandom.uniformInt(1, n+1) + stdrandom.uniformInt(1, n+1)

# displays the output to the terminal
stdio.writeln(str(die))
