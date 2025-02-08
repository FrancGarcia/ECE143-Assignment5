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