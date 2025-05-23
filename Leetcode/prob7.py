'''You are given an integer array pizzas of size n, where pizzas[i] represents the weight of the ith pizza. Every day, you eat exactly 4 pizzas. Due to your incredible metabolism, when you eat pizzas of weights W, X, Y, and Z, where W <= X <= Y <= Z, you gain the weight of only 1 pizza!

On odd-numbered days (1-indexed), you gain a weight of Z.
On even-numbered days, you gain a weight of Y.
Find the maximum total weight you can gain by eating all pizzas optimally.

Note: It is guaranteed that n is a multiple of 4, and each pizza can be eaten only once.

code:'''
import heapq

class Solution:
    def maxWeight(self, pizzas):
        res = 0
        # Create a max-heap by negating the pizza weights
        max_heap = [-num for num in pizzas]
        heapq.heapify(max_heap)  # Convert list to a heap
        
        size = len(pizzas) // 4
        odd = (size + 1) // 2  # Calculate number of odd days
        
        # First, process the odd days: take the heaviest pizza each time
        for _ in range(odd):
            res += -heapq.heappop(max_heap)  # Pop the largest (negated back to positive)
        
        # Then, process the even days: remove one pizza and take the second heaviest
        for _ in range(size - odd):
            heapq.heappop(max_heap)  # Remove one pizza
            res += -heapq.heappop(max_heap)  # Pop the second heaviest (negated back to positive)
        
        return res
