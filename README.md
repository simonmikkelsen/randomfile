# randomfile
Finds a random file very quickly.

Usage:
   python randomfile.py [dir 1] [dir 2] ...

Finds a random file in the file system.
When no arguments are given, the current directory is searched.

The dir is found by picking one of the given directories randomly.
Inside that, one of the files or directories are picked randomly.
If it is a file, it is returned.
If it is a directory, a random item is picked from that one.
If an empty directory is hit, it is returned.

This algorithm is very fast and will more often return files
higher up in the directory hirachy, as well as files in 
directories with a few files. This is some times what is
desiered, but not always.

