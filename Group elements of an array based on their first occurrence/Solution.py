"""
Group elements of an array based on their first occurrence

Given an unsorted array of integers containing many duplicates elements, rearrange the given array such that same element appears together and relative order of first occurrence of each element remains unchanged.




For example,

Input:  { 1, 2, 3, 1, 2, 1 }

Output: { 1, 1, 1, 2, 2, 3 }


Input:  { 5, 4, 5, 5, 3, 1, 2, 2, 4 }

Output: { 5, 5, 5, 4, 4, 3, 1, 2, 2 }


The idea is to use hashing to solve this problem. We store frequency of each element present in the input array in a map. Then we traverse the input array and for each element A[i], two cases are possible –

If A[i] exists in the map, then this is first occurrence of A[i] in input array. We print element A[i] k times where k is the frequency of A[i] in the input array (stored in map). Finally we delete A[i] from the map so it would not get processed again.

If A[i] is not present in the map, then this is repeated occurrence of A[i], and move to the next element.

"""
def rearrange(A,n):
    freq={}
    for i in range(n):
        freq[A[i]]=0
    for i in range(n):
        freq[A[i]]=freq[A[i]]+1

    for i in range(n):
        if A[i] in freq:
            n=freq[A[i]]
            while(n):
                print(A[i],end=" ")
                n=n-1
            del freq[A[i]]
A=[5,4,5,5,3,1,2,2,4]
n=len(A)
rearrange(A,n)
