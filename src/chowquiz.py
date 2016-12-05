import pdb
import re
'''
Using Python 2.7 or 3.3+ syntax/semantics, please fill out the bodies of
the included functions to include implementations of what is described in the
docstrings.
'''

def list_of_integers(start=23, end=100):
    '''
    Returns a list of integers from 23 to 100 that are evenly divisible by 7.
    '''
    result = []
    for i in range (start, end+1):
        if i % 7 == 0:
            result.append(i)
    return result


def dict_mapping():
    '''
    Returns a dictionary mapping integers to their 2.5th root for all integers
    from 2 up to 100 (including 100).
    '''
    dictionary = {}
    for i in range(2, 100+1):
        compute = i**(1/2.5)
        dictionary[i] = compute

    return dictionary


def find_ips(inp):
    '''
    Returns a list of valid ip (v4) addresses of the form 'x.x.x.x'
    that are in the input string (separated by at least some whitespace).
    >>> find_ips('this has one ip address 127.0.0.1')
    ['127.0.0.1']
    '''

    pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
    test = pat.findall(inp)

    return test


def generate_cubes_until(modulus):
    '''
    Generates the cubes of integers greater than 0 until the next is 0 modulo
    the provided modulus.
    >>> list(generate_cubes_until(25))
    [1, 8, 27, 64]
    '''
    result = []
    count = 1

    while ( ((count**3) % modulus != 0) & (count < 100) ):
        result.append(count**3)
        count += 1

    return result


def dummy():
    #pdb.set_trace()
    return [1]
