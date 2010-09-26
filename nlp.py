#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#author:         rex
#blog:           http://iregex.org
#filename        x.py
#created:        2010-09-26 19:15

import re

regex=re.compile(r"(?x) (?: [\w-]+  | [\x80-\xff]{3} )")

def init_wordslist(fn="./words.txt"):
    f=open(fn)
    lines=sorted(f.readlines())
    f.close()
    return lines

def words_2_trie(wordslist):
    d={}
    for word in wordslist: 
        ref=d
        chars=regex.findall(word)
        for char in chars:
            ref[char]=ref.has_key(char) and ref[char] or {}
            ref=ref[char]
        ref['']=1
    return d

def search_in_trie(chars, trie):
    ref=trie
    index=0
    for char in chars:
        if ref.has_key(char):
            print char,
            ref=ref[char] 
            index+=1
        else:
            if index==0:
                index=1
                print char, 
            print '*',
            try:
                chars=chars[index:]
                search_in_trie(chars, trie)
            except:
                pass
            break

words=init_wordslist()
trie=words_2_trie(words)
string="很美观对不对奇妙的是对于第一条字串它生成的结构是这样的；对于新插入的第二条，第三条……第N条字串，它不是另起炉炉灶，而是萧规曹随，见缝插针，充分利用前面已经成生的数据结构。这要归功于Hash/Dictionary这种数据结构的特点。看一下针对于foobar foobah fooxar foozap fooza 完全插入后的效果 理性爱国 性爱好神奇 我爱正则表达式"
chars=regex.findall(string)
search_in_trie(chars, trie)








