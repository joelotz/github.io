Title: N-Queens Puzzle, Part 1-Introduction
Date: 2020-06-26
Tags: Python
Author: Joe
Keywords: ubuntu 20.4, n queens, n-queens, backtracking, python 3
Version: OS, Ubuntu 20.04 LTS, python, 3.7.4

The N-Queens puzzle is the popular problem of placing N number of chess queens on an NxN grid board such that no queens cannot attack each other; i.e no two queens share the same row, column, or diagonal. The puzzle is often generalized to the “[8 Queens Puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle)” to match a standard size chess board and is a good example of a simple but nontrivial algorithm problem. 

* It is known that a solution exists for all N>3
* It gets *very* difficult to do by hand for N>7
* Good candidate for computer (programmatic) solution

### Combinations and Permutations

[Combinations](https://en.wikipedia.org/wiki/Combination) and [permutations](https://en.wikipedia.org/wiki/Permutation) are often confused; for our purposes I will simply say that one cares about order while the other does not, and this makes a difference. In combinations the pair $(0,1)$ is the same as $(1,0)$. This is good for relationships or interactions because the interaction between John and Bill is the same and between Bill and John, we don’t care about order. 

On the other hand, let’s say… for example… I want to calculate all the possible locations of queens without duplication of rows. So given a list of objects $[A,B,C,D]$ or, in our example case, the four possible rows $[0,1,2,3]$, how many different ways can we arrange the queens with one on each row?
$$ P_N = N! $$
$$ P_4 = 4!= 4 \cdot 3 \cdot 2 \cdot 1 = 24$$

Now is a good time to finally break out `python` and the standard library [itertools](https://docs.python.org/2/library/itertools.html). Here we can just ask itertools to create all the permutations of [0,1,2,3] for us. Note the result from itertools is an [iterator](https://www.geeksforgeeks.org/iterators-in-python/) so to view it (i.e. print it) we must turn the iterator into a list.
```python
import itertools
perms = list(itertools.permutations([0,1,2,3]))
print(perms)

[(0, 1, 2, 3),
 (0, 1, 3, 2),
 (0, 2, 1, 3),
 (0, 2, 3, 1),
 (0, 3, 1, 2),
 (0, 3, 2, 1),
 (1, 0, 2, 3),
 (1, 0, 3, 2),
 (1, 2, 0, 3),
 (1, 2, 3, 0),
 (1, 3, 0, 2),
 (1, 3, 2, 0),
 (2, 0, 1, 3),
 (2, 0, 3, 1),
 (2, 1, 0, 3),
 (2, 1, 3, 0),
 (2, 3, 0, 1),
 (2, 3, 1, 0),
 (3, 0, 1, 2),
 (3, 0, 2, 1),
 (3, 1, 0, 2),
 (3, 1, 2, 0),
 (3, 2, 0, 1),
 (3, 2, 1, 0)]
```
Above are all the possible locations of our queens. Since this is a python list we can view the length of it. For a 4x4 grid there are 24 possible locations of 4 queens on different rows.
```python
len(perms)
24
```
### Solutions

Now the part we've all been waiting for...how do we find the solution(s) to our puzzle? The different methods and algorithms of finding the solution is the fun part and the entire point of this series of articles. I will look at the popular algorithms as a exercise in my python coding skills and an opportunity to learn something new. 

See the next articles were I find solutions using the following algorithms:

- [Part 2 - Brute Force](n-queens-puzzle-part-2-brute-force-algorithm.html)
- [Part 2.5 - Brute Force (All Solutions)](n-queens-puzzle-part-25-brute-force-algorithm-all-solutions.html)
- [Part 3 - Backtracking](n-queens-puzzle-part-3-backtracking-algorithm-all-solutions.html)
- Part 3.5 - Backtracking with Threading
- Branch and Bound
- Genetic Algorithms