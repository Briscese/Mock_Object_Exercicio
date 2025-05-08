import pytest
from src.custom_stack_class import CustomStack, StackEmptyException
from src.number_asc_order import NumberAscOrder

def test_sort_with_six_elements():
    stack = CustomStack(6)
    numeros = [23, 5, 41, 17, 2, 33]

    for num in numeros:
        stack.push(num)

    sorter = NumberAscOrder()
    resultado = sorter.sort(stack)

    assert resultado == sorted(numeros)

def test_sort_with_empty_stack_raises_exception():
    stack = CustomStack(6)
    sorter = NumberAscOrder()

    with pytest.raises(StackEmptyException):
        sorter.sort(stack)
