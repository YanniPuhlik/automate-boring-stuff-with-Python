#Character Picture Grid, Chapter 4
#Say you have a list of lists where each
#value in the inner lists is a one-character string, like this:

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#write code that uses it to print the image.


#..OO.OO..
#.OOOOOOO.
#.OOOOOOO.
#..OOOOO..
#...OOO...
#....O....


# Answer:
for i in range(len(grid[1])):
    for row in grid:
        print (row[i], end='')
    print()

