class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiouAEIOU"

        count = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            # Remove the character leaving the window
            if s[i - k] in vowels:
                count -= 1

            # Add the character entering the window
            if s[i] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count