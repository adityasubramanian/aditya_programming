/**
Return the new *length* of the new array after removing all duplicates. 
**/ 
public int removeDuplicates(int [] nums) {
	int i = 0; 				// Declare a point to start iterating through. 
	for (int j = 0; j < nums.length; j++) {		//Reach length of input.  
		if (nums[j] != nums[i]) {				// 
			i++; 
			nums[i] = nums[j]; 
		}
	}
	return i+1; 
}
