class Solution:
    def minDeletions(self, s: str) -> int:
        freq_counter = Counter(s)
        freq_set = set()
        deletions = 0

        for char, freq in freq_counter.items():
            while freq in freq_set:
                freq -= 1
                deletions += 1
            if freq > 0:
                freq_set.add(freq)

        return deletions
        