class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose= defaultdict(int)
        win= defaultdict(int)

        for winner, loser in matches:
            lose[loser] +=1
            win[winner] +=1
        
        losers=[]
        winners=[]
        for i in lose:
            if lose[i]==1:
                losers.append(i)
        for i in win:
            if i not in lose:
                winners.append(i)
        winners.sort()
        losers.sort()
            
        return [winners, losers]




        