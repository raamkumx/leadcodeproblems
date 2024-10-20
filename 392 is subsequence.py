# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

s = "asdf"
t = "ahbgdc"
i, j = 0, 0

while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1
    if i == len(s):
        print("True")
        break
else:
    print("False")

