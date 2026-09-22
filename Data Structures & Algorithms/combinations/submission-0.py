class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combos = []
        combo = []
        def dfs(number, size):
            if size == k:
                combos.append(combo.copy())
                return
            if number > n:
                return
            # add this number
            combo.append(number)
            dfs(number + 1, size + 1)
            combo.pop()

            # don't add this number 
            dfs(number + 1, size)
        dfs(1, 0)
        return combos
            
