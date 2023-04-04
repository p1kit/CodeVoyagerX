"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Intuition: We create a dictionary that maps each letter to its position in the order.
        Then we compare each word with the next one. If the first letter of the first word is
        before the first letter of the second word, we continue to the next word. If the first
        letter of the first word is after the first letter of the second word, we return False.
        If the first letter of the first word is the same as the first letter of the second word,
        we compare the second letter of the first word with the second letter of the second word.
        If the second letter of the first word is before the second letter of the second word,
        we continue to the next word. If the second letter of the first word is after the second
        letter of the second word, we return False. If the second letter of the first word is
        the same as the second letter of the second word, we compare the third letter of the
        first word with the third letter of the second word. And so on. If we reach the end of
        the first word, we continue to the next word. If we reach the end of the second word,
        we return False.

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Parameters
        ----------
        words: List[str]
        order: str

        Returns
        -------
        bool - True if the words are sorted lexicographically in the alien language, False otherwise

        """
        dict = {}
        for i in range(len(order)):
            dict[order[i]] = i
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if dict[words[i][j]] < dict[words[i + 1][j]]:
                    break
                elif dict[words[i][j]] > dict[words[i + 1][j]]:
                    return False
        return True

if __name__ == "__main__":
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    solution = Solution()
    print(solution.isAlienSorted(words, order))
    assert solution.isAlienSorted(words, order) == True
