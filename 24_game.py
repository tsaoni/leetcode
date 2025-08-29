from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        from copy import deepcopy
        options = []
        def swap(idx1, idx2, lst): 
            if idx1 != idx2:
                lst[idx1] ^= lst[idx2]
                lst[idx2] ^= lst[idx1]
                lst[idx1] ^= lst[idx2]

        def perm(lst, idx): 
            if idx == 3: 
                # print(lst)
                options.append(deepcopy(lst))
            else:
                for n_idx in range(idx, 4): 
                    swap(idx, n_idx, lst)
                    perm(lst, idx + 1)
                    swap(idx, n_idx, lst)
            
        perm(cards, 0)
        
        ops = [None, "+", "-", "*", "/"]
        def expr(e1, e2, op): 
            if op == "+": 
                return e1 + e2 
            elif op == "-": 
                return e1 - e2 
            elif op == "*": 
                return e1 * e2 
            elif op == "/": 
                if e2 == 0: 
                    return None
                return e1 / e2 
        def eval(ptr, cards):
            nonlocal stack
            if ptr == 4: 
                val = stack[0]
                print(stack)
                for i in range(2, len(stack), 2): 
                    val = expr(val, stack[i], stack[i - 1])
                # print(val)
                return val == 24
            for op in ops: 
                if op is None: 
                    # if ptr < 3:
                    for _op in ops[1:]: 
                        stack.append(_op)
                        stack.append(cards[ptr])
                        if eval(ptr + 1, cards): 
                            return True 
                        stack = stack[: -2]
                else: 
                    tmp = stack.pop(-1)
                    # print(stack, "hi")
                    res = expr(tmp, cards[ptr], op)
                    stack.append(res)
                    
                    if eval(ptr + 1, cards): 
                        return True
                    # stack.pop(-1)
            return False
        
        
        orders = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        def eval2(ptr, cards): 
            nonlocal stack
            if ptr == 4: 
                for order in orders: 
                    _stack = []
                    o_idx = 0
                    for e in stack: 
                        if e in ops:
                            _stack.append((e, order[o_idx]))
                            o_idx += 1 
                        else: 
                            _stack.append(e)
                    p = 1
                    # print(_stack)
                    while len(_stack) > 1: 
                        for i in range(1, len(_stack), 2): 
                            if _stack[i][1] == p: 
                                num = expr(_stack[i - 1], _stack[i + 1], _stack[i][0])
                                if num is None: 
                                    return False
                                for _ in range(3):
                                    _stack.pop(i - 1)
                                _stack.insert(i - 1, num)
                                break
                        p += 1
                    if abs(_stack[0] - 24) < 1e-5: 
                        return True
                # print(_stack[0])
                return False
            else:     
                for op in ops[1:]:
                    stack.append(op)
                    stack.append(cards[ptr])
                    if eval2(ptr + 1, cards): 
                        return True
                    stack = stack[: -2]
            
        for cards in options:
            # print(cards)
            stack = [cards[0]]
            if eval2(1, cards): 
                return True
        return False
    
if __name__ == "__main__": 
    cards = [4,1,8,7]
    cards = [1,2,1,2]
    cards = [1,7,4,5]
    cards = [1,8,2,5]
    # cards = [3,3,8,8]
    # cards = [3,9,7,7]
    # cards = [1,9,1,2]
    ret = Solution().judgePoint24(cards)
    print(ret)