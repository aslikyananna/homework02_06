Suppose you have a 5 × 5 list that consists of zeros and M’s. Write a program that creates a new 5 × 5 list that has M’s in the same place, but the zeroes are replaced by counts of how many M’s are in adjacent cells (adjacent either horizontally, vertically, or diagonally). An example is shown below. [Hint: short-circuiting may be helpful for avoiding index-out-of-range errors.] 
0 M 0 M 0     1 M 3 M 1
0 0 M 0 0       1 2 M 2 1
0 0 0 0 0        2 3 2 1 0
M M 0 0 0      M M 2 1 1
0 0 0 M 0       2 2 2 M 1


Write a program that rotates a matrix by 180 degrees.
Input:
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
Output:
16  15  14  13
12  11  10  9
8   7   6   5
4   3   2   1



Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm, and asks them how many hours into the future they want to go. Print out what the hour will be that many hours into the future, printing am or pm as appropriate. An example is shown below.
Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead? 5
New hour: 1 pm
