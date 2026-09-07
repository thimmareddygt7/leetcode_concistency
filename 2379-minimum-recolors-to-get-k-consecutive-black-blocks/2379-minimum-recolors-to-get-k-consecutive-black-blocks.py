class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        countb = blocks[:k].count("B")
        minimum = k - countb

        for i in range(k, len(blocks)):

            if blocks[i-k] == "B":
                countb -= 1

            if blocks[i] == "B":
                countb += 1

            recolors = k - countb
            minimum = min(minimum, recolors)

        return minimum