class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]
        if query_row == 0: 
            return 1. if poured > 0 else 0.
        for i in range(100): 
            nxt = [0.] * (i + 2)
            for j in range(i + 1): 
                flow = max(prev[j] - 1, 0) / 2
                nxt[j] += flow
                nxt[j + 1] += flow
            if query_row == (i + 1): 
                return nxt[query_glass] if nxt[query_glass] < 1. else 1. 
            prev = nxt 
        return 0. 

if __name__ == "__main__": 
    poured = 1
    query_row = 1
    query_glass = 1

    # poured = 2
    # query_row = 1
    # query_glass = 1

    poured = 100000009
    query_row = 33
    query_glass = 17
    ret = Solution().champagneTower(poured, query_row, query_glass)
    print(ret)