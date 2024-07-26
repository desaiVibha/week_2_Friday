
""" Question 1. write a program that takes an array and Find the most frequent element in it. 
if there are multiple element maximum number of times, print any of them """
""" There are 3 ways to solve it. 
1. If we compare each element with every other element and keep the counter of each element's value, 
the time complexity will be O(n2). Because we need to run two for loops. Space complexity will be O(1).
2. We can sort the array first and then do a linear traversal to see the duplicate values and then keep a count of them and then the
maximum value. Here the time complexity will be O(nlog(n)) and space complexity will be O(1).
3. The perfect solution is to create a hash table and store elements and their frequency counts as key-value pairs and finally, 
we traverse the hash table and print the key with the maximum value. Here the time complexity and space complexity will be O(n)."""

import math as mt 
  
def mostFrequent(arr, n):   
    # Insert all elements in Hash. 
    Hash = dict() 
    for i in range(n): 
        if arr[i] in Hash.keys(): 
            Hash[arr[i]] += 1
        else: 
            Hash[arr[i]] = 1  
    # find the max frequency 
    max_count = 0
    res = -1
    for i in Hash:  
        if (max_count < Hash[i]):  
            res = i 
            max_count = Hash[i]           
    return res 
arr =  [1,3,2,1,4,1]
n = len(arr) 
print(mostFrequent(arr, n))  