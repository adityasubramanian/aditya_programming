# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function 
meal = float(input())
tip = int(input())
tax = int(input())
final = meal +((tip * meal)/100) + ((tax * meal)/100)
print ('The final price of the meal is ${}.'.format(int(round(final,0))))


