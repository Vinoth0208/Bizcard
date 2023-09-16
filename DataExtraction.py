import os
import sys
import pandas as pd
from datacollect import extractinfo
sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\Bizcard\venv\Lib\site-packages')
import streamlit as st
import easyocr



def dataextract():
    data = {}
    data1={}
    st.write("")
    st.write("")
    st.write("")
    path = r'C:\Users\Vinoth\PycharmProjects\Bizcard\images'
    files = os.listdir(path)

    for i in files:
        imageread = easyocr.Reader(['en'])
        text = imageread.readtext(r'C:\Users\Vinoth\PycharmProjects\Bizcard\images' + '\\' + i, detail=0,paragraph=True)
        data[i] = text
        text1 = imageread.readtext(r'C:\Users\Vinoth\PycharmProjects\Bizcard\images' + '\\' + i, detail=0)
        data1[i]=text1
    datas=[]
    for j in data:
        info=extractinfo(data[j], data1[j])
        ddf=pd.DataFrame.from_dict(info, orient="index")
        datas.append(ddf.transpose())
    if not len(datas)==0:
        result=pd.concat(datas, ignore_index=True)
        st.header("Extracted Data:")
        st.write(result)
        return result
    else:
        return st.error("Please upload a file to extract data")



