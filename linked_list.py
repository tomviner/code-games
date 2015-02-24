from collections import Sequence


class Node(Sequence):
    def __init__(self, value, next=None):
        self.value = value
        self._next = next

    def __repr__(self):
        return '[{}]-->{}'.format(self.value, self._next)

    def traverse(self):
        if not self._next:
            return [self.value]
        return [self.value] + self._next.traverse()

    def reverse(self, last=None):
        next = self._next
        self._next = last
        if next:
            return next.reverse(self)
        return self

    def __iter__(self):
        return self

    def next(self):
        print self
        if self._next:
            return self._next
        raise StopIteration

    def __getitem__(self, n):
        index = self.value - 1
        diff = abs(index - n)
        if n == index:
            return self
        next_index = self._next.value - 1
        next_diff = abs(next_index - n)
        if next_diff < diff:
            return self._next.__getitem__(n)
        raise IndexError("can't find item {}".format(n))

    def __len__(self):
        return max(self.traverse())

    def __getattribute__(self, name):
        print '__getattribute__', name
        return object.__getattribute__(self, name)

def reverse_from_head(head):
    node = head
    last = None
    while True:
        next = node._next
        node._next = last
        if not next:
            return node
        last = node
        node = next
