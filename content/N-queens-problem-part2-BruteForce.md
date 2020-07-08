Title: N-Queens Puzzle, Part 2-Brute Force Algorithm
Date: 2020-07-03
Tags: Python
Author: Joe
Keywords: ubuntu 20.4, n queens, n-queens, brute-force search, alogrithms, python 3
Version: OS, Ubuntu 20.04 LTS, python, 3.7.4

This article is number 2 in a series implementing different alogrithms to solve the N-Queens problem. See the first article ["Part 1-Introduction"](n-queens-puzzle-part-1-introduction.html) for an overview of the puzzle and some background information.

In this article I'm going to implement a Brute-Force algorithm in python to find solutions to the N-Queens puzzle. 

### Brute-Force Search Algorithm

The [Brute-Force Algorithm](https://en.wikipedia.org/wiki/Brute-force_search) involves finding all possible permutations of the queen positions and then evaluating each to determine if it is a valid solution. This is typically one of the easier search algorithms to implement and it will always find a solution if it exists, however, the computational cost is proportional to the number of candidates and increases to be impractical very quickly. This is known as “combinatorial explosion” and limits the use of this algorithm as the computational cost of finding a solution grows exponentially as the search space increases.

In this “brute force” algorithm we find the solution by looking at every position on an NxN board, N times, for N queens. Assuming the reader understands [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation), this means $O(N^N)$  time complexity!! Wow.

### Dimensionality Reduction via Encoding

One method of time complexity is to reduce the computations, we reduce computations by reducing the search space, we reduce the search space by reducing dimensionality. For the N-Queens problem we can do that heuristically by recognizing  we can have only one queen in the row or column. 

For the remainder of this article, I’ll be using an N=4 example.  In the particular solution below, a 4x4 board has 4 queens placed on it, denoted by red X's. The indices are [zero indexed](https://en.wikipedia.org/wiki/Zero-based_numbering), meaning they start at zero. For a generalized NxN grid (aka. board) the indices go from 0 to N-1. For the time being, it doesn’t matter where the queens are placed, assume this example is a random solution.

![NQueens_1_00](/images/NQueens_1_00.png)

One way of encoding the queen locations are  to use a list of ordered pairs representing the row and column positions.

$$[ (row_0,col_0), (row_1,col_1), (row_{N-1},...,col_{N-1}) ]$$

The above example can be encoded as [ (1,0),(3,1),(0,2),(2,3)], that is a queen is located at position (1,0), position (3,1), and so on as shown in the image below.

![NQueens_1_02](/images/NQueens_1_02.png)

We can reduce the dimensionality by recognizing the column value is already represented by the location within the list.

![NQueens_1_03](/images/NQueens_1_03.png)

Therefore, this example can be encoded as $[1,3,0,2]$ - where by definition, there can only be a single queen in each column, thus eliminating one dimension that needs to be searched.

### Relationships = Combinations

I showed how we can encode our queen placement as an ordered list,  $Queens=[1,3,0,2]$, now we can discuss the interaction or relationship between each of them. Mathematically these are called [combinations](https://en.wikipedia.org/wiki/Combination). Given a collection of queens, we can show each possible interaction between any two queens as $\binom {Queens}k$. 

![NQueens_1_02](/images/NQueens_1_01.png)

The combination $A=(0,1)$ is the interaction between the queen in row 0 and the queen in row 1, as so on.
```python
A = (0,1)
B = (0,2)
C = (0,3)
D = (1,2)
E = (1,3)
F = (2,3)
```

### Code
I used python3 language for the code to implement this algorithm. It could have been written in nearly anything, but I like python. It also has a great library named `itertools` which provides very optimized functions for iterative functionality. I took advantage of this library, specifically, the optimized permutation and combination functions. 

```python
#### IMPORTS

import itertools

#### FUNCTIONS ####

def perm_to_board(perm):
    "Makes a full board board from a given permutation"
    board = create_empty_board(len(perm))
    for ndx in range(len(perm)):
        board[perm[ndx]][ndx] = 1
    return board

def print_perm(perm):
    "Pretty print utility function"
    print()
    print(perm," =" )
    print_board(perm_to_board(perm))
    
def is_solution(perm):
    "Check if input array contains queens on the same diagonal"
    for (i,j) in itertools.combinations(range(len(perm)), 2):
        if ( abs(i-j) == abs(perm[i]-perm[j]) ): return False
    return True

def find_permutations(N):
    "Find all possible permuations of 0-(N-1)"
    return list(itertools.permutations(range(0,N)))

def find_first_solutions(all_permutations):
    "Utility function that checks validity of each solution"
    for perm in all_permutations:
        if is_solution(perm): return perm
        
if __name__ == '__main__':
    # input size of board = number of queens
    print("How many queens to place?")
    # convert input string to a number
    N = int(input()) 

    # find all permutations of N queens
    all_permuations = find_permutations(N)

    # go through all perms, return first valid one
    perm = find_first_solutions(all_permuations)

    # pretty print the perm and board
    print_perm(perm)
```

So what is going on here? First I ask the user how many queens to place on an NxN board. Then find all permutations of 0-N as possible candidates. I then evaluate each one until a solution is found. As explained in a previous section, the problem is constrained such that there is only one queen in each column. By looking for permutations of only $[0,1,2,...,N]$ I further constrained the problem to only one queen in each row in my permutation definition. This leaves the validation to only having to evaluate whether the candidate location is blocked by an existing queen on the diagonal. A tricky solution to this is recognizing that given two queens, they are on the same diagonal if and only if the horizontal distance between them is equal to the vertical distance between them. 

![NQueens_1_02](/images/NQueens_1_04.png)

Referring to the above image, the horizontal distance (*h*) between the two points is $\lvert 2-0 \rvert$, and the vertical distance (*v*) between the two points is $\lvert 0-2 \rvert$. Those values are equal to each other so the two points are on a diagonal from each other and are not valid placements. 