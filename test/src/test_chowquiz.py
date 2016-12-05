import unittest
from src.chowquiz import list_of_integers, dict_mapping, find_ips, generate_cubes_until, dummy

def test_list_of_integers():
    sample = list_of_integers(1,14)
    assert sample == [7,14]

    default_list = list_of_integers()
    assert default_list == [28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98] 

def test_dict_mapping():
	output = dict_mapping()
	assert len(output) == 99
	assert output[2] == 1.3195079107728942
	assert output[100] == 6.309573444801933

def test_find_ips():
	string = "this has one ip address 127.0.0.1"
	ip = find_ips(string)
	assert ip == ['127.0.0.1']

	string2 = "this has one ip address 127.0.0.1, but maybe two 0.0.0.0"
	ip2 = find_ips(string2)
	assert ip2 == ['127.0.0.1', '0.0.0.0']

def test_generate_cubes_until():
	cubes = generate_cubes_until(25)
	assert cubes == [1, 8, 27, 64]

def test_dummy():
    subject = dummy() 
    assert subject == [1]

