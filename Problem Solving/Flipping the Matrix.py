def flippingMatrix(matrix):
    # Write your code here
    return sum([max([matrix[row][column], matrix[-(row+1)][column], matrix[row][-(column+1)], matrix[-(row+1)][-(column+1)]]) for row in range(int(len(matrix)/2)) for column in range(int(len(matrix)/2))])
