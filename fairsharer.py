def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    # code
    values_new = values
    for i in range(0, num_iterations):
        index_of_max_value = values_new.index(max(values_new))
        max_value = max(values_new)
        max_share = max_value * share
        shared_values = []
        for i in range(0, len(values_new)):
            if (i == index_of_max_value-1) or (i == index_of_max_value+1):
                max_value -= max_share
                shared_values.append(values_new[i] + max_share)
            else:
                shared_values.append(values_new[i])
        shared_values[index_of_max_value] = max_value
        values_new = shared_values
        print(values_new)
    return values_new

fair_sharer([0,1000,90,800],20)