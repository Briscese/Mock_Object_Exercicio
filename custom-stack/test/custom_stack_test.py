import pytest
from src.custom_stack_class import *

def test_push_one_element_in_stack():
    element_value = 5.0
    cut = CustomStack(5)
    cut.push(element_value)
    assert not cut.is_empty()
    assert element_value == cut.top()
    assert 1 == cut.size()

def test_push_until_limit_and_raise_exception():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)
    with pytest.raises(StackFullException):
        cut.push(3)

def test_pop_element_from_stack():
    cut = CustomStack(3)
    cut.push(10)
    assert cut.pop() == 10
    assert cut.is_empty()

def test_pop_from_empty_stack_raises_exception():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.pop()

def test_top_from_empty_stack_raises_exception():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.top()

def test_top_after_multiple_pushes():
    cut = CustomStack(5)
    cut.push(1)
    cut.push(2)
    cut.push(3)
    assert cut.top() == 3
    assert cut.size() == 3
