#!/usr/bin/python
"""
go2.py v 0.2.0 Daniel Tate

Wraps around the mlocate util and gives you a shell in the working directory of a result.
Do whatever you want with the code.

 v 0.0.1 - Initial Version
 v 0.2.0 - change subprocess.check_output method to compatible subprocess.Popen method
 Quick and dirty code.  No sanity checks at this point.

 Usage:  type go2.py [target], i.e. go2.py bashrc.
"""


import subprocess
import os.path
import sys
def go2( tofind ):
        # Variable Initalization
        x = 0
        targets = [] #targets list is to provide numbers to destination paths

        tofind = sys.argv[1]

        dirs = subprocess.Popen(["locate",tofind],stdout=subprocess.PIPE)
        dirs2, stderr = dirs.communicate()

        print "Files matching the pattern " + tofind +  "were found in:"
        for directory in dirs2.split("\n"):

                # Eliminate the null value at the end of the mlocate output
                if not directory: continue
                print x,os.path.dirname(directory)
                targets.insert(x,os.path.dirname(directory))
                x += 1

        print "\n"
        sel = raw_input("Choose a directory:")
        selection=int(sel)
        command_string = "bash -c 'cd " + targets[selection] + " ;bash'"
        print "Starting new shell in " + targets[selection]

        os.system(command_string)
        return 1

if len(sys.argv) <= 1:
        print "No Arguments Passed"
else:
        go2(sys.argv[1])
