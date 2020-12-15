Title: N-Queens Puzzle, Part 3-Backtracking Algorithm (All Solutions)
Date: 2020-07-17
Tags: Python
Author: Joe
Keywords: ubuntu 20.4, n queens, n-queens, backtracking search, alogrithms, python 3
Version: OS, Ubuntu 20.04 LTS, python, 3.7.4
Status: Draft

This article is Part 3 in a series implementing different algorithms to solve the N-Queens problem. In this article I’ll be exploring the [backtracking](https://en.wikipedia.org/wiki/Backtracking) search algorithm. See the first article ["Part 1-Introduction"](n-queens-puzzle-part-1-introduction.html) for an overview of the puzzle and some background information.

### Backtracking

This is a common algorithm that is intuitive to human thinking; a candidate is iteratively built up and then "backtracks" when it is determined that it cannot be a solution. Think of how a child goes through a maze, he comes upon a right/left decision and choses right. That leads to a deadend so he comes back to the decision point and re-selects left. That path comes to another right/left decision and so on. 

Abandoning a path that we know is fruitless can save a lot of computation time. Clearly there is no sense in continuing looking for a solution if we know one does not exist.