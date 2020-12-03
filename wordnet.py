import os
import sys
import re

import unicodedata

def get_line_from_id(id):
        
    file_list = os.listdir("/home/keita/bof/unix/dict/word_net/data/")
    lines = []
    for f_name in file_list:
        if re.match('data\.',f_name):
            f = open(f'/home/keita/bof/unix/dict/word_net/data/{f_name}')
            for content in f:
                content = "< " + content
                if f"< {id}" in content:
                    lines.append(content)
        else:
            pass
                    

    return lines

def get_mean_from_line(line):
    word = []
    relate_word = []
    w_mean = line.split(" | ")
    w_list = w_mean[0].split(" ")
    parts = w_list[3]
    mean = w_mean[1]
    for w in w_list:
        r = []
        if re.match('[a-z]{2,100}',w):
            word.append(w)            
        if re.match('[0-9]{8}',w):
            i = w_list.index(w)
            r.append(w_list[i-1])
            r.append(w)
            relate_word.append(r)
            
    return word,parts,relate_word,mean

def judge_words(relate_word):
    hyponym = []
    hypernym = []
    relate = []
    for r in relate_word:
        if r[0] == "<":
            pass
        elif r[0] == '@':
            hyponym.append(r[1])
        elif r[0] == '~':
            hypernym.append(r[1])
        elif r[0] == '+':
            relate.append(r[1])

    return hyponym, hypernym, relate


def main():
    word = sys.argv[1]
    
    file_list = os.listdir("/home/keita/bof/unix/dict/word_net/data/")
    
    # print(file_list)

    w_id = []
    for f_name in file_list:
        if re.match('index\.',f_name):
            f = open(f'/home/keita/bof/unix/dict/word_net/data/{f_name}')
            for content in f:                
                content = "<" + content
                # print(content)
                if f"<{word} " in content:
                    mean_w = content
                    id_contents = mean_w.split()
                    for i in id_contents:
                        if re.match('[0-9]{8}',i):
                            w_id.append(i)                    
        else:
            pass
    print(w_id)
    if len(w_id) == 0:
        print(f'<"{word}" does not exits in WordNet or "{word}" is not noun or verb>')
        return 0
    
    mean_w=''
    count = 1
    for i in w_id:
        lines = get_line_from_id(i)
        for line in lines:
            word,parts,relate_word,mean = get_mean_from_line(line)
            # print(relate_word)
            print("*", count,parts,word)
            print(mean)
            count += 1
            for i_r in relate_word:
                hyponym, hypernym, relate = judge_words(relate_word)
            for hypo in hyponym:
                print("** hyponym words" )
                lines_r = get_line_from_id(hypo)
                for line_r in lines_r:
                    word_r,parts_r,relate_word_r,mean_r = get_mean_from_line(line_r)
                    print(parts_r,word_r)
                    print(mean_r)

            for hyper in hypernym:
                print("** hypernym words" )
                lines_r = get_line_from_id(hyper)
                for line_r in lines_r:
                    word_r,parts_r,relate_word_r,mean_r = get_mean_from_line(line_r)
                    print(parts_r,word_r)
                    print(mean_r)

            for rel in relate:
                print("** derivationally related form" )
                lines_r = get_line_from_id(rel)
                for line_r in lines_r:
                    word_r,parts_r,relate_word_r,mean_r = get_mean_from_line(line_r)
                    print(parts_r,word_r)
                    print(mean_r)

            
                    
if __name__ == "__main__":
    main()
