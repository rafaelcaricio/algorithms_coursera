#!/usr/bin/env python


class QuickFind(object):
    def __init__(self, n):
        self.entities = []
        for i in xrange(n):
            self.entities.append(i)

    def connected(self, p1, p2):
        return self.entities[p1] == self.entities[p2]

    def union(self, p1, p2):
        group_of_p1 = self.entities[p1]
        group_of_p2 = self.entities[p2]
        for i, group in enumerate(self.entities):
            if group_of_p2 == group:
                self.entities[i] = group_of_p1


if __name__ == '__main__':
    qf = QuickFind(5)
    assert qf.entities == [0,1,2,3,4]
    qf.union(0,1)
    assert qf.entities == [0,0,2,3,4]
    qf.union(3,4)
    assert qf.entities == [0,0,2,3,3]
    qf.union(4,0)
    assert qf.entities == [3,3,2,3,3]
    assert qf.connected(4, 1)
    print "Yay! \o/"
