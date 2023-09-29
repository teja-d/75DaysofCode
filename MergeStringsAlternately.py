class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_tot = len(word1) if len(word1) < len(word2) else len(word2)
        rem_str = word1[len_tot:] + word2[len_tot:]
        tot_str = "".join([word1[i]+word2[i] for i in range(len_tot)]) + rem_str
        return tot_str