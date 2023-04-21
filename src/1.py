from typing import List


class Solution:
    def sem(self, nums: List[int], target: int) -> List[int]:
        import collections

        sum = collections.defaultdict(int)

        for idx in range(len(nums)):
            if (target - nums[idx]) in sum:
                return [sum[target - nums[idx]], idx]
            sum[nums[idx]] = idx
        return [-1, -1]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().sem(nums, target))
    assert Solution().sem(nums, target) == [0, 1]
