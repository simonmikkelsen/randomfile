#!/usr/bin/python

import getopt, os, os.path, sys
import random

class RandomFileFinderTreeWalker:
    def __init__(self):
        self.matched = None 
    def get_matched_directory(self):
        return self.matched
    def find_random_file(self, directories):
        # If we only get a single empty dir, return that.
        if len(directories) == 1 and len(os.listdir(directories[0])) == 0:
            return directories
        next_dir = random.choice(directories)

        if self.matched == None:
            self.matched = next_dir

        if os.path.isfile(next_dir):
            return next_dir
        else:
            choices = [os.path.join(next_dir, dir) for dir in os.listdir(next_dir)]
            return self.find_random_file(choices)


if __name__ == "__main__":

    def print_help():
        print """Usage: randomfile.py [-h] [dir ...]
Prints the full path of a random file in one of the directories given as arguments.
    -h --help      Print this message and exit.
    -e --relative  Print the path relative to the dir argument it came from.    
    """

    verbose = 0
    relative = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hve",
                                   ["help", "verbose"])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(2)
    for switch, value in opts:
        if switch in ("-h", "--help"):
            print_help()
            sys.exit(0)
        elif switch in ("-v", "--verbose"):
            verbose += 1
        elif switch in ("-e", "--relative"):
            relative = True

    if len(args) == 0:
        search_dirs = ['./'] 
    else:
        search_dirs = args


    try:
        rand = RandomFileFinderTreeWalker()
        path = os.path.normpath(rand.find_random_file(search_dirs))
        if relative:
            matched_dir = os.path.normpath(rand.get_matched_directory())
            path = path[len(matched_dir) + 1:]
        
        print path
        
    except KeyboardInterrupt:
        print "You cancelled."
        sys.exit(1)
