#Example: ComplexMatrix class that represents a 2x2 matrix of complex numbers. [Cover mostly dunder methods]
class ComplexMatrix:
    def __init__(self, a, b, c, d):
        self.matrix = [[complex(a), complex(b)], [complex(c), complex(d)]]

    # __str__ and __repr__ for string representation
    def __str__(self):
        return f"{self.matrix[0]}\n{self.matrix[1]}"
    
    def __repr__(self):
        return f"ComplexMatrix({self.matrix[0][0]}, {self.matrix[0][1]}, {self.matrix[1][0]}, {self.matrix[1][1]})"

    # __len__ to get the number of elements
    def __len__(self):
        return 4  # 2x2 matrix

    # __getitem__ and __setitem__ for indexing
    def __getitem__(self, index):
        row, col = index
        return self.matrix[row][col]

    def __setitem__(self, index, value):
        row, col = index
        self.matrix[row][col] = complex(value)

    # __add__, __radd__, and __iadd__ for addition
    def __add__(self, other):
        if isinstance(other, ComplexMatrix):
            return ComplexMatrix(
                self[0, 0] + other[0, 0], self[0, 1] + other[0, 1],
                self[1, 0] + other[1, 0], self[1, 1] + other[1, 1]
            )
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        result = self + other
        self.matrix = result.matrix
        return self

    # __mul__ and __rmul__ for scalar multiplication
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float, complex)):
            return ComplexMatrix(
                self[0, 0] * scalar, self[0, 1] * scalar,
                self[1, 0] * scalar, self[1, 1] * scalar
            )
        return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    # __eq__ for comparison
    def __eq__(self, other):
        return self.matrix == other.matrix

    # __call__ to calculate the determinant
    def __call__(self):
        return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]

    # __iter__ to iterate over elements in the matrix
    def __iter__(self):
        return iter([self[0, 0], self[0, 1], self[1, 0], self[1, 1]])

    # Context management (__enter__ and __exit__)
    def __enter__(self):
        print("Entering the context of ComplexMatrix")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context of ComplexMatrix")

    # __del__ for cleanup
    def __del__(self):
        print("ComplexMatrix instance is being deleted")

# Usage Example
with ComplexMatrix(1+2j, 2+3j, 4+5j, 6+7j) as matrix:
    print("Matrix:")
    print(matrix)

    print("\nMatrix Determinant:", matrix())

    # Length of the matrix
    print("\nLength:", len(matrix))

    # Accessing and setting elements
    print("\nElement at (0, 1):", matrix[0, 1])
    matrix[0, 1] = 10 + 10j
    print("Updated Matrix:\n", matrix)

    # Addition with another matrix
    other_matrix = ComplexMatrix(1, 1, 1, 1)
    sum_matrix = matrix + other_matrix
    print("\nSum of Matrices:\n", sum_matrix)

    # Scalar multiplication
    scaled_matrix = 2 * matrix
    print("\nScaled Matrix:\n", scaled_matrix)

    # Iterating over matrix elements
    print("\nIterating over elements:")
    for element in matrix:
        print(element)

    # Equality check
    print("\nIs matrix equal to other_matrix?", matrix == other_matrix)

print("\nOutside the context, matrix should be cleaned up")
