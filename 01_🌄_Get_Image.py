import streamlit as st 
import requests
from bs4 import BeautifulSoup
import webbrowser
st.set_page_config(page_title="Get Image", page_icon="🌄", layout="wide", initial_sidebar_state="expanded")

bgcolor="#F7DC6F"
fontcolor="#452B05"
html_temp = """
		<div style="background-color:{};padding:10px">
		<h2 style="color:{};text-align:center;">GET IMAGE </h2>
		</div>
		"""
st.markdown(html_temp.format(bgcolor,fontcolor),unsafe_allow_html=True)
st.markdown("<div><p style='color:{}'>Hello Users. Welcome to GET IMAGE</p></div>".format(fontcolor),unsafe_allow_html=True)
st.markdown("<div><p style='color:{}'>Hear you will get roylty free images</p></div>".format(fontcolor),unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> Search for Images </h2>", unsafe_allow_html=True)


with st.form("Search"):
    keyword=st.text_input("Enter your keyword")
    search = st.form_submit_button("Search")
placeholder=st.empty()
if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, "html.parser")
    rows=soup.find_all("div", class_="ripi6")
    col10,col11=placeholder.columns(2)
    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("img")
            list=img["srcset"].split("?")
            anchor=figures[i].find("a",class_="rEAWd")
            if i == 0:
                col10.image(list[0])
                btn=col10.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
            else:
                col11.image(list[0])
                btn=col11.button("Download",key=str(index)+str(i))
                if btn :
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])
