from collections import defaultdict


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
    f = open(fname, 'r')
    mappings = defaultdict(list)
    for line_number, line in enumerate(f):
        #print(f"line number {line_number}")
        #print(line.lower().split())
        for position,word in enumerate(line):
            mappings[word].append((line_number,position))
    res = [0]*len(message)
    for i,word in enumerate(message):
        res[i] = mappings[word][0]
    return res

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
    pass

print(encrypt_message("let us", "metamorphosis.txt"))