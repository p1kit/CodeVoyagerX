# valid anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        import collections

        seen = collections.defaultdict(int)

        for idx in range(len(s)):
            seen[s[idx]] += 1
            seen[t[idx]] -= 1

        for key in seen:
            if seen[key] != 0:
                return False
        return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
    assert Solution().isAnagram(s, t) == True
