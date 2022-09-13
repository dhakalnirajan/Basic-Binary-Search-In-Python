# Python Program For Recursive Binary Search

# Searching Algorithms are designed to check for an element or retrieve an element from a data structure where it is stored. Based on type of search operation, there are two types of Searching methods, Sequential Search and Interval search.

# One example of Sequential Search is Linear Search method. A linear search is the simplest approach employed to search for an element in a data set. It examines each element until it finds a match, starting at the beginning of the data set, until the end. The search is finished and terminated once the target element is located.

# One example of Interval Search is Binary Search Method. Binary search is an approach used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to 0.

# In Searching Algorithms, there are two ways to implement the methods. One is iterative method and another is recursive method. Both Iteration and Recursion are based on control structure. Iteration uses repetition structure while recursion uses a selection structure. An iterative algorithm uses looping statements such as for loop, while loop or do-loop to repeat same steps while recursive algorithm uses a module(function) till the stopping condition is satisfied.

# An iterative algorithm will be faster than recursive algorithm because of overheads like calling functions registering stacks repeatedly. Many times, iterative algorithms are not efficient as they take more space and time.

# Recursive algorithms are mostly used to solve complex problems when their application is effective.

# Algorithm for this Program:

# 1. Compare x with the middle element.
# 2. If x matches with the middle element, we return the mid index.
# 3. Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
# 4. Else (x is smaller) recur for the left half.


# CODE BEGINS
# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    
    # Check the base
    if r>= 1:
        mid = 1 + (r-1) // 2
        
        # If the element is present in the middle:
        if arr[mid] == x:
            return mid
        # If the element is smaller than the mid, it is in the left subarray.
        elif arr[mid] < x:
            return binarySearch(arr, 1, mid+1, x)
        # else, the element is greater than mid, it is on the right subarray.
        else:
            return binarySearch(arr, mid-1, r, x)
    else:
        # element is not present in the array:
        return -1

# Code for drive
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# Asking the user to input the value.
x = int(input())

# Calling the Function.
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at the index % d" % result)
else:
    print("Element is not present in the array.")