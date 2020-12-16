#!/usr/bin/python3

import sys
import re
import os

# Get input filename
inFileName = sys.argv[1]

# Create output filename, append '2' to the name
outFileName = inFileName + '.tmp'

# Read all lines into memory
with open(inFileName, "r") as f:
    lines = f.readlines()

# Process and write modified lines to output file
with open(outFileName, "w") as of:

# Iterate over all lines
    for line in lines:
        if line.startswith('; printing object ', 0): # Line with ; printing object
            startObjectNr = line.index(':') + 1 # Position of id: number
            endObjectNr = line.index('copy', startObjectNr) # Position of the word copy
            line = 'M486 S' + line[startObjectNr:endObjectNr] + line # Add M486
        of.write(line)
of.close()
f.close()
os.remove(inFileName)
os.rename(outFileName, inFileName)
# End of script
