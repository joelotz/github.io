Title: N-Queens Puzzle, Part 2.5-Brute Force Algorithm (All Solutions)
Date: 2020-07-10
Tags: Python
Author: Joe
Keywords: ubuntu 20.4, n queens, n-queens, brute-force search, alogrithms, python 3
Version: OS, Ubuntu 20.04 LTS, python, 3.7.4

This article is Part 2.5 in a series implementing different algorithms to solve the N-Queens problem. I named it 2.5 because it is an extension of [Part 2](n-queens-puzzle-part-2-brute-force-algorithm.html) where I implemented the Brute Force Search Algorithm. In that algorithm I stopped evaluating the candidates once a solution was found. While it involves much more computation, in this implementation I continue to evaluate the candidates to provide *all* solutions. 

See the first article ["Part 1-Introduction"](n-queens-puzzle-part-1-introduction.html) for an overview of the puzzle and some background information.

### Solution Set

For a given number of queens there can be many solutions that satisfy the problem. Not surprisingly, as the size of the board (NxN) and number of queens (N) increases so does the number of solutions. Here is a table from [Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle#Counting_solutions) that show number of fundamental solutions per number of queens. 

![NQueens_Solution_Table](/mnt/DataDrive/Blog/content/images/2020/NQueens_2-01.png)

### Code

As in Part2 I used an optimized Python library called `itertools` to calculate the combinations and permutations. 

```python
#### IMPORTS
import itertools

#### FUNCTIONS ####

def create_empty_board(N):
    "Create an NxN board of zeros"
    return [[0]*N for _ in range(N)] 

def perm_to_board(perm):
    "Makes a board from a given permutation"
    board = create_empty_board(len(perm))
    for ndx in range(len(perm)):
        board[perm[ndx]][ndx] = 1
    return board
    
def print_board(board):
    "Pretty print the board."
    print()
    for row in board:
        print(row)
    return

def is_solution(perm):
    "Check if input array contains queens on the same diagonal"
    # Given two queens, they are on the same diagonal if the horizontal
    #  distance between them is equal to the vertical distance between
    #  them.
    #
    # Cells (row1,col1) and (row2,col2) are on the same diagonal, 
    #  if and only if, |row1-row2|=|col1-col2|. 
    #
    # Remember, permutations care about order whereas combinations do not
    for (i,j) in itertools.combinations(range(len(perm)), 2):
        if ( abs(i-j) == abs(perm[i]-perm[j]) ): return False
        
    return True

def find_permutations(N):
    "Find all possible permuations of 0-(N-1)"
    return list(itertools.permutations(range(0,N)))

def find_solutions(all_permutations):
    "Utility function that checks validity of each solution"
    solutions = []
    for perm in all_permutations:
        if is_solution(perm): solutions.append(list(perm))
    return solutions

if __name__ == '__main__':
    # input size of board = number of queens
    print("How many queens to place?")
    # convert input string to a number
    N = int(input()) 

    all_permuations = find_permutations(N)
    solutions = find_solutions(all_permuations)

    print("There are",len(solutions),"solutions found.")
    print_board(solutions)
```
