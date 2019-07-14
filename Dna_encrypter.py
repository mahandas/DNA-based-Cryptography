from itertools import groupby
from heapq import *
import os

dict_rc = {
  "A":"T","G":"C","T":"A","C":"G"
}

DNA_dict = {
  "0":{"A":"T","T":"G","G":"C","C":"A"},
  "1":{"A":"G","T":"C","G":"A","C":"T"}
}

IX = []
P = []
IX_dna = []
Data_fragments = []
fragments = []
fragment = []
temp_i = ""
fragments_i = []
ID = bin(176)[2:len(bin(176))]

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
        
        heapify(itemqueue)
        while len(itemqueue) > 1:
                l = heappop(itemqueue)
                r = heappop(itemqueue)
                n = Node(None, r.weight+l.weight)
                n.setChildren(l,r)
                heappush(itemqueue, n)

        codeIt("",itemqueue[0])
        return codes, "".join([codes[ai] for ai in input])
	


def apend_zeroes(temp_i, length):
  temp_i = bin(temp_i)
  temp_i = temp_i[2:len(temp_i)]
  while(len(temp_i) < length):
    temp_i = "0" + temp_i
  return temp_i

def final_appenders(fragment_val):
  if fragment_val.startswith('T'):
    fragment_val = 'A' + fragment_val
  elif fragment_val.startswith('A'):
    fragment_val = 'T' + fragment_val
  else:
    fragment_val = 'T' + fragment_val
    
  if fragment_val.endswith('C'):
    fragment_val =fragment_val + 'G'
  elif fragment_val.endswith('G'):
    fragment_val =fragment_val + 'C'
  else:
    fragment_val =fragment_val + 'C'

  return fragment_val

def DNA_Encoder(valuetopass,Start_DNA = "T"):
  temp_dna = Start_DNA
  for j in valuetopass:
    temp_dna = temp_dna + DNA_dict[j][Start_DNA]
    Start_DNA = DNA_dict[j][Start_DNA]
  return temp_dna[0:(len(temp_dna)-1)]




def fragmenting(var):
        for i in range(0, len(var), 5):
          fragments.append(var[i:i+10])

        for i in range(0, len(fragments)-1):
          if (i==0 or (i%2 ==0)):
            print('Fragment' + str(i) + ': ' + fragments[i])
            fragment.append(fragments[i])
          else:
            temp_s = ""
            for j in fragments[i]:
              temp_s = temp_s + dict_rc[j]
            print('Fragment' + str(i) + ': ' + temp_s)
            fragment.append(temp_s)
          #print(apend_zeroes(i, 12))
          fragments_i.append(apend_zeroes(i, 6))

        for i in range (0, len(fragments_i)):
          sumP = "0"
          for j in fragments_i[i]:
            if not (i==0 or (i%2 == 0 )):
              sumP = bin(int(sumP,2) + int(j,2))
          sumP = bin(int(sumP,2) + int(ID,2))
          P.append(sumP[2:len(sumP)])
          
        for i in range(0, len(fragments_i)):
          IX.append(str(ID) + str(fragments_i[i]) + str(P[i]))

        for i in range(0, len(IX)):
          IX_dna.append(DNA_Encoder(IX[i]))
        for i in range(0, len(fragment)):
          Data_fragments.append(final_appenders(fragment[i] + IX_dna[i]))

file = open('DNA_input.txt',encoding='utf-8')
input = file.read()
print(input)
value_input = huffman(input)
n = len(value_input[len(value_input)-1])
S2 = apend_zeroes(n, 10)
S3 = "0"
S4 = value_input[len(value_input)-1] + S3 + S2
while(len(S4)%5 != 0):
        S3 = S3 + "0"
        S4 = value_input[len(value_input)-1] + S3 + S2

fragmenting(DNA_Encoder(S4))

dst="DNA_output.txt"
if(os.path.isfile(dst)):
    os.remove(dst)
  
with open(dst, "a") as myDNAdata:
        for i in Data_fragments:
                myDNAdata.write(i)
  
  
print("Data encoding into DNA complete.")
  
