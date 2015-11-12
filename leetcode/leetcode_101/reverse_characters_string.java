public void reverse(char [] str) {
	int i = 0; 
	int j = str.length - 1; 

	while (i < j) {
		swap(str, i,j); 
		i++; 
		j--; 
	}
}
public void swap(char[] str, i, j) {
	char temp = str[i]; 
	str[i] = str[j]; 
	str[j] = str[temp]; 
}