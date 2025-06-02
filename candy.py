from typing import List 

class Solution:
    def candy(self, ratings: List[int]) -> int:
        stack = [0]
        acc = 0
        minc = 0
        for i in range(1, len(ratings) + 1): 
            if i < len(ratings) and ratings[stack[-1]] > ratings[i]: 
                stack.append(i)
            else: 
                idx = stack[0]
                if ratings[idx] > ratings[idx - 1]: 
                    # tmp = minc + 1 
                    minc += 1
                else: 
                    minc = 1
                    # tmp = minc - 1
                tv = max(minc, len(stack)) 
                acc += tv + len(stack) * (len(stack) - 1) // 2
                #(2 * tv - len(stack) + 1) * len(stack) // 2
                # minc = tv - len(stack) + 1
                if len(stack) > 1: 
                    minc = 1
                stack = [i]
            # print(i, acc, stack)
                
                
        return acc 

if __name__ == "__main__": 
    ratings = [1,0,2]
    ratings = [1,2,2]
    ratings = [1,2,87,87,87,2,1]
    ratings = [29,51,87,87,72,12]
    # ratings = [1,3,4,5,2]
    # ratings = [0,1,2,5,3,2,7]
    ret = Solution().candy(ratings)
    print(ret)