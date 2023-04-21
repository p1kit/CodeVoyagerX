# contains duplicate


class Soltuion:
    def containsDuplicate(self, nums: list[int]) -> bool:
        import collections

        last_seen = collections.defaultdict(int)

        for num in nums:
            if num in last_seen:
                return True
            else:
                last_seen[num] = 1
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Soltuion().containsDuplicate(nums))
    assert Soltuion().containsDuplicate(nums) == True
