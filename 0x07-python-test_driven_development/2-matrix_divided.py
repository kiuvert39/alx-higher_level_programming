def matrix_divided(matrix, div):
    typeErrorMessage = 'matrix must be a matrix (list of lists) of integers/floats'
    sizeError = 'Each row of the matrix must have the same size'
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(typeErrorMessage)
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(typeErrorMessage)
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(sizeError)
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    
    return new_matrix