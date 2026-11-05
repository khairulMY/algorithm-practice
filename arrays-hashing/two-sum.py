"""
Problem: Two Sum
Source: LeetCode #1
Difficulty: Easy
Pattern: Hash map

Approach:
  Store each number's index as I scan. For each number, check whether
  (target - number) is already stored.

Time: O(n)
Space: O(n)

testing with diiferent array;
if same number is present in the array, it will return the first index of that number and the index of the current number.
if have another set after it will return the first index of that number and the index of the current number. 

"""


def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []


if __name__ == "__main__":
    print(two_sum([5,2,8,5,5], 10))   # expected: [1, 2]