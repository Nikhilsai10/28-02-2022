
def firstNonRepeating(arr, n):

	for i in range(n):
		j = 0
		while(j < n):
			if (i != j and arr[i] == arr[j]):
				break
			j += 1
		if (j == n):
			return arr[i]
	
	return -1
	
# Driver code
arr = [ 1,2,1,3,2,4,2,5,4,6,5,7,6,4 ]
n = len(arr)
print(firstNonRepeating(arr, n))

