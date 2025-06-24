from util.coloring import coloring_string_at_index_to_index

class KMP:
    def __init__(self, text : str):
        self.text = text

    def _compute_prefix_table(self, pattern : str) -> list[int]:
        m = len(pattern)
        prefix_table = [0] * m
        j = 0  # length of previous longest prefix suffix

        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix_table[j - 1]

            if pattern[i] == pattern[j]:
                j += 1
                prefix_table[i] = j
            else:
                prefix_table[i] = 0

        return prefix_table

    def search(self, pattern : str) -> int:
        n = len(self.text)
        m = len(pattern)
        j = 0

        prefix_table = self._compute_prefix_table(pattern)

        for i in range(n):
            while j > 0 and self.text[i] != pattern[j]:
                j = prefix_table[j - 1]

            if self.text[i] == pattern[j]:
                j += 1

            if j == m:
                # print(coloring_string_at_index_to_index(self.text, i - m + 1, i + 1))
                return i - m + 1

        return -1