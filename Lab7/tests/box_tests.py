import pytest

from ..box import Box

# Write your tests here
@pytest.fixture
def emptyBox():
    return Box(True)

@pytest.fixture
def nonEmptyBox():
    box = Box()
    return box

@pytest.mark.isEmpty

def test_box_isempty_true(emptyBox):
    assert emptyBox.isEmtpy()

@pytest.mark.isEmpty

def test_hashmap_isempty_false(nonEmptyBox):
    assert not nonEmptyBox.isEmpty()

@pytest.mark.find

def test_box_find(nonEmptyBox):
    species = nonEmptyBox.findEntryByNickName("Sparky").getValue().getSpecies()
    assert species == "Pikachu"

# Write your tests here