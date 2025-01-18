from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length(lista): 
    p = lista
    length = 0
    while p is not None: 
        p = p.next
        length += 1
    return length

def get_middle_idx(acc_list_lens):
    mid = int(acc_list_lens[-1] / 2)
    abs_fn = lambda x: x if x > 0 else -x
    dist_list = [abs_fn(l - mid) for l in acc_list_lens]
    min_dist = min(dist_list)
    min_idx = dist_list.index(min_dist)
    return min_idx + 1

def merge_list(lista, listb): 
    pa, pb = lista, listb
    cur = None
    if lista is None: return listb 
    if listb is None: return lista
    # ret = pa if pa.val < pb.val else pb
    start = 1
    while pa is not None and pb is not None: 
        if pa.val > pb.val: 
            if cur: 
                cur.next = pb 
                cur = cur.next 
            else: 
                cur = pb 
            pb = pb.next
        else: 
            if cur: 
                cur.next = pa
                cur = cur.next 
            else: 
                cur = pa
            pa = pa.next
        if start: 
            ret = cur 
            start = 0
    if pa is not None: 
        cur.next = pa 
    if pb is not None: 
        cur.next = pb
    return ret

def merge_recur(lists, acc_list_lens): 
    # final condition
    if len(lists) == 0: return None 
    if len(lists) == 1: return lists[0]
    # find pivot 
    min_idx = get_middle_idx(acc_list_lens)
    # sort
    left = merge_recur(lists[: min_idx], acc_list_lens[: min_idx])
    right = merge_recur(lists[min_idx:], acc_list_lens[min_idx:])
    ret = merge_list(left, right)
    # debug(ret)
    return ret

def debug(ret): 
    cur = ret 
    pstr = ""
    while cur: 
        pstr += f" {cur.val}"
        cur = cur.next 
    print(pstr.strip())

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ret = None 
        # bulid list lengths
        acc_list_lens = [] 
        acc_len = 0
        for l in lists:
            acc_len += get_length(l)
            acc_list_lens += [acc_len]
        # recursive
        ret = merge_recur(lists, acc_list_lens)
        
        return ret


if __name__ == "__main__": 
    def build_test_case(inputs): 
        ret = []
        for l in inputs: 
            cur = None 
            for i, item in enumerate(l):
                tmp = ListNode(val=item, next=None)
                if cur: 
                    cur.next = tmp 
                    cur = cur.next 
                else: cur = tmp
                if i == 0: start = cur
            ret += [start]
        return ret 
    inputs = [[1,4,5],[1,3,4],[2,6]]
    test_case = build_test_case(inputs)
    ret = Solution().mergeKLists(test_case)