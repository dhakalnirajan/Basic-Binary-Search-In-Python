# Python Program For Recursive Binary Search

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) &nbsp; [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try) &nbsp;

Searching Algorithms are designed to check for an element or retrieve an element from a data structure where it is stored. Based on type of search operation, there are two types of Searching methods, Sequential Search and Interval search.

One example of Sequential Search is Linear Search method. A linear search is the simplest approach employed to search for an element in a data set. It examines each element until it finds a match, starting at the beginning of the data set, until the end. The search is finished and terminated once the target element is located.

One example of Interval Search is Binary Search Method. Binary search is an approach used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to 0.

In Searching Algorithms, there are two ways to implement the methods. One is iterative method and another is recursive method. Both Iteration and Recursion are based on control structure. Iteration uses repetition structure while recursion uses a selection structure. An iterative algorithm uses looping statements such as for loop, while loop or do-loop to repeat same steps while recursive algorithm uses a module(function) till the stopping condition is satisfied.

An iterative algorithm will be faster than recursive algorithm because of overheads like calling functions registering stacks repeatedly. Many times, iterative algorithms are not efficient as they take more space and time.

Recursive algorithms are mostly used to solve complex problems when their application is effective.

#### Algorithm for this Program:

1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
4. Else (x is smaller) recur for the left half.