from collections import defaultdict
import random

def get_sample(nbits=3,prob=None,n=1):
    """
    Returns a random sampled list of size n from a finite probability mass function p organized as a dictionary.

    :param nbits: The number of bits of each key in the dictionary.
    :param prob: The probability mass function organized as a dictionary.
    :param n: The number of random samples to return from the dictionary at random.

    :return: A list that contains the randomly sampled keys from the dictionary.
    """
    if prob is None:
        return []
    assert(isinstance(nbits,int)), "nbits must be an int"
    assert(isinstance(n,int) and n > 0), "n must be an int greater than 0"
    assert(isinstance(prob, dict)), "prob must be a dictionary"
    for index,(key,value) in enumerate(prob.items()):
        try:
            num = int(key,2)
        except ValueError as e:
            print(f"Error: {e}")
        assert(num == index), f"Key must be equal to index"
        assert(isinstance(key,str) and len(key) == nbits), f"Each key must be a string of length nbits"
        assert(0 <= value and value <= 1 and (isinstance(value, int) or isinstance(value, float))), f"Each value must be an int or decimal between 0 and 1 inclusive"
    assert(sum(prob.values()) == 1), f"The sum of the probability mass distribution must be 1"
    
    numbers = list(prob.keys())
    probabilities = list(prob.values())
    return random.choices(numbers, probabilities, k=n)

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

def gather_values(x: list):
    """
    Returns a dictionary of lists that contain the mapped values from map_bitstring.

    :param x: The list retrieved from get_sample() function 
    :return: A dictionary that contains the bitstrings as the keys and the bitstring mappings as the values.
    """
    res = {}
    mappings = map_bitstring(x)
    for num in x:
        if num in res:
            res[num].append(mappings[num])
        else:
            res[num] = [mappings[num]]
    return res

def threshold_values(seq,threshold=1):
    """
    Returns a filtered dictionary that keeps the top threshold keys and sets all other values to 0.
    In case of ties, choose the smalelst value between the bitstrings as the tie-breaker.

    :param seq: The list to pass into gather_values()
    :param threshold: The number of most frequent keys to keep.
    :return: A filtered dictionary with the most frequent keys' values set to 1 and 0 for the other keys.
    """
    assert(isinstance(seq, list)), "Seq must be a list"
    assert(isinstance(threshold, int) and threshold >= 0), "Threshold must be a valid int greater than or equal to 0"
    seq = dict(sorted(gather_values(seq).items(), key=lambda x: x[0]))
    new_dict = {int(key,2):sum(value) for key,value in seq.items()}
    filtered_dict = dict(sorted(new_dict.items(), key=lambda x: (-x[1], x[0])))
    for i,(key,value) in enumerate(filtered_dict.items()):
        if i < threshold:
            filtered_dict[key] = 1
        else:
            filtered_dict[key] = 0
    for key,value in seq.items():
        seq[key] = filtered_dict[int(key,2)]
    return seq
