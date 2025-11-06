from typing import List
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = defaultdict(list)
        for r, f, c in zip(ratings, foods, cuisines): 
            f = self.encode(f)
            self.foods[c].append((r, f))
        self.map = {}
        for c, lst in self.foods.items(): 
            lst.sort()
            for i in range(len(lst)): 
                r, f = lst[i]
                self.map[f] = (r, c)

    def encode(self, food): 
        s = ""
        for c in food:
            _c = chr(ord('z') - ord(c) + ord('a'))
            s += _c 
        for _ in range(len(s), 10): 
            s += "{"
        return s

    def decode(self, food): 
        s = ""
        for c in food: 
            if c == "{": 
                break 
            _c = chr(ord('z') - ord(c) + ord('a'))
            s += _c 
        return s

    def changeRating(self, food: str, newRating: int) -> None:
        food = self.encode(food)
        r, c = self.map[food] 
        
        def search(newRating, food, c=c, eq=False): 
            l, r = 0, len(self.foods[c]) 
            if eq: 
                r -= 1
            key = (newRating, food) 
            while l < r: 
                mid = (l + r) // 2 
                if self.foods[c][mid] < key:
                    l = mid + 1
                else:
                    r = mid 
              
            return l
        
        idx = search(r, food, eq=True)
        # print([(r, self.decode(f))for r, f in self.foods[c]])
        # import pdb 
        # pdb.set_trace()
        self.foods[c].pop(idx)
        new_idx = search(newRating, food)
        self.foods[c].insert(new_idx, (newRating, food))
        self.map[food] = (newRating, c)
        # print(idx, self.decode(food), self.map[food])
        

    def highestRated(self, cuisine: str) -> str:
        # print(cuisine, [(r, self.decode(f))for r, f in self.foods[cuisine]])
        return self.decode(self.foods[cuisine][-1][1])


func = ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
args = [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]

# Your FoodRatings object will be instantiated and called as such:
ret = []
for f, a in zip(func, args): 
    if f == "FoodRatings": 
        obj = FoodRatings(*a)
        ret.append(None)
    elif f == "highestRated": 
        ret.append(obj.highestRated(*a)) 
    elif f == "changeRating": 
        obj.changeRating(*a)
        ret.append(None)
# print(obj.foods)
print(ret)
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)