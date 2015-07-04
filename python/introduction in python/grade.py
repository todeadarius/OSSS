#!/usr/bin/env python

import sys
import csv
with open('stats.csv', 'r') as csvfile:
    info = csv.reader(csvfile, delimiter = ',', quotechar = '"')
    valori_maxime = []
    student_max = {
        'test_name' : "wow",
    	'highschool' : '',
    	'student_name' : '',
    	'student_grade' : -1
   		}
    for idx, row in enumerate(info):
        student = {
    	    'test_name' : row[0],
    	    'highschool' : row[1],
    	    'student_name' : row[2],
    	    'student_grade' : int(row[3])
   			}
        if student['test_name'] != student_max['test_name']:
            if idx != 0:
   		        valori_maxime.append(student_max)
            student_max = student
        elif student['student_grade'] > student_max['student_grade']:
   		    student_max = student
    for s in valori_maxime:
        print "Test: %s\nNota-maxima: %s\n" % (s['test_name'], s['student_grade'])
   		   
   		
   	
        
