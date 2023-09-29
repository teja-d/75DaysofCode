class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip().split(' ')
        l = [i for i in l[::-1] if i!='']
        f = " ".join(l)
        return f

        