import pytest

from myHashMap import MyHashMap

@pytest.fixture
def emptyHashMap():
    return MyHashMap()

@pytest.fixture
def nonEmptyHashMap():
    myHashMap = MyHashMap()
    myHashMap.put("Jose", "Student")
    myHashMap.put("Alyssa", "Professor")

    return myHashMap

@pytest.mark.isEmpty

def test_hashmap_isempty_true(emptyHashMap):
    assert emptyHashMap.isEmtpy()

@pytest.mark.isEmpty

def test_hashmap_isempty_false(nonEmptyHashMap):
    assert not nonEmptyHashMap.isEmpty()

@pytest.mark.size 

def test_hashmap_size(nonEmptyHashMap):
    assert nonEmptyHashMap.size() == 3

# Write your tests here