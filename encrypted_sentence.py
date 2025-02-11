import collections
import random
import string

def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 

    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert(isinstance(message, str)), "Message must be a valid string"
    assert(isinstance(fname, str)), "fname must be a valid string"
    # Build the map for encryption
    encryption_mappings,_ = build_encryption_decryption_map(fname)
    # Do the actual encryption
    message = message.split()
    # print(message)
    encrypted_result = [0]*len(message)
    for i,word in enumerate(message):
        try:
            assert(word in encryption_mappings), "Word in sentence to encrypt must be a valid word found in Metamorphosis"
        except AssertionError as e:
            print(f"Encryption failed: {e}")
            print(word)
            return None
        tuples = encryption_mappings[word]
        # Randomly choose a tuple to map the word and pop it from the list of possible mappings
        # To increase randomness and reduce duplicate mappings during encryption
        element = tuples.pop(random.randrange(len(tuples)))
        encrypted_result[i] = element
    return encrypted_result

def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message. 
    
    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert(isinstance(inlist, list)), "inlist must be a list"
    for tup in inlist:
        assert(isinstance(tup,tuple) and len(tup) == 2 and isinstance(tup[0],int) and 
               isinstance(tup[1],int)), "Element in list is not a valid tuple of two ints"
        # Also assert against duplicate tuples in the inlist
    
    _,decrypted_mappings = build_encryption_decryption_map(fname)
    decrypted_result = [0]*len(inlist)
    for i,tup in enumerate(inlist):
        try:
            assert(tup in decrypted_mappings), "Tuple must be valid within the Metamorphosis text"
            assert(len(inlist) == len(set(inlist))), "Cannot have duplicate tuples in the list"
        except AssertionError as e:
            print(f"Decryption failed: {e}")
            return None
        decrypted_result[i] = decrypted_mappings[tup]
    return " ".join(decrypted_result)

def build_encryption_decryption_map(fname):
    """
    Builds a dictionary that maps each word to a list of possible tuples.
    Each tuple represents the (line number, position in the line) of where that specific
    key word is found in the fname file that is pased as an argument.

    :param fname: filename for source text
    :type fname: str
    :returns: a dictionary that maps the possible encodings for encrypting and decrypting
    """
    assert(isinstance(fname, str)), "fname must be a valid file in str format"
    f = open(fname, 'r')
    encrypt_mappings = collections.defaultdict(list)
    decrypt_mappings = {}
    for line_number, line in enumerate(f):
        filtered = line.translate(str.maketrans('', '', string.punctuation)).lower().split()
        for position,word in enumerate(filtered):
            try:
                assert((line_number+1,position+1) not in encrypt_mappings[word]), "Tuples cannot be repeated for the same word"
            except AssertionError as e:
                print(f"Encryption map building failed: {e}")
                return None
            encrypt_mappings[word].append((line_number+1,position+1))
            decrypt_mappings[(line_number+1,position+1)] = word
    return encrypt_mappings,decrypt_mappings