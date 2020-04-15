A = list((5,2,1,3,4,0))

	
print(A)
for i in range (len(A)-1) :
	for j in range ((len(A)-1), i , -1):
		if(A[j] < A[j-1]):
			A[j],A[j-1] = (A[j-1],A[j])
print(A)


#print(A[2])
#print(A[-2])

