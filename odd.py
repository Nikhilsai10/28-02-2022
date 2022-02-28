
def getOddOccurrence(arr, arr_size):
	
	for i in range(0,arr_size):
		count = 0
		for j in range(0, arr_size):
			if arr[i] == arr[j]:
				count+=1
			
		if (count % 2 != 0):
			return arr[i]
		
	return -1
	
	
# driver code
arr = [1,2,3,2,1,3,2,1,2,2 ]
n = len(arr)
print(getOddOccurrence(arr, n))


