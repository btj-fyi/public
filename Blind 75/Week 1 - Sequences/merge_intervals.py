"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]


def mergeIntervals(intervals: list[list]) -> list[list]:
    merge_intervals = []
    count = 0
    for i in range(len(intervals) - 1):  # pylint: disable=C0200
        starti = intervals[i][0]
        endi = intervals[i][1]
        startj = intervals[i + 1][0]
        endj = intervals[i + 1][1]
        if startj <= endi:
            print(f"{endi},{startj} is overlap")
            merge_intervals.append([starti, endj])
            count += 2
        elif count < len(intervals):
            print("not overlap")
            merge_intervals.append([starti, endi])
            merge_intervals.append([startj, endj])
            count += 1
    return merge_intervals


print(mergeIntervals(intervals))
