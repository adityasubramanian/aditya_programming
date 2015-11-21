/**
*Return the new *length* of the new array after removing all duplicates. 
**/ 
public int removeDuplicates(int [] nums) {
	if (nums.length == 0) { return 0; }
	if (nums.length == 1) { return 1; }
	int compare_to = 0; 
	for (int i = 0; i < nums.length; i++) {
		if (nums[compare_to] != nums[i]) {
			compare_to++; 
			nums[compare_to] = nums[i]
		}
	}
	return compare_to+1; 
}
