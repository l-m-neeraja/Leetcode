class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h=[]
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                h.append(arr[i]/arr[j])
        h.sort()
        mini=h[k-1]
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i]/arr[j]==mini:
                    return [arr[i],arr[j]]