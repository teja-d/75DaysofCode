class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        vws = [i for i in s if i.lower() in vowels]
        vws.reverse()
        flag = 0
        cnt = 0
        f = ''
        while True:
            if len(s) <= flag:
                break
            if s[flag].lower() in vowels:
                f += vws[cnt]
                cnt+=1
            else:
                f += s[flag]
            flag += 1
        return f