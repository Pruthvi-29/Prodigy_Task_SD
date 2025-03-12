def print_grid(grid):
    """Print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) for num in row))

def find_empty_location(grid):
    """Find an empty location in the grid (represented by 0)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  
    return None

def is_safe(grid, row, col, num):
    """Check if it's safe to place a number in the given row and column."""
    
    for j in range(9):
        if grid[row][j] == num:
            return False

   
    for i in range(9):
        if grid[i][col] == num:
            return False

    
    box_row_start = row - row % 3
    box_col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + box_row_start][j + box_col_start] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True  

    row, col = empty_location

    for num in range(1, 10):  
        if is_safe(grid, row, col, num):
            grid[row][col] = num  

            if solve_sudoku(grid):
                return True  

            grid[row][col] = 0 

    return False  
def main():
   
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Grid:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()