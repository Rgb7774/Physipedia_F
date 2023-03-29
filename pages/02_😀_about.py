import streamlit as st 


st.header("About Me")
st.markdown('<p style="font-family:italic; color: cooper black; font-size: 20px;">Hay! My name is Chetan Katkar. Curruntly studing in MSc(phyiscs) in RJ clg. This app I have devloped hear is on purpose of project which i got on python class. Thanks to my sir and friends who help me to devlope it. I hope you like it. </p>',unsafe_allow_html=True)



bgcolor="#FA8072"
fontcolor="#ffffff"
html_temp = """
		<div style="background-color:{};padding:10px">
		<h1 style="color:{};text-align:center;">Thank You!! </h1>
		</div>
		"""
st.markdown(html_temp.format(bgcolor,fontcolor),unsafe_allow_html=True)
st.markdown("<div><p style='color:{}'>Hello Users. Welcome to Physipedia</p></div>".format(bgcolor),unsafe_allow_html=True)