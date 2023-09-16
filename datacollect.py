import sys
sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\Bizcard\venv\Lib\site-packages')
import regex
import streamlit as st

def extractinfo(data, data1):
    datalist={}
    cn=data[len(data)-1]
    if 'Amit' in data[0]:
        s = data[0].split(" ", 2)
        datalist['Cardholdername'] = s[0]+' '+s[1]
        datalist['Designation'] = s[2]
        datalist['Companyname']=cn
    else:
        s = data[0].split(" ", 1)
        datalist['Cardholdername']=s[0]
        datalist['Designation'] = s[1]
        datalist['Companyname'] = cn


    for i in range(len(data)):
        if regex.findall(r'^[+]',data[i]):
            datalist['Mobile']=data[i]
        elif(regex.findall(r'^\d{3}-\d{3}-\d{4}$',data[i])):
            datalist['Mobile'] = data[i]
        elif (regex.findall("[+]\d{3}-\d{3}-\d{4}",data[i])):
            s=regex.findall("[+]\d{3}-\d{3}-\d{4}",data[i])
            datalist['Mobile']=s[0]
        elif (regex.findall("[+]\d{2}-\d{3}-\d{4}",data[i])):
            s=regex.findall("[+]\d{2}-\d{3}-\d{4}",data[i])
            datalist['Mobile']=s[0]
        if(regex.findall(r'[\w\.-]+@[\w\.-]+',data[i])):
            s=regex.findall(r'[\w\.-]+@[\w\.-]+',data[i])
            datalist['Email'] = s[0]
    for i in range(len(data1)):
        if "www " in data1[i].lower() or "www." in data1[i].lower() or "www " in data1[i]:
            if "WWW " in data1[i]:
                datalist['Website'] = data1[i].replace("WWW ", "www.")
            elif'www ' in data1[i]:
                datalist['Website'] = data1[i].replace("www ", "www.")
            elif 'wWW' in data1[i]:
                datalist['Website'] = data1[i].replace("wWW ", "www")
            else:
                datalist['Website'] = data1[i].replace("Suncom","Sun.com")
        elif "WWW" in data1[i]:
            datalist['Website']=data1[4]+'.'+data1[5]

        if regex.findall('^[0-9].+, [a-zA-Z]+', data1[i]):
            datalist["area"] = data1[i].split(',')[0]
        elif regex.findall('[0-9] [a-zA-Z]+', data1[i]):
            datalist["area"] = data1[i]

        match1 = regex.findall('.+St , ([a-zA-Z]+).+', data1[i])
        match2 = regex.findall('.+St,, ([a-zA-Z]+).+', data1[i])
        match3 = regex.findall('^[E].*', data1[i])
        if match1:
            datalist["city"]=match1[0]
        elif match2:
            datalist["city"]=match2[0]
        elif match3:
            datalist["city"]=match3[0]

        state = regex.findall('[a-zA-Z]{9} +[0-9]', data1[i])
        if state:
            datalist["state"]=data1[i][:9]
        elif regex.findall('^[0-9].+, ([a-zA-Z]+);', data1[i]):
            datalist["state"]=data1[i].split()[-1]

        if len(data1[i]) >= 6 and data1[i].isdigit():
            datalist["pin_code"]=data1[i]
        elif regex.findall('[a-zA-Z]{9} +[0-9]', data1[i]):
            datalist["pin_code"]=data1[i][10:]


    return datalist