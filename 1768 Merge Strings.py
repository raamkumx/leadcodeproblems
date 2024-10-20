# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
# word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
#
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"

word1 = "abc"
word2 = "pqr"

min_len = min(len(word1), len(word2))
s = []
for i in range(min_len):
    s.append(word1[i])
    s.append(word2[i])

s.append(word1[min_len:])
s.append(word2[min_len:])

print("".join(s))

