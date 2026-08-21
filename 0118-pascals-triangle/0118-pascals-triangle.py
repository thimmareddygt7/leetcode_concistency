class Solution:
    def generate(self, numRows):
        result = [[1]]

        for _ in range(numRows - 1):
            previous = result[-1]
            current = [1]

            for i in range(len(previous) - 1):
                current.append(previous[i] + previous[i + 1])

            current.append(1)
            result.append(current)

        return result