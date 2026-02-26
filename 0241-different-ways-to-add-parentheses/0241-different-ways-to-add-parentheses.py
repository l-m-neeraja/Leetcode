class Solution:
    def diffWaysToCompute(self, e: str) -> List[int]:
        ans = []
        for i in range(len(e)):
            if e[i]=='+' or e[i]=='-' or e[i]=='*':
                left = self.diffWaysToCompute(e[0:i])
                right = self.diffWaysToCompute(e[i+1:])
                sign = e[i]
                for l in left:
                    for r in right:
                        l,r = int(l),int(r)
                        if sign=='+':
                            ans.append(l+r)
                        elif sign=='-':
                            ans.append(l-r)
                        else:
                            ans.append(l*r)
        if not ans:
            ans.append(int(e))
        return ans