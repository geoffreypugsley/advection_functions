def subset_around_point(matrix, initial_point, subset_size):
    """
    Extracts a subset of a matrix around the specified initial point.

    Parameters:
    - matrix: The input matrix.
    - initial_point: Tuple containing (row, column) indices of the initial point.
    - subset_size: Size of the subset to be extracted.

    Returns:
    - subset_matrix: The extracted subset.
    """

    # Calculate the indices for the subset
    start_row = max(0, initial_point[1] - subset_size // 2)
    end_row = min(matrix.shape[0], start_row + subset_size)

    start_col = max(0, initial_point[0] - subset_size // 2)
    end_col = min(matrix.shape[1], start_col + subset_size)

    # Extract the subset
    subset_matrix = matrix[start_row:end_row, start_col:end_col]

    return subset_matrix
