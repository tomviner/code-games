import pytest
from linked_list import Node, reverse_from_head

from itertools import izip

@pytest.fixture
def l1():
    l3 = Node(3)
    l2 = Node(2, l3)
    l1 = Node(1, l2)
    return l1

def test_traverse(l1):
    assert l1.traverse() == [1, 2, 3]

def test_reverse_traverse(l1):
    l3 = l1.reverse()
    assert l3.traverse() == [3, 2, 1]

def test_reverse_one_el():
    l3 = Node(3)
    assert l3.reverse().traverse() == [3]

def test_reverse_from_head(l1):
    assert reverse_from_head(l1).traverse() == [3, 2, 1]

def test_builtin_reverse(l1):
    for node, expected_val in izip(reversed(l1), [3, 2, 1]):
        print node, expected_val
        assert node.value == expected_val

def test_loop(l1):
    for node, expected_val in izip(l1, [1, 2, 3]):
        print 'node', node, 'expected_val', expected_val
        print
        assert node.value == expected_val
