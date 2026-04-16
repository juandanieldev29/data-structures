class Solution(object):

    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     longest = 0
    #     for x in range(len(s)):
    #         max_substring = 1
    #         prev = {s[x]}
    #         for y in range(x + 1, len(s)):
    #             if s[y] not in prev:
    #                 max_substring += 1
    #                 prev.add(s[y])
    #             else:
    #                 break
    #         longest = max(longest, max_substring)
    #     return longest

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        left = 0
        right = 0
        seen = {}
        while left < len(s) and right < len(s):
            current = s[right]
            position = seen.get(current, left)
            if current not in seen or position < left:
                seen[current] = right
                longest = max(longest, right + 1 - left)
            else:
                left = seen[current] + 1
                seen[current] = right
            right += 1
        return longest
        

solution = Solution()
# result = solution.lengthOfLongestSubstring("abcabcbb")
# print(result)
# result = solution.lengthOfLongestSubstring(" ")
# print(result)
# result = solution.lengthOfLongestSubstring("abba")
# print(result)
result = solution.lengthOfLongestSubstring("tmmzuxt")
print(result)
