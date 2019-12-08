# Python program for implementation of Selection Sort
# https://www.geeksforgeeks.org/selection-sort

# Time Complexity: O(n2) as there are two nested loops.

# Auxiliary Space: O(1)
# The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

# In Place : Yes, it does not require extra space.

import sys
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

	# Find the minimum element in remaining
	# unsorted array
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j

	# Swap the found minimum element with
	# the first element
	A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i]),
