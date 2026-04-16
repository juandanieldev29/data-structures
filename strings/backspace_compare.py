class Solution(object):
#     def backspaceCompare(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         return self.process_string(s) == self.process_string(t)
    
#     def process_string(self, word):
#         letters = []
#         for char in word:
#             if char == '#':
#                 letters.pop()
#             else:
#                 letters.append(char)
#         return "".join(letters)


    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p1 = len(s) - 1
        p2 = len(t) - 1

        while p1 >= 0 or p2 >= 0:
            if p1 < 0 and p2 >= 0 and t[p2] != "#":
                return False
            if p2 < 0 and p1 >= 0 and s[p1] != "#":
                return False
            if s[p1] == "#" or t[p2] == "#":
                if s[p1] == "#":
                    backcount = 2
                    while backcount > 0 and p1 >= 0:
                        p1 -= 1
                        backcount -= 1
                        if s[p1] == "#":
                            backcount += 2
                if t[p2] == "#":
                    backcount = 2
                    while backcount > 0 and p2 >= 0:
                        p2 -= 1
                        backcount -= 1
                        if t[p2] == "#":
                            backcount += 2
            else:
                if s[p1] != t[p2]:
                    return False
                p1 -= 1
                p2 -= 1
        return True


solution = Solution()
print(solution.backspaceCompare("hd#dp#czsp#####", "hd#dp#czsp######"))
