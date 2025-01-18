from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        cur = head 
        while cur: 
            nodes += [cur] 
            cur = cur.next
        n_rev = int(len(nodes) / k) * k
        def get_index(idx): 
            if idx % k == 0:
                return idx + 2 * k - 1  
            # elif idx % k == k - 1:
            #     return idx + 1
            else: 
                return idx - 1
        ptrs = [get_index(idx) for idx in range(n_rev)] + [idx + 1 for idx in range(n_rev, len(nodes))]

        for i, node in enumerate(nodes): 
            if ptrs[i] > len(nodes) - 1: 
                if i == len(nodes) - 1:
                    tmp = None 
                else:
                    if len(nodes) % k == 0: 
                        tmp = None
                    else:
                        tmp = nodes[n_rev] 
            # if ptrs[i] == len(nodes): tmp = None 
            else: tmp = nodes[ptrs[i]]
            node.next = tmp
        if len(nodes) % k == 0: 
            nodes[-k].next = None 
        else: nodes[-1].next = None
        head = nodes[min(k - 1, len(nodes) - 1)]
        # ori_idx if ori_idx % k == 0 ptr = ori_idx + 1 else ori_idx - 1
        return head
    
if __name__ == "__main__": 
    def debug(nodes): 
        import time
        pstr = ""
        cur = nodes 
        while cur: 
            pstr += f" {cur.val}"
            cur = cur.next
            print(pstr)
            time.sleep(1)

    def build_test_case(inputs): 
        cur = None
        for i, x in enumerate(inputs): 
            tmp = ListNode(val=x, next=None)
            if cur == None: cur = tmp 
            else:
                cur.next = tmp 
                cur = tmp
            if i == 0: head = tmp
        return head
    
    inputs = [1,2,3,]
    test_case = build_test_case(inputs)
    ret = Solution().reverseKGroup(test_case, 3)
    debug(ret)