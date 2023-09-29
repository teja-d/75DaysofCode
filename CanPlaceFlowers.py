class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerlist = []
        if len(flowerbed)==1 and flowerbed[0]==0:
            flowerlist.append(0)
        if len(flowerbed)>1 and (flowerbed[0]==flowerbed[1]==0):
            flowerlist.append(0)
        prev = flowerbed[0]
        i=1
        while i<len(flowerbed)-1:
            if prev==flowerbed[i]==flowerbed[i+1]==0 and (i-1 not in flowerlist):
                flowerlist.append(i)
            prev = flowerbed[i]
            i+=1
        if len(flowerbed)>1 and (flowerbed[-1]==flowerbed[-2]==0) and (len(flowerbed)-2 not in flowerlist):
            flowerlist.append(len(flowerbed)-1)
        print(flowerlist)
        if len(flowerlist) >= n:
            return True
        return False
