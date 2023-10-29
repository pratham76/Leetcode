class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
      
        score = [[0]*8 for _ in range(2)]
        
        for p, (i, j) in enumerate(moves):
            p %= 2
            score[p][i] += 1
            score[p][3+j] += 1
            if i == j: score[p][6] += 1
            if i+j == 2: score[p][7] += 1
            if any(x == 3 for x in score[p]): return "AB"[p]
            
        return "Pending" if len(moves) < 9 else "Draw"