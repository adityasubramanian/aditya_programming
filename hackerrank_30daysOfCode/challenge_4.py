class Person:    
 		def __init__(self,initial_Age):
              # Add some more code to run some checks on initial_Age
        def amIOld(self):
            # Do some computations in here and print out the correct statement to the console 
        def yearPasses(self):
            # Increment the age of the person in here

T = int(raw_input())
for i in range(0,T):
    age = int(raw_input())
    p = Person(age)
    p.amIold()
    for j in range(0,3): 
        p.yearPasses(); 
    p.amIOld(); 
    print ""