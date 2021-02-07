# Instructions

Neighbor Joining Problem
Construct the tree resulting from applying the neighbor-joining algorithm to a distance matrix.

Given: An integer n, followed by a space-separated n x n distance matrix.

Return: An adjacency list for the tree resulting from applying the neighbor-joining algorithm. Edge-weights should be accurate to two decimal places (they are provided to three decimal places in the sample output below).

Note on formatting: The adjacency list must have consecutive integer node labels starting from 0. The n leaves must be labeled 0, 1, ..., n-1 in order of their appearance in the distance matrix. Labels for internal nodes may be labeled in any order but must start from n and increase consecutively.



Your code must have a function named `main` that will take as input the integer `n`  and the matrix `D` as a list of lists and return the tree `t` as a dictionary of dictionaries, i.e to encode an edge that goes from node 1 to node 4 with the weight of 8 do:

```
# assume t is the tree
t[1][4] = 8.0
```

Note that leaf and node labels should be integers as described in the Rosalind page:

http://rosalind.info/problems/ba7e/

Run the tester as below:

```
python tester.py
```

Your `neighbors.py` file should be in the same directory as the tester for the above to work.
