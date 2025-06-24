# Boyer-Moore Algorithm

class BM:
    def __init__(self, text : str):
        self.text = text

    def _compute_last_occurrence_table(self, pattern: str) -> dict[str, int]:
        last_occurrence = {}
        for i, char in enumerate(pattern):
            last_occurrence[char] = i
        return last_occurrence

    def search(self, pattern: str) -> int:
        last_occurrence = self._compute_last_occurrence_table(pattern)
        n, m = len(self.text), len(pattern)
        if m == 0:
            return -1

        shift = 0
        while shift <= n - m:
            j = m - 1

            while j >= 0 and pattern[j] == self.text[shift + j]:
                j -= 1

            if j < 0:
                return shift

            char_shift = last_occurrence.get(self.text[shift + j], -1)
            shift += max(1, j - char_shift)

        return -1
