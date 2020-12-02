import os
import sys
import re

import unicodedata

def main():
    word = sys.argv[1]
    
    file_list = os.listdir("/home/keita/bof/unix/dict/word_net/data/")
    
    # print(file_list)

    w_id = []
    for f_name in file_list:
        if re.match('index\.',f_name):
            f = open(f'/home/keita/bof/unix/dict/word_net/data/{f_name}')
            for line in f:                
                content = f.readline()
                content = "<" + content
                # print(content)
                if f"<{word}%" in content:
                    mean_w = content
                    i = mean_w.split()[1]
                    w_id.append(i)                    
        else:
            pass

    if len(w_id) == 0:
        print(f'<"{word}" does not exits in WordNet or "{word}" is not noun or verb>')
        return 0
    
    mean_w=''
    for i in w_id:        
        for f_name in file_list:
            if re.match('data\.',f_name):
                f = open(f'/home/keita/bof/unix/dict/word_net/data/{f_name}')
                for line in f:                
                    content = f.readline()
                    content = "< " + content
                    if f'< {i}' in content:                 
                        w_list = content.split(" | ")
                        print(content.split(" ")[5])
                        print(f_name.split(".")[1],":",w_list[1])
        else:
            pass
        
    
if __name__ == "__main__":
    main()
