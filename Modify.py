import mysql
import streamlit as st


def modify():
    connector = mysql.connector.Connect(host="localhost", user="root", password="root")
    cursor = connector.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    database_exists = False
    for database in databases:
        if 'bizcard' in database:
            database_exists = True
            break
    if not database_exists:
        st.error('Please upload a file to create database')
    else:
        cursor.execute("use Bizcard")
        cursor.execute("select cardholdername from Cardinfo")
        opt=[]
        for i in cursor.fetchall():
            opt.append(i[0])
        tp=tuple(opt)
        selected=st.selectbox('Select a Card to modify', tp)
        cursor.execute(f"select * from Cardinfo where cardholdername ='{selected}'")
        datalist=cursor.fetchone()
        st.header("Make your changes and hit save button")
        cardholdername=st.text_input("Card Holder",datalist[0])
        designation=st.text_input("designation", datalist[1])
        companyname=st.text_input("companyname", datalist[2])
        mobile=st.text_input("mobile", datalist[3])
        email=st.text_input("emailr", datalist[4])
        website=st.text_input("website", datalist[5])
        area=st.text_input("area", datalist[6])
        city=st.text_input("city", datalist[7])
        state=st.text_input("state", datalist[8])
        pin_code=st.text_input("pin_code", datalist[9])
        save=st.button("Save")
        if save:
            cursor.execute("""
            UPDATE Cardinfo SET 
            cardholdername=%s,
            designation=%s,
            companyname=%s,
            mobile=%s,
            email=%s,
            website=%s,
            area=%s,
            city=%s,
            state=%s,
            pin_code=%s
            WHERE cardholdername=%s""", (cardholdername, designation, companyname, mobile, email, website, area, city, state, pin_code,selected))
            connector.commit()
            st.success("Information updated in database successfully.")
def delete():
    connector = mysql.connector.Connect(host="localhost", user="root", password="root")
    cursor = connector.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    database_exists = False
    for database in databases:
        if 'bizcard' in database:
            database_exists = True
            break
    if not database_exists:
        st.error('Please upload a file to create database')
    else:
        cursor.execute("use Bizcard")
        cursor.execute("select cardholdername from Cardinfo")
        opt = []
        for i in cursor.fetchall():
            opt.append(i[0])
        tp = tuple(opt)
        selected = st.selectbox('Select a Card to modify', tp)
        st.write(f"### You have selected :green[{selected}'s] card to delete")
        st.write("#### Proceed to delete this card?")
        if st.button("Yes Delete Business Card"):
            cursor.execute(f"DELETE FROM Cardinfo WHERE cardholdername='{selected}'")
            connector.commit()
            st.success("Business card information deleted from database.")