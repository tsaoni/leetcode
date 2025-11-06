class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        modulo = 10 ** 9 + 7
        n_people = [[1, 0]] + [[0, 0] for _ in range(n - 1)] 
        if delay < n:
            n_people[delay][1] += 1 
        if forget < n:
            n_people[forget] = [-1, -1] 
        for t in range(1, n):
            n_know, n_share = n_people[t - 1]
            n_people[t] = [(n_know + n_people[t][0]) % modulo, (n_share + n_people[t][1]) % modulo]
            if True: #n_people[t][1] > 0: 
                # if t == 2: 
                #     import pdb 
                #     pdb.set_trace()
                n_share = n_people[t][1]
                n_people[t][0] = (n_people[t][0] + n_share) % modulo
                if t + delay < n: 
                    n_people[t + delay][1] = (n_people[t + delay][1] + n_share) % modulo
                if t + forget < n: 
                    n_people[t + forget][0] = (n_people[t + forget][0] - n_share + modulo) % modulo
                    n_people[t + forget][1] = (n_people[t + forget][1] - n_share + modulo) % modulo

            # print(t, n_people)
        return n_people[-1][0]
    
if __name__ == "__main__": 
    n = 6
    delay = 2
    forget = 4
    # n = 4
    # delay = 1
    # forget = 3
    ret = Solution().peopleAwareOfSecret(n, delay, forget)
    print(ret)