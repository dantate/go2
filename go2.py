#!/usr/bin/python
#go2.py v 0.0.1 Daniel Tate

#Wraps around the mlocate util and gives you a shell in the working directory of a result.
#Do whatever you want with the code.

# v 0.0.1 
# Quick and dirty code.  No sanity checks at this point.

# Usage:  type go2.py [target], i.e. go2.py bashrc.  Invoke exactly the same as locate.

import subprocess
import os
import sys 

dirs = subprocess.check_output(["locate",sys.argv[1]])
dirs_array = dirs.split("\n")

x = 0
targets = []
dirs_array.pop()
for x,directory in enumerate(dirs_array):

        print x,directory
        targets.insert(x,os.path.dirname(directory))

        
sel = raw_input("Choose:")
selection=int(sel)
command_string = "bash -c 'cd " + targets[selection] + " ;bash'"
print "Starting new shell in " + targets[selection]

os.system(command_string)
