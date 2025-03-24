from typing import List
from collections import defaultdict
from copy import deepcopy
import math

import string

class Spreadsheet:

    def __init__(self, rows: int):
        self.table = {}
        for c in string.ascii_uppercase: 
            self.table[c] = [0] * rows 
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        r, col = cell[0], int(cell[1:]) - 1
        self.table[r][col] = value

    def resetCell(self, cell: str) -> None:
        r, col = cell[0], int(cell[1:]) - 1
        self.table[r][col] = 0

    def getValue(self, formula: str) -> int:
        num1, num2 = formula[1:].split("+")
        vals = []
        for n in [num1, num2]: 
            if n[0] in string.ascii_uppercase: 
                r, col = n[0], int(n[1:]) - 1
                vals += [self.table[r][col]] 
            else: 
                vals += [int(n)]
        return sum(vals)

# Your Spreadsheet object will be instantiated and called as such:

# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

# exit(-1)

class SegmentTree: 
    def __init__(self, arr): 
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end): 
        if start == end: 
            self.tree[node] = arr[start]
        else: 
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])


    def set(self, index, value, node=0, start=0, end=None): 
        if end is None: 
            end = self.n - 1 
        if start == end: 
            self.tree[node] = value 
        else: 
            mid = (start + end) // 2 
            if index <= mid: 
                self.set(index, value, 2 * node + 1, start, mid)
            else: 
                self.set(index, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def get_max(self, L, R, node=0, start=0, end=None): 
        if end is None: 
            end = self.n - 1 
        if R < start or L > end: 
            return float("-inf")
        if L <= start and R >= end: 
            return self.tree[node]
        mid = (start + end) // 2 
        val = max(self.get_max(L, R, 2 * node + 1, start, mid), 
                  self.get_max(L, R, 2 * node + 2, mid + 1, end))
        return val

class Solution: 
    def func(): 
        return 
    
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = defaultdict(int)
        for d in digits: 
            cnt[d] += 1 

        ret = 0
        for num, c in cnt.items(): 
            if num % 2 == 0: 
                tmp = deepcopy(cnt)
                tmp[num] -= 1 
                for num1, c1 in tmp.items(): 
                    if num1 > 0 and c1 > 0: 
                        tmp[num1] -= 1 
                        for num2, c2 in tmp.items(): 
                            if c2 > 0: 
                                ret += 1 
                        tmp[num1] += 1
        
        return ret

    def longestCommonPrefix2(self, words: List[str], k: int) -> List[int]:
        N = max([len(w) for w in words])
        cnt, ncnt = {"": 0}, {}
        # match = ["" for _ in words]
        # k_idxs = [i for i in range(len(words))]
        k_len, prev_k_len = 0, 0
        for i in range(N): 
            # pfx_d = defaultdict(list)
            # num_k = 0
            # for idx in k_idxs: 
            #     w = words[idx]
            #     if i < len(w): 
            #         pfx_d[w[: i + 1]] += [idx]
            #     if len(pfx_d[w[: i + 1]]) == k: 
            #         num_k += 1 
            
            for w in words: 
                if i < len(w): 
                    if w[: i] in cnt: 
                        if w[: i + 1] in ncnt: 
                            ncnt[w[: i + 1]] += 1
                        else: 
                            ncnt[w[: i + 1]] = 1
    
            k_num, k_larger_num = 0, 0
            for s, c in ncnt.items(): 
                if c > k: 
                    # cnt[s] = c 
                    k_larger_num += 1
                elif c == k: 
                    # cnt[s] = c 
                    k_num += 1 
    
            
            if k_num + k_larger_num == 0: 
                break 

            cnt = {}
            for s, c in ncnt.items(): 
                if c >= k: 
                    cnt[s] = c 
            ncnt = {}
            if k_num > 1 or k_larger_num > 0: 
                prev_k_len = i + 1

            k_len = i + 1

        ret = []
        if "" in cnt: 
            return [0] * len(words)
        else:
            for w in words: 
                if w[: k_len] in cnt: 
                    c = cnt[w[: k_len]]
                    if c == k: 
                        ret += [prev_k_len]
                    else: 
                        ret += [k_len]
                else: 
                    ret += [k_len]
        return ret

    def longestCommonPrefix1(self, words: List[str], k: int) -> List[int]:
        """
        """
        def find_max_prefix(words, k):
            # print(words)
            def good(num): 
                cnt, ncnt = {"": 0}, {}
                for i in range(num): 
                    for w in words: 
                        if i < len(w): 
                            if w[: i] in cnt: 
                                if w[: i + 1] in ncnt: 
                                    ncnt[w[: i + 1]] += 1
                                else: 
                                    ncnt[w[: i + 1]] = 1
                    cnt = {}
                    for s, c in ncnt.items(): 
                        if c >= k: 
                            cnt[s] = c 
                    ncnt = {}
                # print(num)
                # print(cnt)
                return cnt
            
            word_len = [len(w) for w in words]
            max_word_len = max(word_len)
            left, right = 0, max_word_len
            rcnt = {}
            while True: 
                mid = math.ceil((left + right) / 2)
                if left == mid: 
                    break
                cnt = good(mid)
                if len(cnt) > 0: 
                    rcnt = cnt
                    left = mid
                else: 
                    right = mid - 1
            return left, rcnt
        
        if len(words) == 1: 
            return [0]
        
        valk, cntk = find_max_prefix(words, k)
        # valk1, cntk1 = find_max_prefix(words, k + 1)
        # print(valk)
        # print(cntk)
        # print(valk1)
        # print(cntk1)
        ret = []
        for i, w in enumerate(words): 
            s = w[: valk]
            if s in cntk:
                if cntk[s] > k: 
                    ret += [valk] 
                else: 
                    if len(cntk) > 1: 
                        ret += [valk] 
                    else:
                        val, _ = find_max_prefix(words[: i] + words[i + 1: ], k)
                        ret += [val]
            else: 
                ret += [valk]
        # for i in range(len(words)): 
        #     val = find_max_prefix(words[: i] + words[i + 1: ])
        #     ret += [val]
        return ret

    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        """
        results in TLE
        """
        def find_max_prefix(i_words):
            # print(i_words)
            def good(num): 
                cnt, ncnt = {"": 0}, {}
                for i in range(num): 
                    for w in i_words: 
                        if i < len(w): 
                            if w[: i] in cnt: 
                                if w[: i + 1] in ncnt: 
                                    ncnt[w[: i + 1]] += 1
                                else: 
                                    ncnt[w[: i + 1]] = 1
                    cnt = {}
                    for s, c in ncnt.items(): 
                        if c >= k: 
                            cnt[s] = c 
                    ncnt = {}
                # print(num)
                # print(cnt)
                return len(cnt) > 0
            
            word_len = [len(w) for w in i_words]
            max_word_len = max(word_len)
            left, right = 0, max_word_len
            while True: 
                mid = math.ceil((left + right) / 2)
                if left == mid: 
                    break
                if good(mid): 
                    left = mid
                else: 
                    right = mid - 1
            return left
        
        if len(words) == 1: 
            return [0]
        ret = []
        for i in range(len(words)): 
            val = find_max_prefix(words[: i] + words[i + 1: ])
            ret += [val]
        return ret

    def longestSpecialPath(
        self,
        edges: list[list[int]],
        nums: list[int]
    ) -> list[int]:
        maxLength = 0
        minNodes = 1
        graph = [[] for _ in range(len(nums))]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        prefix = [0]
        lastSeenDepth = {}

        def dfs(
            u: int,
            prev: int,
            leftBoundary: list[int],
        ) -> None:
            nonlocal maxLength, minNodes
            prevDepth = lastSeenDepth.get(nums[u], 0)
            lastSeenDepth[nums[u]] = len(prefix)

            if prevDepth != 0:
                leftBoundary = sorted(leftBoundary + [prevDepth])[-2:]

            length = prefix[-1] - prefix[leftBoundary[0]]
            nodes = len(prefix) - leftBoundary[0]
            if length > maxLength or (length == maxLength and nodes < minNodes):
                maxLength = length
                minNodes = nodes

            for v, w in graph[u]:
                if v == prev:
                    continue
                prefix.append(prefix[-1] + w)
                dfs(v, u, leftBoundary)
                prefix.pop()

            lastSeenDepth[nums[u]] = prevDepth

        dfs(0, -1, leftBoundary=[0, 0])
        return [maxLength, minNodes]

    def longestSpecialPath2(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        """
        top down approach
        """
        N = len(nums)
        root = 0
        T = [[] for _ in range(N)]
        for v1, v2, c in edges: 
            T[v1] += [[v2, c]]
            T[v2] += [[v1, c]]
        
        stacks = [[root]]
        w_nodes = [[]]
        W = [0]
        N_w = [0] * N
        cnt = [defaultdict(int)]
        cnt2 = [0]
        # W = 0
        ret = [-1, -1]
        while len(stacks) > 0: 
            """current"""
            x = stacks[-1][-1]
            w_nodes[-1] += [x]
            W[-1] += N_w[x]
            cnt[-1][nums[x]] += 1 
            if cnt[-1][nums[x]] == 2: 
                if cnt2[-1] < 1: 
                    cnt2[-1] += 1 
                else: 
                    # adjust window and update return 
                    # clen = W[-1] - N_w[x]
                    # if clen > ret[0]: 
                    #     ret = [clen, len(w_nodes[-1]) - 1]
                    # elif clen == ret[0]: 
                    #     ret[1] = min(ret[1], len(w_nodes[-1]) - 1)
                    
                    while True:
                        tmp = w_nodes[-1].pop(0)
                        tmp = nums[tmp]
                        W[-1] -= N_w[w_nodes[-1][0]]
                        cnt[-1][tmp] -= 1
                        if cnt[-1][tmp] == 1: 
                            cnt2[-1] = 1
                            break 
                        

            elif cnt[-1][nums[x]] > 2: 
                # adjust window and update return 
                # clen = W[-1] - N_w[x]
                # if clen > ret[0]: 
                #     ret = [clen, len(w_nodes[-1]) - 1]
                # elif clen == ret[0]: 
                #     ret[1] = min(ret[1], len(w_nodes[-1]) - 1)
                
                while True: 
                    tmp = w_nodes[-1].pop(0)
                    tmp = nums[tmp]
                    W[-1] -= N_w[w_nodes[-1][0]]
                    cnt[-1][tmp] -= 1
                    if tmp == nums[x]: 
                        cnt[-1][nums[x]] = 2 
                        break
        
            clen = W[-1] 
            if clen > ret[0]: 
                ret = [clen, len(w_nodes[-1])]
            elif clen == ret[0]: 
                ret[1] = min(ret[1], len(w_nodes[-1]))

            # print(W)
            # print(w_nodes)
            # print(cnt)
            # W += N_w[x]
            parent = -1 if len(stacks) == 1 else stacks[-2][-1]
            # print(W)
            # if len(T[x]) == 1: # leaf
            #     if len(stacks[-1]) == 0: 
            #         stacks.pop(-1) 
            # elif len(T[x]) == 2: 

            # else: 
            """prepare for next"""
            new_stack = []
            for nx, w in T[x]: 
                if nx != parent: 
                    N_w[nx] = w
                    new_stack += [nx]
            
            if len(new_stack) == 0: # leaf
                while True: 
                    if len(stacks) == 0: 
                        break
                    if len(stacks[-1]) == 1: 
                        tmp = stacks.pop(-1)[0]
                        
                        # print(stacks)
                        # print(tmp, len(T[tmp]), w_nodes)
                        if len(stacks) > 0:
                            tmpp = stacks[-1][-1]
                            if len(T[tmpp]) > 2: 
                                w_nodes.pop(-1)
                                W.pop(-1)
                                cnt.pop(-1)
                                cnt2.pop(-1)

                        # if len(tmp) > 0: 
                        #     tmp = tmp[0]
                        #     W -= N_w[tmp]
                    else:
                        tmp = stacks[-1].pop(-1)
                        w_nodes[-1] = deepcopy(w_nodes[-2])
                        cnt[-1] = deepcopy(cnt[-2])
                        cnt2[-1] = cnt2[-2]
                        W[-1] = W[-2]
                        
                        
                        # W -= N_w[tmp]
                        break

                # tmp = stacks[-1].pop(-1)
                
                # w_nodes[-1] = deepcopy(w_nodes[-2])
                # cnt[-1] = deepcopy(cnt[-2])
                # cnt2[-1] = deepcopy(cnt2[-1])
                # W[-1] = W[-2]

                # tmp = w_nodes[-1].pop(-1)
                # cnt[-1][nums[tmp]] -= 1
                # if cnt[-1][nums[tmp]] == 1: 
                #     cnt2[-1] -= 1
                # W[-1] -= N_w[tmp]
                
                # W[-1] = W[-2]
                # W -= N_w[tmp]
            else:
                stacks += [new_stack]
                if len(new_stack) > 1: 
                    w_nodes += [deepcopy(w_nodes[-1])]
                    cnt += [deepcopy(cnt[-1])]
                    cnt2 += [cnt2[-1]]
                    W += [W[-1]]

            # if len(stacks[-1]) == 0: 
            #     while True: 
            #         if len(stacks) == 0: 
            #             break
            #         if len(stacks[-1]) < 2: 
            #             tmp = stacks.pop(-1)
            #             # if len(tmp) > 0: 
            #             #     tmp = tmp[0]
            #             #     W -= N_w[tmp]
            #         else:
            #             tmp = stacks[-1].pop(-1)
            #             w_nodes.pop(-1)
            #             W.pop(-1)
            #             cnt.pop(-1)
            #             # W -= N_w[tmp]
            #             break
            
            # print(x)
            # print(stacks)
            # print(w_nodes)



        return ret

    def longestSpecialPath1(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        """
        use segment tree
        """
        N = len(nums)
        M = max(nums)
        INF = 10 ** 20

        e = defaultdict(list)
        for u, v, l in edges: 
            e[u] += [(v, l)]
            e[v] += [(u, l)]

        nums_stack = defaultdict(list)
        longest = 0 
        min_longest = INF
        st = SegmentTree([-1] * (M + 1))
        stack = []
        def go(node, parent, depth, w): 
            stack.append((node, w))
            nums_stack[nums[node]].append(depth)
            
            if len(nums_stack[nums[node]]) >= 2: 
                st.set(nums[node], nums_stack[nums[node]][-2])
            prev_depth = st.get_max(0, M)
            pnode, _ = stack[prev_depth]
            if len(nums_stack[nums[pnode]]) >= 3: 
                st.set(nums[pnode], nums_stack[nums[pnode]][-3])
            else: 
                st.set(nums[pnode], -1)

            best_depth = st.get_max(0, M) + 1 
            bnode, bw = stack[best_depth]
            nonlocal longest 
            nonlocal min_longest 
            L = len(stack) - best_depth 
            W = w - stack[best_depth][1] 
            if W > longest: 
                longest = W 
                min_longest = L 
            elif W == longest: 
                if L < min_longest: 
                    min_longest = L 
            
            if len(nums_stack[nums[pnode]]) >= 2: 
                st.set(nums[pnode], nums_stack[nums[pnode]][-2])
            else: 
                st.set(nums[pnode], -1)

            for v, l in e[node]: 
                if parent != v: 
                    go(v, node, depth + 1, w + l)
            
            nums_stack[nums[node]].pop()
            if len(nums_stack[nums[node]]) >= 2: 
                st.set(nums[node], nums_stack[nums[node]][-2])
            elif len(nums_stack[nums[node]]) == 1: 
                st.set(nums[node], -1)
            stack.pop()
        
        go(0, -1, 0, 0)
        
        return (longest, min_longest)

    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        """
        bottom up approach 
        (TLE)
        """
        N = len(nums)
        root = 0
        T = [[] for _ in range(N)]
        for v1, v2, c in edges: 
            T[v1] += [[v2, c]]
            T[v2] += [[v1, c]]
        
        parents = [-1] * N 
        vals = [0] * N 
        cur = [root]
        while len(cur) > 0: 
            nxt = []
            for x in cur: 
                for n, c in T[x]:
                    if n > 0 and parents[n] < 0: 
                        parents[n] = x 
                        vals[n] = c
                        nxt += [n]
                    
            cur = nxt
        # print(parents)
        # print(vals)
        cands = []
        for i in range(N): 
            if i not in parents: 
                cands += [i]
        
        ret = [-1, -1]
        # print(cands)
        for cand in cands: 
            cnt = {k: 0 for k in nums}
            nqueue = [nums[cand]]
            cnt[nums[cand]] += 1
            lqueue = []
            nerr = 0
            def update(ret, nq, lq):
                tmp = sum(lq)
                if tmp > ret[0]: 
                    ret = [tmp, len(nq)]
                    # print(nq)
                    # print(lq)
                elif tmp == ret[0]: 
                    ret[1] = min(ret[1], len(nq))
                    # print(nq)
                    # print(lq)
                return ret

            while parents[cand] != -1: 
                lqueue += [vals[cand]]
                cand = parents[cand]
                nqueue += [nums[cand]]
                
                
                cnt[nums[cand]] += 1 
                if cnt[nums[cand]] == 2: 
                    nerr += 1 
                    if nerr == 2: 
                        ret = update(ret, nqueue[: -1], lqueue[: -1])
                        
                        while True: 
                            x = nqueue.pop(0)
                            lqueue.pop(0)
                            cnt[x] -= 1 
                            if cnt[x] == 1: 
                                break 
                        nerr = 1
                elif cnt[nums[cand]] > 2: 
                    ret = update(ret, nqueue[: -1], lqueue[: -1])
                    
                    while True: 
                        x = nqueue.pop(0)
                        lqueue.pop(0)
                        cnt[x] -= 1 
                        if cnt[x] == 2: 
                            break 
            ret = update(ret, nqueue, lqueue)  
            # print(lqueue)  
                
        return ret

if __name__ == "__main__": 
    # digits = [1,3,5]
    # test_case = (digits, )
    # ret = Solution().totalNumbers(*test_case)
    # print(ret)

    # words = ["jump","run","run","jump","run"]
    # k = 2
    # words = ["dog","racer","car"]
    # k = 2
    # words = ["fdcc","ccfef","acaa","adfa","afc","fdbda"] 
    # k = 1
    # words = ["efea","ceb","aff","ebb","cffaf","b","faaf","fbe","aed","dacc","ddd","fda"] 
    # k = 1
    # test_case = (words, k)
    # ret = Solution().longestCommonPrefix2(*test_case)
    # print(ret)

    edges = [[0,1,1],[1,2,3],[1,3,1],[2,4,6],[4,7,2],[3,5,2],[3,6,5],[6,8,3]]
    nums = [1,1,0,3,1,2,1,1,0] 
    
    edges = [[1,0,3],[0,2,4],[0,3,5]]
    nums = [1,1,0,2]

    edges = [[1,2,4],[0,1,8],[0,3,6]] 
    nums = [1,3,1,1]

    edges = [[0,2,4],[1,2,10],[3,1,5]] 
    nums = [4,5,4,5] 
    
    edges = [[0,3,7],[3,1,9],[3,2,7]] 
    nums = [2,1,2,2]

    # edges = [[0,3,2],[1,7,10],[7,5,10],[5,6,9],[3,6,2],[3,2,5],[2,4,10],[4,8,5]] 
    # nums = [3,3,1,1,2,1,4,1,2]

    test_case = (edges, nums)
    ret = Solution().longestSpecialPath2(*test_case)
    print(ret)

