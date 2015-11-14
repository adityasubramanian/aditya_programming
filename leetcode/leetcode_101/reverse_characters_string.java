public void reverse(char [] str) {
	int i = 0; 
	int j = str.length - 1; 

	while (i < j) {
		char temp = str[i]; 
		str[i] = str[j]; 
		i++; 
		str[j] = str[temp];
		j--; 
	}
}
