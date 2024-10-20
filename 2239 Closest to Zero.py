# 2239 Find Closest Number to Zero
# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers,  return the number with the largest value.

# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1

# Example 2:

# Input: nums = [2,-1,1]
# Output: 1

nums = [2,4,-2,1]

closest = nums[0]
for num in nums[1:]:
    if abs(num) < abs(closest):
        closest = num
if closest < 0 and abs(closest) in nums:
    closest = abs(closest)

print(closest)
