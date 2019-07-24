from pypinyin import pinyin, lazy_pinyin, Style
import pickle
import re
import time
import os
with open('splitdata/seg_lists_0.pkl','rb') as f:
    data = pickle.load(f)

CACHE_DIR = './.ch_cache'
    

for d in data:
    for word in d:
        pass
        parseResult = pinyin(word, style=Style.INITIALS, strict=False)
        parseResultHead = parseResult[0][0]
        parseResultHead = re.sub(r"[^A-Za-z|0-9]+", '', parseResultHead) #僅保留英文與數字
        if(len(parseResultHead)>1): #只取頭
            parseResultHead = parseResultHead[0]
        if(parseResultHead == ''):
            parseResultHead = '._others'
        else:
            pass
        
        # 檢查資料夾存在
        if(not os.path.isdir(CACHE_DIR + parseResultHead)):
            os.mkdir(CACHE_DIR + parseResultHead)
        
        #
        word = word + '.pkl'
        with open(CACHE_DIR + parseResultHead + word , 'wb') as f:
            pickle.dump(word,f)
        
