with open("stringmatrix.dat", "r") as file:
    grid = [line.split() for line in file if line.strip()]
    print("Grid:")
    print(grid)
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if any(len(row) != cols for row in grid):
        raise ValueError("The input file does not contain a rectangular matrix.")
        print("Number of rows:", rows)
        print("Number of columns:", cols)
        columns = []
        for j in range(cols):
            columns.append([grid[i][j] for i in range(rows)])
            print("Columns:")
            print(columns)
            diagonals = []
            for start_col in range(cols):
                diagonal = []
                i, j = 0, start_col
                while i < rows and j < cols:
                    diagonal.append(grid[i][j])
                    i += 1
                    j += 1
                    diagonals.append(diagonal)
                    for start_row in range(1, rows):
                        diagonal = []
                        i, j = start_row, 0
                        while i < rows and j < cols:
                            diagonal.append(grid[i][j])
                            i += 1
                            j += 1
                            diagonals.append(diagonal)
                            print("Diagonals:")
                            print(diagonals)