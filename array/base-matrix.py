def matrix_two(matrix):
    rows, cols = len(matrix), len(matrix[0]);
    new_matrix = [];

    # this way i can print all the elements that are in the matrix
    for j in range(rows):
        for i in range(cols):
            print(matrix[j][i]);
    
    # this way i can get the first element in each row
    # or all the elements in the first column
    for j in range(rows):
        print('first element in each row', matrix[j][0]);
    
    # create a new matrix but using the columns as rows 
    for j in range(cols):
        arr = [];
        for i in range(rows):
            arr.append(matrix[i][j]);
        new_matrix.append(arr);
    
    # print the first element in each column
    for x in matrix[0]:
        print('first columns elements', x);

    # print the last element in each column
    for i in matrix[len(matrix) - 1]:
        print('last columns elements:', i)
        
    # print(new_matrix);

    
matrix_two([[1,2,3],[4,5,6],[7,8,9],[1,4,7]]);