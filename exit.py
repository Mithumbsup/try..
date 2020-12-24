from bs4 import BeautifulSoup
import requests
import urllib.parse as rep
import csv 
import pandas as pd 
import numpy as np
import time 

def makeUrl(base_url,target):
    quote = rep.quote_plus(target)
    url = base_url + quote
    # print(url)
    resp = requests.get(url)  
    return resp


def extract_data(target):
    base = "https://namu.wiki/w/"
    res1 = makeUrl(base,target)
    soup = BeautifulSoup(res1.text,"html.parser")   
    searchList = soup.select("div > div.wiki-paragraph")
    if not searchList :
        pass 
    else :
        searchList = [ newData.get_text() for newData in searchList]
    
    imagesList = soup.findAll('img')
    # print(images)
    if not imagesList :
        pass
    else :
        imagesList = [ div['src'] for i, div in enumerate(imagesList,1)]
    
    # print(imagesList)
    return searchList , imagesList


# 검색데이터 로드
filePath = "C:\\Users\\mis\\Desktop\\crawling\\csv\\"
fileName = "cropName.csv"
df = pd.read_csv(filePath+fileName)
columns = df.columns 
df[["DESCRIPTION","IMAGEFILE"]] = df[["DESCRIPTION","IMAGEFILE"]].astype(str)

for idx_num in range(len(df)):
    # print(bool(type(idx_num/10)== float))
    if type(idx_num/10) == int:
        time.sleep(10)
        continue
    else :
        idx = df.iloc[idx_num] #한행씩 불러오기
        target = idx['CROPNAME'] 
        newData = extract_data(target)[0]
        if not newData:
            pass 
        elif len(newData) > 2 :
            df.at[idx_num, "DESCRIPTION"] = newData[2] 
        else: 
            # print(len(newData))
            df.at[idx_num, "DESCRIPTION"] = newData[1] 
        
        
        imgSrc = extract_data(target)[1]
        df.at[idx_num, "IMAGEFILE"] = imgSrc
        print(len(imgSrc))
        # print(df.dtypes)
        # if not imgSrc:
        #     pass 
        # elif len(imgSrc) > 3 :
        #     df.at[idx_num, "IMAGEFILE"] = imgSrc[2] 
        # else: 
        #     print(len(imgSrc))
        #     df.at[idx_num, "IMAGEFILE"] = imgSrc[len(imgSrc)-1]

save_csv = df.to_csv(filePath + "result.csv",
                    index=False,
                    encoding = "utf-8"
                    )
                        
# print(df["IMAGEFILE"].head())
