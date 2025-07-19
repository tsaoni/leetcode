from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort() 
        pi, ti = 0, 0 
        n_match = 0
        while pi < len(players) and ti < len(trainers): 
            if players[pi] <= trainers[ti]: 
                n_match += 1 
                pi += 1
            ti += 1 
        return n_match
        