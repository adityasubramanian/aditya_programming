# Enter your code here. Read input from STDIN. Print output to STDOUT
def interchange():
	a = int(raw_input())
	b = int(raw_input())
	a,b = b,a
	return a
	return b 
if __name__ =="__main__":
	interchange()