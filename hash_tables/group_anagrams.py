def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())

# def group_anagrams(words):
#     anagrams = []
#     words_dict = {}
#     for word in words:
#         sorted_word = sorted(word)
#         sorted_word = "".join(sorted_word)
#         if sorted_word in words_dict:
#             words_dict[sorted_word].append(word)
#         else:
#             words_dict[sorted_word] = [word]
#     for value in words_dict.values():
#         anagrams.append(value)
#     return anagrams


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

#print("\n2nd set:")
#print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

#print("\n3rd set:")
#print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""