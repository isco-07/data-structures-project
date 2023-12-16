"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Node, Stack

# @pytest.fixture
# def stack():
#     return Node(5, None)


def test_class_node():
    n1 = Node(5, None)
    n2 = Node('a', n1)
    assert n1.data == 5
    assert n2.data == 'a'


def test_class_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top.data == 3
    assert stack.top.next_node.data == 2
    assert stack.top.next_node.next_node.data == 1
