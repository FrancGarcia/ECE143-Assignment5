def map_bitstring(x: list):
    """
    Maps the elements in the list to 0 if number of 0's in the element
    is strictly more than the number of 1's in that same element.
    :param x: The list of bitstrings to be mapped
    :return: A dictionary that maps the bitstrings to 0 or 1
    """
    assert(isinstance(x,list)), "x must be a list"
    for num in x:
        assert(isinstance(num, str)), "Each element must be a string"
        assert(set(num).issubset({'0','1'})), "Each element must only contain 0's and 1's"
    my_dict = {}
    for bitstring in x:
        ones_count = 0
        zeroes_count = 0
        for bit in bitstring:
            if bit == '1':
                ones_count += 1
            else:
                zeroes_count += 1
        if zeroes_count > ones_count:
            my_dict[bitstring] = 0
        else:
            my_dict[bitstring] = 1
    return my_dict
