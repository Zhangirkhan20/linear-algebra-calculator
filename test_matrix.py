import unittest

from matrix import Matrix
from gaussian import solve


class TestMatrix(unittest.TestCase):

    def test_addition(self):
        a = Matrix([
            [1, 2],
            [3, 4]
        ])

        b = Matrix([
            [5, 6],
            [7, 8]
        ])

        result = a + b

        self.assertEqual(
            result.data,
            [
                [6, 8],
                [10, 12]
            ]
        )
    
    def test_matrix_subtraction(self):
        a = Matrix([[5, 7], [3, 8]])
        b = Matrix([[2, 4], [1, 6]])

        result = a - b

        self.assertEqual(result.data, [[3, 3], [2, 2]])

    def test_multiplication(self):
        a = Matrix([
            [1, 2],
            [3, 4]
        ])

        b = Matrix([
            [5, 6],
            [7, 8]
        ])

        result = a * b

        self.assertEqual(
            result.data,
            [
                [19, 22],
                [43, 50]
            ]
        )

    def test_transpose(self):
        a = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        result = a.transpose()

        self.assertEqual(
            result.data,
            [
                [1, 4],
                [2, 5],
                [3, 6]
            ]
        )

    def test_determinant(self):
        a = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(a.determinant(), -2)

    def test_gaussian_solution(self):
        system = Matrix([
            [1, 1, 1, 6],
            [2, -1, 1, 3],
            [1, 2, -1, 2]
        ])

        result = solve(system)

        self.assertEqual(
            result,
            [1.0, 2.0, 3.0]
        )

    def test_addition_dimension_error(self):
        a = Matrix([
            [1, 2],
            [3, 4]
        ])

        b = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        with self.assertRaises(ValueError):
            a + b


if __name__ == "__main__":
    unittest.main()