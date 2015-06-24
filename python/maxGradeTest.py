#!/usr/bin/env python

import sys
import csv


def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    try:
        fileIN = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename"
        usage()
        sys.exit(1)
    info = csv.reader(fileIN, delimiter=',', quotechar='"')
    valori_maxime = []
    student_max = {
        'test_name': '',
        'highschool': '',
        'student_name': '',
        'student_grade': -1
        }
    for idx, row in enumerate(info):
        student = {
            'test_name': row[0],
            'highschool': row[1],
            'student_name': row[2],
            'student_grade': int(row[3])
            }
        if student['test_name'] != student_max['test_name']:
            if idx != 0:
                valori_maxime.append(student_max)
            student_max = student
        elif student['student_grade'] > student_max['student_grade']:
            student_max = student
    for s in valori_maxime:
        print "Test:%s\nNotaMaxima:%s\n" % (s['test_name'], s['student_grade'])
if __name__ == "__main__":
    sys.exit(main())
