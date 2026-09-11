from matrix import Matrix

def guassian_elimination(matrix):
    data = [row[:] for row in matrix.data]

    rows = matrix.rows
    cols = matrix.cols

    for i in range(rows):
        pivot = data[i][i]

        if pivot == 0:
            for row in range(i + 1, rows):
                if data[row][i] != 0:
                    data[i], data[row] = data[row], data[i]
                    pivot = data[i][i]
                    break
            else:        
                raise ValueError("System has no unique solutions.")
            
        for j in range(i, cols):
            data[i][j] = data[i][j] / pivot

        for k in range(i + 1, rows):
            factor = data[k][i]
                
            for j in range(i, cols):
                data[k][j] -= factor * data[i][j]

    return Matrix(data)

def back_substitution(matrix):
        data = matrix.data

        rows = matrix.rows
        cols = matrix.cols

        solutions = [0] * rows

        for i in range(rows -1, -1, -1):
            value = data[i][cols - 1]

            for j in range(i + 1, rows):
                value -= data[i][j] * solutions[j]

            solutions[i] = value / data[i][i]
        
        return solutions 

def solve(matrix):
        upper_matrix = guassian_elimination(matrix)
        return back_substitution(upper_matrix)
    