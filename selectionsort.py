A = list((5, 2, 1, 3, 4, 0))
print(A)

for i in range(len(A)-1):
	min_position = A.index(min(A[i:]))
	#print(min_position)
	A[min_position], A[i] = A[i], A[min_position]
print(A)
