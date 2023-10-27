class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.elements = [[0] * columns for _ in range(rows)]
    
    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match.")
        
        result = Matrix(self.rows, self.columns)
        
        for i in range(self.rows):
            for j in range(self.columns):
                result.elements[i][j] = self.elements[i][j] + other.elements[i][j]
        
        return result

# Create two Matrix objects
matrix1 = Matrix(2, 2)
matrix1.elements = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.elements = [[5, 6], [7, 8]]

# Add the matrices using the + operator
result = matrix1 + matrix2

# Access the result matrix elements
for row in result.elements:
    print(row)








'''
class Result:
    def __init__(self, attempts=0, right=0, wrong=0):
        self.attempts = attempts
        self.right = right
        self.wrong = wrong
    
    def __add__(self, other):
        total_attempts = self.attempts + other.attempts
        total_right = self.right + other.right
        total_wrong = self.wrong + other.wrong
        return Result(total_attempts, total_right, total_wrong)


# Create two Result objects
result1 = Result(3, 2, 1)
result2 = Result(4, 3, 1)

# Combine the results using the + operator
combined_result = result1 + result2

# Access the combined results
print(combined_result.attempts)  
print(combined_result.right)     
print(combined_result.wrong)     
'''