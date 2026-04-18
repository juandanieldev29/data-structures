class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                result_left = self.is_valid_sub_palindrome(s, left + 1, right)
                result_right = self.is_valid_sub_palindrome(s, left, right - 1)
                if not result_left and not result_right:
                    return False
            left += 1
            right -= 1
        return True

    def is_valid_sub_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
            
    
solution = Solution()
result = solution.validPalindrome('abca')
