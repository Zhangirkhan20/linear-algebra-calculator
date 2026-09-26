from matrix import Matrix
from gaussian import solve

def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    data = []

    for i in range(rows):
        row = list(map(float, input(f"Enter row {i + 1}: ").split()))

        if len(row) != cols:
            raise ValueError("Incorrect number of elements in row")

        data.append(row)

    return Matrix(data)

def main():
    while True:
        print("1. Add matrices")
        print("2. Subtract matrices")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Determinant")
        print("6. Solve linear system")
        print("7. Exit")

        choice = input("Choose an option: ")
        
        try:
            if choice == "1":
                a = input_matrix()
                b = input_matrix()
                print(a + b)

            elif choice == "2":
                a = input_matrix()
                b = input_matrix()
                print(a - b)

            elif choice == "3":
                a = input_matrix()
                b = input_matrix()
                print(a * b)
    
            elif choice == "4":
                a = input_matrix()
                print(a.transpose())

            elif choice == "5":
                a = input_matrix()
                print("Determinant:", a.determinant())

            elif choice == "6":
                system = input_matrix()
                print("Solution:", solve(system))

            elif choice == "7":
                break

            else:
                print("Invalid option.")

        except ValueError as error:
            print("Error:", error)

        
           
if __name__ == "__main__":
    main()