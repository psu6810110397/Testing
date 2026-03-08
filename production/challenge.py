def gridChallenge(grid):

    sorted_grid = ["".join(sorted(row)) for row in grid]

    rows = len(sorted_grid)
    if rows == 0:
        return "YES"
    cols = len(sorted_grid[0])

    for col in range(cols):
        for row in range(1, rows):

            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"

    return "YES"


def run_with_input():

    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(input().strip())
    return gridChallenge(grid)
