def palindrome(word):
    start_index = 0
    end_index = 0
    for index, _ in enumerate(word):
        left = index
        right = index
        while left >= 0 and right < len(word) and word[left] == word[right]:
            if right - left > end_index - start_index:
                start_index = left
                end_index = right
            left -= 1
            right += 1


        left = index
        right = index + 1
        while left >= 0 and right < len(word) and word[left] == word[right]:
            if right - left > end_index - start_index:
                start_index = left
                end_index = right
            left -= 1
            right += 1

    return word[start_index: end_index + 1]

print(palindrome("madam"))
print(palindrome("noon"))
