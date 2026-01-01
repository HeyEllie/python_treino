import random
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def falling_numbers(num_columns=40, num_rows=20, fall_speed=0.1):
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    while True:
        clear_console()

        # Introduce new falling numbers at the top
        for _ in range(random.randint(1, 3)): # Randomly add 1-3 new numbers
            col = random.randint(0, num_columns - 1)
            grid[0][col] = str(random.randint(0, 9))

        # Move numbers down
        for r in range(num_rows - 1, 0, -1):
            for c in range(num_columns):
                grid[r][c] = grid[r-1][c]
        
        # Clear the top row after moving
        for c in range(num_columns):
            grid[0][c] = ' '

        # Print the current grid
        for row in grid:
            print(''.join(row))

        time.sleep(fall_speed)

if __name__ == "__main__":
    falling_numbers()