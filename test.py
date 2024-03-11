import pandas as pd
import re
import numpy as np
def readInput(start,end):
    df = pd.read_excel("tmp.xlsx")
    print(df.values.shape[0])
    if end - start +1 > df.values.shape[0]:
        end = df.values.shape[0]
        print(end)
    infos = []
    for i in range(start,end+1):
        data = df[df["ID"] ==   (i)]
        if str(data['content']).strip() == "":
            continue
        info = {}
        content = str(data['content'].values[0])
        info['content'] = content
        tag = re.split(r'[, \s \n]+',str(data['TAG'].values[0]))
        info['tag'] = tag if tag[0] != 'nan' else ""
        hashtag = re.split(r'[,\s\n]+',str(data['HASHTAG'].values[0]))
        info['hashtag'] = hashtag if hashtag[0] != 'nan' else ""
        image = (data['IMAGE'].values).tolist()
        info['image'] = image[0] if str(image[0]) != 'nan' else ""
        infos.append(info)
    return infos


print(readInput(1,4))        
        
