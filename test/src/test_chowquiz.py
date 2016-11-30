import unittest
from src.chowquiz import list_of_integers, dummy

def test_list_of_integers():
    sample = list_of_integers(1,10)
    assert sample == [7]

    default_list = list_of_integers()
    assert default_list == [28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98] 

def test_dummy():
    subject = dummy() 
    assert subject == [1]

