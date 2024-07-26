# Question 2: Write a program to print sum of even and odd elements in an array
# Time Complexity: O(n)
# Space complexity: 0(1)
def EvenOddSum(a, n):
    even = 0
    odd = 0
    result=[0,0]
    for i in range(n): 
        # Loop to find even, odd Sum
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]     
    print ("Even index positions sum ", even)
    print ("Odd index positions sum ", odd)
    result[0]=odd
    result[1]=even
    print(result)
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr) 
EvenOddSum(arr, n)