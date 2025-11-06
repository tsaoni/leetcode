from typing import List
import heapq
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # entries: shop, movie, price
        self.n = n 
        self.entries = [(p, s, m) for s, m, p in entries]
        self.rev = {}
        self.entries.sort()
        self.unrented = defaultdict(list)
        self.rented = []
        for i, (p, s, m) in enumerate(self.entries): 
            self.unrented[m].append(i)
            self.rev[s, m] = i
        

    def search(self, movie: int) -> List[int]:
        # unrented: 5 cheapest shops of the movie
        from itertools import islice

        entries = self.entries
        return [entries[i][1] for i in islice(self.unrented[movie], 5)]
        # return [self.entries[i][1] for i in self.unrented[movie][: 5]]
        
    def _binary_search(self, lst, value): 
        l, r = 0, len(lst) - 1
        while l < r: 
            mid = (l + r) // 2 
            if value <= lst[mid]: 
                r = mid 
            else: 
                l = mid + 1
        if l == len(lst) - 1 and value > lst[-1]: 
            return len(lst) 
        return l 

    def rent(self, shop: int, movie: int) -> None:
        idx = self.rev[shop, movie]
        i = self._binary_search(self.unrented[movie], idx)
        if i < len(self.unrented[movie]) and idx == self.unrented[movie][i]:
            self.unrented[movie].pop(i)
            i = self._binary_search(self.rented, idx)
            # if i < len(self.rented) and idx == self.rented[i]:
            self.rented.insert(i, idx)
       
        
        

    def drop(self, shop: int, movie: int) -> None:
        idx = self.rev[shop, movie] 
        i = self._binary_search(self.rented, idx)
        if i < len(self.rented) and idx == self.rented[i]:
            self.rented.pop(i)
            i = self._binary_search(self.unrented[movie], idx)
            # if i < len(self.unrented[movie]) and idx == self.unrented[movie][i]:
            self.unrented[movie].insert(i, idx)
        
        

    def report(self) -> List[List[int]]:
        # rented: price, shop, movie
        return [[self.entries[i][1], self.entries[i][2]] for i in self.rented[: 5]]
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
    

func = ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
args = [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
ret = []
for f, a in zip(func, args): 
    if f == "MovieRentingSystem": 
        obj = MovieRentingSystem(*a)
        ret.append(None)
        # import pdb 
        # pdb.set_trace()
    elif f == "search": 
        x = obj.search(*a)
        ret.append(x)
    elif f == "rent": 
        obj.rent(*a)
        ret.append(None)
    elif f == "drop": 
        obj.drop(*a)
        ret.append(None)
    elif f == "report": 
        x = obj.report(*a)
        ret.append(x)
    print(f, a)
    print(obj.entries)
    print(obj.rev)
    print(obj.unrented)
    print(obj.rented)
    print()

print(ret)