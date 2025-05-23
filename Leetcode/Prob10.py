'''Trapping Rain Water
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

img link: https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9



code:'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n=len(height)
        left = [0] * n  # Initialize the left array
        right = [0] * n  # Initialize the right array
        left[0]=height[0]
        for i in range(1,n):
            left[i]=max(height[i],left[i-1])

        

        right[n-1]=height[n-1]
        for j in range(n-2,-1,-1):
            right[j]=max(right[j+1],height[j])

        water_trapped=0
        for i in range(n):
            water_trapped +=min(right[i],left[i])-height[i]
        return water_trapped


        
