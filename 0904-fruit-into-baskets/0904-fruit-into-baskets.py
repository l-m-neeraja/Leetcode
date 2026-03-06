class Solution(object):
    def totalFruit(self, fruits):
        if not fruits: 
            return 0
        b1, b2 = -1, -1
        maxi = 0
        cnt = 0
        streak = 0
        for i in range(len(fruits)):
            if fruits[i] == b1 or fruits[i] == b2:
                cnt += 1
            else:
                cnt = streak + 1
            if i > 0 and fruits[i] == fruits[i-1]:
                streak += 1
            else:
                streak = 1
            if fruits[i] != b2:
                b1 = b2
                b2 = fruits[i]
            maxi = max(maxi, cnt)
        return maxi