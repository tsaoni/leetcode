from typing import List
from collections import defaultdict

class Solution:
    def findAllRecipes1(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ing_inv = defaultdict(list) 
        for i, lst in enumerate(ingredients): 
            for x in lst: 
                ing_inv[x] += [i]

        r_acc = [0] * len(recipes)   
        ret = []    
        # print(ing_inv)
        while len(supplies) > 0: 
            avail = set()
            for x in supplies:
                if x in ing_inv:
                    for idx in ing_inv[x]:
                        r_acc[idx] += 1
                        # print(r_acc[idx], recipes[idx])
                        if r_acc[idx] == len(ingredients[idx]): 
                            avail |= {idx}
    
            supplies = []
            for x in avail: 
                ret += [recipes[x]]
                supplies += [recipes[x]]
        return ret

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        TLE
        """
        N = len(recipes)
        ret = []
        for i in range(N): 
            tmp = [x for x in ingredients[i]]
            add = True
            while len(tmp) > 0: 
                ing = tmp.pop(0)
                if ing not in supplies:
                    if ing in recipes: 
                        idx = recipes.index(ing)
                        tmp += ingredients[idx]
                    else: 
                        add = False 
                        break 
            if add:
                ret += [recipes[i]]
        return ret
    
if __name__ == "__main__": 
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]

    # recipes = ["bread","sandwich"]
    # ingredients = [["yeast","flour"],["bread","meat"]]
    # supplies = ["yeast","flour","meat"]
    
    # recipes = ["bread","sandwich","burger"]
    # ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    # supplies = ["yeast","flour","meat"]
    test_case = (recipes, ingredients, supplies)
    ret = Solution().findAllRecipes1(*test_case)
    print(ret)