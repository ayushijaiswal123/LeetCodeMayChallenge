def kadane(a): 
    n = len(a) 
    max_so_far = 0
    max_ending_here = 0
            
    for i in range(0, n): 
        max_ending_here = max_ending_here + a[i] 
        if (max_ending_here < 0): 
            max_ending_here = 0
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
    return max_so_far 

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        all_negative = True
        for num in A:
            if num > 0:
                all_negative = False
        if all_negative:
            return max(A)
        # Using standard Kadane's Algortihm
        max_kadane = kadane(A)
        max_wrap = 0
        for i in range(n):
            max_wrap += A[i]
            A[i] = -A[i]
        
        max_wrap += kadane(A)
        return max(max_wrap, max_kadane)
