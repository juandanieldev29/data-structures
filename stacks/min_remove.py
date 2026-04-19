class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = ""
        s_array = list(s)
        for index, value in enumerate(s):
            if value == "(":
                stack.append(index)
            elif value == ")":
                if not stack:
                    s_array[index] = None
                else:
                    stack.pop()
        while stack:
            remaining_item = stack.pop()
            s_array[remaining_item] = None
        for item in s_array:
            if item:
                result += item
        return result

solution = Solution()
# result = solution.minRemoveToMakeValid("lee(t(c)o)de)")
# result = solution.minRemoveToMakeValid("a)b(c)d")
# result = solution.minRemoveToMakeValid("))((")
result = solution.minRemoveToMakeValid("())()(((")
# result = solution.minRemoveToMakeValid("v((((((())")
# result = solution.minRemoveToMakeValid(")((c)d()(l")
# result = solution.minRemoveToMakeValid("())fwk)))())(())))())()()((())")
# result = solution.minRemoveToMakeValid("(a(b(c)d)")
# result = solution.minRemoveToMakeValid("h((((((b)")
# result = solution.minRemoveToMakeValid("abc")
# result = solution.minRemoveToMakeValid(")i()()((fm(((()")
print(result)

# (

# s = "lee(t(c)o)de)"
# c = ")"
# result = "lee("
# stack = ["t", "(", "c"]