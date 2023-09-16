import os

import mysql.connector
import streamlit as st
from PIL import Image
import easyocr



def migrate(data):
    path = r'C:\Users\Vinoth\PycharmProjects\Bizcard\images'
    files = os.listdir(path)
    for i in range(len(data)):
        imageread = easyocr.Reader(['en'])
        def binary(file):
            with open(file, 'rb') as file:
                binaryData = file.read()
            return binaryData
        data[i].append(binary(path+'\\'+files[i]))

    connector =mysql.connector.Connect(host="localhost",user="root",password="root")
    cursor=connector.cursor()
    cursor.execute("CREATE DATABASE if not exists Bizcard")
    cursor.execute("use Bizcard")
    cursor.execute("Create Table if not exists Cardinfo(cardholdername varchar(1000),designation varchar(255),companyname varchar(255),mobile varchar(255),email varchar(255),website varchar(255),area varchar(255), city varchar(255),state varchar(255),pin_code varchar(255), image LONGBLOB)")
    for i in data:
        tp=tuple(i)
        sql = "insert into Cardinfo(cardholdername,designation,companyname, mobile,email,website,area,city,state,pin_code,image)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tp)
    connector.commit()
    st.success("Data Migrated to MYSQL")
