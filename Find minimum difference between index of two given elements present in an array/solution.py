# Find minimum difference between index of two given elements present in an array
#
# Given two integers, find minimum difference between their index in a given array in linear time and single traversal of the array.
#
#
#
#
# For example,
#
# Input:
# arr = { 1, 3, 5, 4, 8, 2, 4, 3, 6, 5 }
# x = 3, y = 2
#
# Output: Minimum difference between index is 2
#
#
# Input:
# arr = { 1, 3, 5, 4, 8, 2, 4, 3, 6, 5 }
# x = 2, y = 5
#
# Output: Minimum difference between index is 3
#
#
# The idea is to traverse the array and keep track of last occurrence of x and y.
#
# If element x is encountered, we find the absolute difference between current index of x and index of last occurrence of y and update the result if required.
#
#
# If element y is encountered, we find the absolute difference between current index of y and index of last occurrence of x and update the result if required.



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
