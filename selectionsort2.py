
A = list((5, 0, 1, 3, 4, 2))
print(A)

for i in range(len(A)-1):
	min_position = i
	for j in range(i+1, (len(A))):
		if(A[min_position]>A[j]):
			min_position = j
	if i <= min_position:
		A[i], A[min_position] = A[min_position], A[i]

	print(i)
	print(A)