

from collections import defaultdict

def solution(A, B):
    def test(A):
        # Implement your solution here
        A = list(set(A))
        A.sort()
        # ret = 1 
        # print(A)
        for i, x in enumerate(A): 
            # if x <= 0: 
            #     return ret 
            if i + 1 != x: 
                return i + 1
        return len(A) + 1
    # Implement your solution here
    C = []
    for n1, n2 in zip(A, B): 
        C += [max(n1, n2)]
    return test(C)


def solution1(A): 
    A.sort()
    diff = defaultdict(set)
    for i in range(len(A) - 1): 
        for j in range(i + 1, len(A)): 
            diff[A[j] - A[i]] |= set([A[i], A[j]])
    
    # print(diff)
    lst = []
    for k, v in diff.items(): 
        if k == 0: 
            v = list(v)[0]
            lst += [sum([v == x for x in A])]
        else: 
            lst += [len(v)]

    return max(lst)

def test(A):
    # Implement your solution here
    A = list(set(A))
    A.sort()
    # ret = 1 
    # print(A)
    for i, x in enumerate(A): 
        # if x <= 0: 
        #     return ret 
        if i + 1 != x: 
            return i + 1
    return len(A) + 1

if __name__ == "__main__":
    # A = [1, 2, 4, 3]
    # B = [1, 3, 2, 3]
    # A = [3, 2, 1, 6, 5]
    # B = [4, 2, 1, 3, 3]
    A = [1, 2]
    B = [1, 2]
    tmp = solution(A, B)
    print(tmp)