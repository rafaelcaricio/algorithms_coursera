#!/usr/bin/env python


class QuickUnion(object):
    def __init__(self, n):
        self.entities = []
        self.tree_size = []
        for i in xrange(n):
            self.entities.append(i)
            self.tree_size.append(1)

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
        if self.tree_size[root_of_p1]\
            >= self.tree_size[root_of_p2]:
            self.entities[root_of_p2] = root_of_p1
            self.tree_size[root_of_p1] += self.tree_size[root_of_p2]
        else:
            self.entities[root_of_p1] = root_of_p2
            self.tree_size[root_of_p2] += self.tree_size[root_of_p1]


if __name__ == '__main__':
    qf = QuickUnion(5)
    assert qf.entities ==  [0,1,2,3,4]
    assert qf.tree_size == [1,1,1,1,1]
    qf.union(0,1)
    assert qf.entities ==  [0,0,2,3,4]
    assert qf.tree_size == [2,1,1,1,1]
    qf.union(3,4)
    assert qf.entities ==  [0,0,2,3,3]
    assert qf.tree_size == [2,1,1,2,1]
    qf.union(4,0)
    assert qf.entities ==  [3,0,2,3,3]
    assert qf.tree_size == [2,1,1,4,1]
    qf.union(2,4)
    assert qf.entities ==  [3,0,3,3,3]
    assert qf.tree_size == [2,1,1,5,1]
    assert qf.connected(4, 1)
    assert qf.connected(3, 2)
    print "Yay! \o/"
