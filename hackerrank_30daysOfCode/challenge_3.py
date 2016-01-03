#!/bin/python

import sys


N = int(raw_input().strip())

if N % 2 is not 0: 
    print "Weird"
if N % 2 is 0 and N in range(2,5):
	print "Not Weird"
if N % 2 is 0 and N in range(6,20):
	print "Weird"
if N % 2 is 0 and N > 20:
	print "Not Weird"