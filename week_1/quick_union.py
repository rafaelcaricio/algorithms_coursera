#!/usr/bin/env python


class QuickUnion(object):
    def __init__(self, n):
        self.entities = []
        for i in xrange(n):
            self.entities.append(i)

    def root(self, p):
        while self.entities[p] != p:
            p = self.entities[p]
        return p

    def connected(self, p1, p2):
        root_of_p1 = self.root(p1)
        root_of_p2 = self.root(p2)
        return root_of_p1 == root_of_p2

    def union(self, p1, p2):
        root_of_p1 = self.root(p1)
        root_of_p2 = self.root(p2)
        self.entities[root_of_p1] = root_of_p2


if __name__ == '__main__':
    qf = QuickUnion(5)
    assert qf.entities == [0,1,2,3,4]
    qf.union(0,1)
    assert qf.entities == [1,1,2,3,4]
    qf.union(3,4)
    assert qf.entities == [1,1,2,4,4]
    qf.union(4,0)
    assert qf.entities == [1,1,2,4,1]
    assert qf.connected(4, 1)
    print "Yay! \o/"
