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


import math
def findMinDifference(arr,n,x,y):
    x_index=n
    y_index=n
    min_diff=math.inf
    for i in range(n):
        if arr[i]==x:
            x_index=i
            if y_index!=n:
                min_diff=min(min_diff,abs(x_index-y_index))
        if arr[i]==y:
            y_index=i
            if x_index!=n:
                min_diff=min(min_diff,abs(x_index-y_index))

    return min_diff

if __name__=="__main__":
    arr=[1,3,5,4,8,2,4,3,6,5]
    x=2
    y=5
    n=len(arr)
    diff=findMinDifference(arr,n,x,y)
    if diff!=math.inf:
        print(f"Minimum difference is {diff}")
    else:
        print("Invalid Input")
