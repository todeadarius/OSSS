#!usr/bin/env python

import sys


def usage():
    print >> sys.stderr,  "Usage: python %s <filename>" % (sys.argv[0])


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename"
        usage()
        sys.exit(1)

    notaMin = 20
    notaMax = 0
    for idx, line in enumerate(list(fp)):
        nota = int(line.split('\t')[3])
        if nota < notaMin:
            notaMin = nota
        if nota > notaMax:
            notaMax = nota

    print "Nota minima este: %d" % (notaMin)
    print "Nota maxima este: %d" % (notaMax)

if __name__ == "__main__":
    sys.exit(main())
