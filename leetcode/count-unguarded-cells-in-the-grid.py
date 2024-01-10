class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = []
        for i in range(m):
            grid += [['0']*n]

        for i in walls:
            grid[i[0]][i[1]] = 'W'

        for i in guards:
            grid[i[0]][i[1]] = 'G'

        # go through each part and mark the cells

        count = len(guards) + len(walls)
        for i in guards:
            row, col = i

            # to the up
            start = row - 1
            while start >= 0 and grid[start][col] != 'W' and grid[start][col] != 'G':
                if grid[start][col] == '0':
                    grid[start][col] = 'M'
                    count += 1
                start -= 1
                


            # to the bottom
            start = row + 1
            while start < m and grid[start][col] != 'W' and grid[start][col] != 'G':
                if grid[start][col] == '0':
                    grid[start][col] = 'M'
                    count += 1
                start += 1

            # to the left
            start = col - 1
            while start >= 0 and grid[row][start] != 'W' and grid[row][start] != 'G':
                if grid[i[0]][start] == '0':
                    grid[i[0]][start] = 'M'
                    count += 1                
                start -= 1


            # to the right
            start = col + 1
            while start < n and grid[row][start] != 'W' and grid[row][start] != 'G':
                if grid[i[0]][start] == '0':
                    grid[i[0]][start] = 'M'
                    count += 1  
                start += 1

        return m*n - count