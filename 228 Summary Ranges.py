# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of
# nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not
# in nums.

# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

nums = [0, 1, 2, 4, 5, 7]
start = end = nums[0]
output = []

for i in range(1, len(nums)):
    if nums[i] == end + 1:
        end = nums[i]
    else:
        if start == end:
            output.append(str(end))
        else:
            output.append(str(start) + "->" + str(end))
        start = end = nums[i]

if start == end:
    output.append(str(end))
else:
    output.append(str(start) + "->" + str(end))

print(output)
