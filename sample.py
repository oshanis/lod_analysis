import sys

with file(sys.argv[1], 'r') as f: 
    i = 0
    for line in f:
        if i % 1000 == 0:
            print line[:-1]
        i += 1