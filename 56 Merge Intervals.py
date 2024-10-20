# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
#
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]

intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]

intervals.sort(key=lambda interval: interval[0])
merged=[]

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

print(merged)