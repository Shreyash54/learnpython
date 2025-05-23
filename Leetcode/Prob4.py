''' Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

code:'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest_palindrome = ""
        
        for i in range(len(s)):
            # Odd-length palindrome (expand around one character)
            palindrome1 = expand_around_center(s, i, i)
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            
            # Even-length palindrome (expand around two characters)
            palindrome2 = expand_around_center(s, i, i + 1)
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2
        
        return longest_palindrome
