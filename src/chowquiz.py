import pdb
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
    for i in range (start, end):
        if i % 7 == 0:
            result.append(i)
    return result

def dummy():
    #pdb.set_trace()
    return [1]
