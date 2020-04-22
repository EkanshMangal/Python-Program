# Function to merge X[0..m] and Y[0..n] to X[0..m+n+1]
def merge(X,Y,m,n):
     # size of X[] is (k + 1)
    k=m+n+1
    # run till X[] or Y[] has elements left
    while m>=0 and n>=0:
    # put next greater element in next free position in X[] from end
		
        if X[m]>Y[n]:
            X[k] = X[m]
            k = k - 1
            m = m - 1
        else:

            X[k] = Y[n]
            k = k - 1
            n = n - 1
    # copy remaining elements of Y[] (if any) to X[]
    while n>=0:
        X[k] = Y[n]
        k = k - 1
        n = n - 1
    for i in range(0,n):
        Y[i]=0
# The function moves non-empty elements in X[] in the
# beginning and then merge it with Y[]
def rearrange(X,Y,m,n):
    # moves non-empty elements of X[] in the beginning
	k=0
	for i in range(0,m):
	    if X[i]!=0:
	        X[k] = X[i]
	        k = k + 1
    # merge X[0..k-1] and Y[0..n-1] to X[0..m-1]
	merge(X,Y,k-1,n-1)
if __name__ == "__main__":
    # vacant cells in X[] is represented by 0
	X=[0,2,0,3,0,5,6,0,0]
	Y=[1,8,9,10,15]
	m=len(X)
	n=len(Y)
	# validate input before calling rearrange()
	# 1. Both arrays X[] and Y[] should be sorted (ignore 0's in X[])
	# 2. size of array X[] >= size of array Y[] (i.e. m >= n)
	#. Number of vacant cells in array X[] = size of array Y[]

	# merge Y[] in X[]
	rearrange(X,Y,m,n)
	for i in range(m):
	    print(X[i],end=" ")


    