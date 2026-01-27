class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        d={}
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] in d:
                d[arr[i+1]-arr[i]].append([arr[i],arr[i+1]])
            else:
               d[arr[i+1]-arr[i]]=[[arr[i],arr[i+1]]] 
        return d[min(d.keys())]