#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSentences' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY wordSet
#  2. STRING_ARRAY sentences
#

def countSentences(wordSet, sentences):
    from collections import defaultdict
    # Write your code here
    word_dict = {} #defaultdict(list)
    def detect(w1, w2): 
        l1 = [c for c in w1]
        l2 = [c for c in w2]
        for i, c in enumerate(l1): 
            if c in l2: 
                idx = l2.index(c)
                l2[idx] = ""
            else: 
                return False
            if len("".join(l2)) == 0 and i < len(l1) - 1:
                return False 
        if len("".join(l2)) == 0:
            return True 
        return False
    
    for w in wordSet: 
        inset = False
        for k, v in word_dict.items(): 
            if detect(k, w): 
                word_dict[k] += 1 
                inset = True
                break
        if inset == False:
            word_dict[w] = 1
    print(word_dict)

    ret = []
    for s in sentences: 
        tmp = 1 
        for w in s.split(): 
            for k, v in word_dict.items(): 
                if detect(k, w): 
                    tmp *= v
                    break
        ret += [tmp]

    return ret

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # wordSet_count = int(input().strip())

    wordSet = ['star', 'tars', 
'stay',
'tay',
'seed',
'dees',
'eesd',
'rast',
'date',
'ate']

    # for _ in range(wordSet_count):
    #     wordSet_item = input()
    #     wordSet.append(wordSet_item)

    # sentences_count = int(input().strip())

    sentences = ['ate date stay']

    # for _ in range(sentences_count):
    #     sentences_item = input()
    #     sentences.append(sentences_item)

    result = countSentences(wordSet, sentences)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
