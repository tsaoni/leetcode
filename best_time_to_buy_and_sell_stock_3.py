from typing import List
import numpy as np

class Solution:
    def maxProfit1(self, prices: List[int]) -> int: 
        sell, buy = [], []
        min_idx = 0
        n_transact = len(prices)
        for i, p in enumerate(prices): 
            if i == 0: 
                min_idx = i 
                sell += [-1]
                buy += [-1]
            elif buy[-1] == -1: 
                if p - prices[min_idx] > 0: 
                    buy += [min_idx]
                    sell += [i]
                else: 
                    buy += [-1] 
                    sell += [-1]
            else: 
                buy_idx, sell_idx = buy[-1], sell[-1]
                if p - prices[min_idx] > prices[sell_idx] - prices[buy_idx]: 
                    buy += [min_idx]
                    sell += [i]
                else: 
                    buy += [buy_idx]
                    sell += [sell_idx]

            if p < prices[min_idx]: 
                min_idx = i
        
        prices_rev = [prices[i] for i in range(n_transact - 1, -1, -1)]
        for i, p in enumerate(prices_rev): 
            p
        print(buy)
        print(sell)
        return 
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        I just forget... 
        """
        # preprocessing 
        i = 1
        # for _ in range(len(prices)): 
        while True:
            if i > 0 and i < len(prices) - 1:
                if prices[i - 1] > prices[i] and prices[i] > prices[i + 1]: 
                    # prices[i] = -1
                    # i += 1
                    tmp = prices[i - 1]
                    start = i - 1
                    while i < len(prices) and prices[i] < tmp: 
                        tmp = prices[i]
                        i += 1
                    end = i - 1 
                    for j in range(start + 1, end): 
                        prices[j] = -1

                elif prices[i - 1] < prices[i] and prices[i] < prices[i + 1]: 
                    # prices[i] = -1
                    # i += 1

                    start = i - 1 
                    tmp = prices[i - 1]
                    r = (i - 1, i)
                    while i < len(prices) and prices[i] > tmp: # check increasing
                        tmp = prices[i]
                        if prices[i] - prices[i - 1] < prices[r[1]] - prices[r[0]]: 
                            r = (i - 1, i)
                        i += 1
                    end = i - 1
                    for j in range(start + 1, end): 
                        if j not in r: 
                            prices[j] = -1    
                
                i += 1
            else: break

        prices = list(filter(lambda x: x >= 0, prices))
        n_prices = len(prices)


        first_trans_range = [None]
        second_trans_range = [None]
        first_buy, first_sell = 0, 0 
        first_min = 0
        second_buy, second_sell = n_prices - 1, n_prices - 1
        second_max = n_prices - 1
        profit = 0
        # easy check
        # min_idxs, max_idxs = [], []
        # for i in range(n_prices):
        #     if len(min_idxs) == 0: 
        #         min_idxs += [i]
        #     elif len(min_idxs) == 1: 
        #         if prices[min_idxs[0]] < prices[i]: 
        #             min_idxs += [i]
        #         else: min_idxs = [i] + min_idxs
        #     elif prices[min_idxs[0]] > prices[i]: 
        #         min_idxs[0] = i
        #     elif prices[min_idxs[0]] < prices[i]: 
        #         if prices[min_idxs[1]] > prices[i]:
        #             min_idxs[1] = i 
            
        #     if len(max_idxs) == 0: 
        #         max_idxs += [i]
        #     elif len(max_idxs) == 1: 
        #         if prices[max_idxs[0]] < prices[i]: 
        #             max_idxs += [i]
        #         else: max_idxs = [i] + max_idxs
        #     elif prices[max_idxs[1]] < prices[i]: 
        #         max_idxs[1] = i
        #     elif prices[max_idxs[1]] > prices[i]: 
        #         if prices[max_idxs[0]] < prices[i]: 
        #             max_idxs[0] = i 
    
        # s_idxs = np.argsort(prices)
        # # store sorted index values
        # min_s_idxs = [0, 1] if s_idxs[0] < s_idxs[1] else [1, 0]
        # max_s_idxs = [n_prices - 1, n_prices - 2] if s_idxs[n_prices - 1] < s_idxs[n_prices - 2] else [n_prices - 2, n_prices - 1]
        # idx = 2
        # def check_fn(s_idxs, min_s_idxs, max_s_idxs): 
        #     valid = True 
        #     valid &= s_idxs[min_s_idxs[0]] < s_idxs[max_s_idxs[0]] 
        #     valid &= s_idxs[min_s_idxs[1]] < s_idxs[max_s_idxs[1]] 
        #     valid &= s_idxs[min_s_idxs[1]] > s_idxs[max_s_idxs[0]] 
        #     return valid
        
        # profit = 0
        # if n_prices == 1: 
        #     profit = 0
        # elif n_prices < 4: 
        #     for end in range(1, n_prices): 
        #         for start in range(end): 
        #             profit = max(profit, prices[end] - prices[start])
        # else:
        #     relu_fn = lambda x: x if x > 0 else 0
        #     while True: 
        #         if check_fn(s_idxs, min_s_idxs, max_s_idxs): 
        #             profit = relu_fn(prices[s_idxs[max_s_idxs[1]]] - prices[s_idxs[min_s_idxs[1]]]) + \
        #                         relu_fn(prices[s_idxs[max_s_idxs[0]]] - prices[s_idxs[min_s_idxs[0]]])
        #             break
        #         else: 
        #             if idx == (n_prices - 1) / 2: 
        #                 import pdb 
        #                 pdb.set_trace()
        #             elif idx < (n_prices - 1) / 2: 
        #                 new_min_idx, new_max_idx = s_idxs[idx], s_idxs[n_prices - 1 - idx]
        #                 import pdb 
        #                 pdb.set_trace()
        #             else: 
        #                 break 
        #             idx += 1
        # return profit

        for i in range(1, n_prices): 
            if prices[i] - prices[first_min] > prices[first_sell] - prices[first_buy]: # change range
                first_buy = first_min 
                first_sell = i
            elif prices[i] > prices[first_sell]: # get larger sell
                first_sell = i 
            elif prices[i] < prices[first_min]: # set potential buy
                first_min = i 
    
            first_trans_range += [(first_buy, first_sell)]

            # if prices[first_sell] - prices[first_buy] > max(prices[i + 1:]): 
            #     first_trans_range += [(first_buy, first_sell)] * (len(prices) - 1 - i)
            #     break
        
        for i in range(1, n_prices): 
            idx = n_prices - 1 - i 
            if prices[second_max] - prices[idx] > prices[second_sell] - prices[second_buy]: # change range
                second_buy = idx 
                second_sell = second_max
            elif prices[idx] < prices[second_buy]: # get smaller buy
                second_buy = idx 
            elif prices[idx] > prices[second_max]: # set potential sell
                second_max = idx 
            second_trans_range = [(second_buy, second_sell)] + second_trans_range 

            # if prices[second_sell] - prices[second_buy] > max(prices[: idx]): 
            #     second_trans_range = [(second_buy, second_sell)] * idx + second_trans_range
            #     break
            
            # if n_prices > 3: 
            #     if i == n_prices - 1: 
            #         second_start, second_end = second_trans_range[0]
            #         val = prices[second_end] -  prices[second_start]
            #         profit = max(profit, val)

            #         first_start, first_end = first_trans_range[n_prices - 1]
            #         val = prices[first_end] - prices[first_start] 
            #         profit = max(profit, val)
            #     elif i == n_prices - 2: 
            #         idx = n_prices - 1 - i
            #         first_start, first_end = first_trans_range[idx]
            #         second_start, second_end = second_trans_range[-n_prices + 1 + idx]
            #         val = prices[first_end] - prices[first_start] + prices[second_end] -  prices[second_start]
            #         profit = max(profit, val)
            #     elif i == (n_prices - 1) / 2:
            #         first_start, first_end = first_trans_range[i]
            #         second_start, second_end = second_trans_range[-i]
            #         val = prices[first_end] - prices[first_start] + prices[second_end] -  prices[second_start]
            #         profit = max(profit, val)
            #     elif i > int((n_prices - 1) / 2): 
            #         first_start, first_end = first_trans_range[i]
            #         second_start, second_end = second_trans_range[-n_prices + 1 + i]
            #         val = prices[first_end] - prices[first_start] + prices[second_end] -  prices[second_start]
            #         profit = max(profit, val)

            #         idx = n_prices - 1 - i
            #         first_start, first_end = first_trans_range[idx]
            #         second_start, second_end = second_trans_range[-n_prices + 1 + idx]
            #         val = prices[first_end] - prices[first_start] + prices[second_end] -  prices[second_start]
            #         profit = max(profit, val)


        # print(first_trans_range)
        # print(second_trans_range)
        if n_prices == 1: 
            profit = 0
        elif n_prices < 4: 
            profit = 0
            start, end = first_trans_range[-1]
            val = prices[end] - prices[start]
            profit = max(profit, val)
        else:
            profit = 0
            for i in range(0, len(prices) - 1): 
                if i == 0: 
                    second_start, second_end = second_trans_range[i]
                    val = prices[second_end] -  prices[second_start]
                    profit = max(profit, val)
                elif i == len(prices) - 2: 
                    first_start, first_end = first_trans_range[len(prices) - 1]
                    val = prices[first_end] - prices[first_start] 
                    profit = max(profit, val)
                else:
                    first_start, first_end = first_trans_range[i]
                    second_start, second_end = second_trans_range[i + 1]
                    val = prices[first_end] - prices[first_start] + prices[second_end] -  prices[second_start]
                    profit = max(profit, val)
        return profit
    
if __name__ == "__main__": 
    import time 
    start = time.time()
    prices = [3,3,5,0,0,3,1,4]
    test_case = (prices, )
    ret = Solution().maxProfit1(*test_case)
    print(ret)