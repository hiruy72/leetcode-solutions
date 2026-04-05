class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0  # horizontal position
        y = 0  # vertical position
        
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
                
        # check if robot returned to origin
        return x == 0 and y == 0
        