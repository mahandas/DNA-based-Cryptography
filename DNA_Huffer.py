from itertools import groupby
from heapq import *
import os

def huffman(input):

        codes = {}
        class Node(object):
                left = None
                right = None
                item = None
                weight = 0

                def __init__(self, i, w):
                        self.item = i
                        self.weight = w

                def setChildren(self, ln, rn):
                        self.left = ln
                        self.right = rn

                def __repr__(self):
                        return "%s - %s — %s - %s" % (self.item, self.weight, self.left, self.right)

                def __lt__(self, a):
                        return (self.weight, a.weight)
        def codeIt(s, node):
                if node.item:
                        if not s:
                                codes[node.item] = "0"
                        else:
                                codes[node.item] = s
                else:
                        codeIt(s+"0", node.left)
                        codeIt(s+"1", node.right)


        itemqueue =  [Node(a,len(list(b))) for a,b in groupby(sorted(input))]
        print(itemqueue)
        heapify(itemqueue)
        while len(itemqueue) > 1:
                l = heappop(itemqueue)
                r = heappop(itemqueue)
                n = Node(None, r.weight+l.weight)
                n.setChildren(l,r)
                heappush(itemqueue, n)

        codeIt("",itemqueue[0])
        return codes, "".join([codes[ai] for ai in input])

file = open('C:/Users/mahan.das/Desktop/DNA_data.txt',encoding='utf-8')
input = file.read()
value_input = huffman(input)
print(value_input)
dst="C:/Users/mahan.das/Desktop/DNA_huffed.txt"
if(os.path.isfile(dst)):
    os.remove(dst)
with open(dst, "a") as myDNAdata:
    myDNAdata.write(value_input[1])
