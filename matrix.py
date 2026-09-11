class Matrix:
    def __init__(self, data):
        if not data:
            raise ValueError("Matrix data cannot be empty.")

        row_length = len(data[0])

        for row in data:
            if len(row) != row_length:
                raise ValueError("All rows in the matrix must have the same length.")

            
        self.data = data
        self.rows = len(data)
        self.cols = row_length




    def __str__(self):
        result = ""

        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
            

        return result 


    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")

        result = []

        for i in range(self.rows):
            new_row = []

            for j in range(self.cols):
                value = self.data[i][j] + other.data[i][j]
                new_row.append(value)

            result.append(new_row)

        return Matrix(result)
    

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must equal "
                "number of rows in the second matrix."
            )

        result = []

        for i in range(self.rows):
            new_row = []

            for j in range(other.cols):
                value = 0

                for k in range(self.cols):
                    value += self.data[i][k] * other.data[k][j]

                new_row.append(value)

            result.append(new_row)

        return Matrix(result)

        
    def transpose(self):
        result = []

        for j in range(self.cols):
            new_row = []

            for i in range(self.rows):
                new_row.append(self.data[i][j])

            result.append(new_row)

        return Matrix(result)


    def determinant(self):
        if not self.is_square():
            raise ValueError("Determinant is only defined for square matrices.")

        if self.rows == 2:
            return (
                self.data[0][0] * self.data[1][1]
                - self.data[0][1] * self.data[1][0]
            )

        raise NotImplementedError("Determinant currently supports only 2x2 matrices.")


    def is_square(self):
        return self.rows == self.cols



