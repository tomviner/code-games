from collections import Iterator


class Node(Iterator):
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
