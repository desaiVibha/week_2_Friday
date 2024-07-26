# Question 3: Write a program that find the minimum and maximum numbers among those elements.
def set_min(A):
    mini = float('inf')  # Initialize mini as positive infinity
    for num in A:
        if num < mini:
            mini = num
    return mini

def set_max(A):
    maxi = float('-inf')  # Initialize maxi as negative infinity
    for num in A:
        if num > maxi:
            maxi = num
    return maxi
A = [3,1,4,6,2,7]
N = len(A)
print("Minimum element is:", set_min(A))
print("Maximum element is:", set_max(A))