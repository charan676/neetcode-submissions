class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n):
            if i == n - 1:
                ans.append(-1)
            else:
                ans.append(max(arr[i + 1:]))
        return ans