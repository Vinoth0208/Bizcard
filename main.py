import sys

import pandas as pd

import DataExtraction
from Modify import modify, delete
from sqlmigration import migrate

sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\Bizcard\venv\Lib\site-packages')
import os.path
import easyocr
from matplotlib import pyplot as plt
from DataExtraction import dataextract
import cv2
import streamlit_option_menu
import streamlit as st

st.set_page_config(layout="wide",page_title="Bizcard_EasyOCR")


selected = streamlit_option_menu.option_menu("Menu", ["About", "Upload", "DataExtraction", 'Modify', 'Contact'],
                                                 icons=["exclamation-circle","upload","clipboard","pencil-square", 'telephone-forward' ],
                                                 menu_icon= "menu-button-wide",
                                                 default_index=0,
                                                 orientation="horizontal",
                                                 styles={"nav-link": {"font-size": "15px", "text-align": "centre",  "--hover-color": "#d1798e"},
                        "nav-link-selected": {"background-color": "#b30e35"}})
if selected=='About':
    st.title(':blue[Project Title: BizCardX: Extracting Business Card Data with OCR]')
    st.header(':red[Technologies used:]')
    st.subheader(':green[Python, EasyOCR,streamlit GUI, SQL, Data Extraction]')
    st.markdown("Welcome to our amazing application that can extract text from images, process it, and store it securely in our database. With this powerful tool, you can easily convert images containing text into a machine-readable format, making it easy to access and manipulate the information.")
    st.text('''Here's how our application works:

Image Import: Start by uploading any image or multiple images containing text directly from your computer or mobile device. 
Our application supports various image formats such as JPEG, PNG.

Text Extraction: Once the images are uploaded, our advanced optical character recognition (OCR) technology comes into play. 
It scans the images, identifies the text elements, and accurately extracts the text from each image.

Text Processing: The extracted text goes through a series of processing steps to ensure accuracy and improve readability.

Data Storage: Once the text is extracted and processed, it is securely stored in our robust and reliable database.''')
if selected=='Upload':
    st.write("")
    st.write("")
    st.write("")
    imageuploaded=st.file_uploader('Select a Bizcard image to upload', type=['png','jpg','gif'], accept_multiple_files=True)
    for i in imageuploaded:
        if i:
            with open(os.path.join(r'C:\Users\Vinoth\PycharmProjects\Bizcard\images',i.name),'wb') as imgfile:
                imgfile.write(i.getbuffer())
            st.markdown("     ")
            st.markdown("    ")
            st.success('File Upload Success')

        def preview(image, result):
            for (boundingbox, text, probablity) in result:
                (topleft, topright, bottomright, bottomleft) = boundingbox
                topleft = (int(topleft[0]), int(topleft[1]))
                topright = (int(topright[0]), int(topright[1]))
                bottomright = (int(bottomright[0]), int(bottomright[1]))
                bottomleft = (int(bottomleft[0]), int(bottomleft[1]))
                cv2.rectangle(image, topleft, bottomright, (252, 186, 3), 1)
                cv2.putText(image, text, (bottomleft[0], bottomleft[1]),
                            cv2.QT_FONT_NORMAL, 0.6, (3, 252, 119), 2)
            plt.rcParams['figure.figsize'] = (15, 15)
            plt.axis('off')
            plt.imshow(image)


        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.markdown("     ")
            st.markdown("     ")
            st.markdown("### You have uploaded the card")
            st.image(i)

        with col2:
            st.markdown("    ")
            st.markdown("    ")
            with st.spinner("Please wait processing image..."):
                imageread = easyocr.Reader(['en'])
                st.set_option('deprecation.showPyplotGlobalUse', False)
                saved_img = os.getcwd() + "\\" + "images" + "\\" + i.name
                image = cv2.imread(saved_img)
                result = imageread.readtext(saved_img)
                st.markdown("### Image Processed and Data Extracted")
                st.pyplot(preview(image, result))

if selected=='DataExtraction':
    if os.listdir(r'C:\Users\Vinoth\PycharmProjects\Bizcard\images') is not None:
        data=dataextract()
        # st.write(data)
        state = st.button(":orange[Upload to MYSQL]")
        if state:
            migrate(data.values.tolist())
if selected=='Modify':
    tabselected = streamlit_option_menu.option_menu("", ["Update",  'Delete'],
                                                 icons=["pencil-square", "trash"],
                                                 menu_icon= "menu-button",
                                                 default_index=0,
                                                 orientation="horizontal",
                                                 styles={"nav-link": {"font-size": "15px", "text-align": "centre",
                                                                      "--hover-color": "#d1798e"},
                                                         "nav-link-selected": {"background-color": "#b30e35"}})

    if tabselected=='Update':
        modify()
    if tabselected=='Delete':
        delete()
if selected == 'Contact':
    st.title("Name: :orange[Vinoth Palanivel]")
    st.subheader("Degree: :orange[Bachelor of Engineering in Electrical and Electronics Engineering]")
    st.subheader("E-mail: :orange[vinothchennai97@gmail.com]")
    st.subheader("Mobile: :orange[7904197698 or 9677112815]")
    st.subheader("Linkedin: :orange[https://www.linkedin.com/in/vinoth-palanivel-265293211/]")
    st.subheader("Github: :orange[https://github.com/Vinoth0208/]")
    st.subheader("Project links:")
    st.subheader("1. https://github.com/Vinoth0208/Youtube_Project_For_DataScience")
    st.subheader("2. https://github.com/Vinoth0208/PhonepePulse")

