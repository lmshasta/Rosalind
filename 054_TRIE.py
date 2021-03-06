#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Introduction to Pattern Matching
Rosalind ID: TRIE
Rosalind #: 054
URL: http://rosalind.info/problems/trie/
'''

from itertools import count


class NumberedTrie(object):
    def __init__(self):
        self.counter = count(start=1)
        self.root = [next(self.counter), {}]

    def insert(self, bp):
        node = self.root
        for ch in bp:
            if ch not in node[1]:
                node[1][ch] = [next(self.counter), {}]
            node = node[1][ch]


def problem(bps):
    trie = NumberedTrie()
    for bp in bps:
        trie.insert(bp)
    return trie.root


def format(node):
    for ch, node2 in node[1].iteritems():
        print node[0], node2[0], ch
        format(node2)


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open("data/rosalind_trie.txt").readlines()
    dataset = [l.strip() for l in dataset if l.strip()]
    format(problem(dataset))
