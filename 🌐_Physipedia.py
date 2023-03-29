import streamlit as st

st.set_page_config(page_title="Physipedia", page_icon="🌐", layout="wide", initial_sidebar_state="expanded")
st.markdown(
        """<style>
        .css-1rs6os.edgvbvh3
        {
                visibility: hidden;
        }
        
        .css-10pw50.egzxvld1
        {
                visibility: visible;
        }
        footer:after{
                content:'Made by Chetan';
                display: block;
                position: relative;
                color:tomato;
                pedding:20px;
                top:3px;
        }
        </style>""",unsafe_allow_html=True
)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com" target="_blank">Data Professor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#st.markdown("<h1 style ='text-align: center;' >PHYSIPEDIA</h1>", unsafe_allow_html=True)
bgcolor="#3498DB"
fontcolor="#ffffff"
html_temp = """
		<div style="background-color:{};padding:10px">
		<h2 style="color:{};text-align:center;">PHYSIPEDIA </h2>
		</div>
		"""
st.markdown(html_temp.format(bgcolor,fontcolor),unsafe_allow_html=True)
st.markdown("<div><p style='color:{}'>Hello Users. Welcome to Physipedia</p></div>".format(bgcolor),unsafe_allow_html=True)

st.markdown("<h2 style ='text-align: center;' >Welcome to Physipedia!!</h2>", unsafe_allow_html=True)
col1,col2 = st.columns(2)
signin_txt=col1.text('If you already have account please SignIn')
signin= col1.button('SignIn')
signup_txt=col2.text('If you don\'t have an account please signup')
signup= col2.button('SignUp')
if(signin):
        with st.form('login'):
                col3,col4 =st.columns(2)
                login=col3.text_input("Enter Your Username")
                if login =="":
                        st.warning("Please field above fields")
                passw= col4.text_input('Enter Your Password')
                if passw == "":
                        st.warning("Please field above fields")
                elif login !=""and passw!="":
                        st.warning("succecfull")
                btn1=st.form_submit_button('Submit')
                
elif(signup):
        with st.form("sign"):
                col5,col6 = st.columns(2)
                f_name=col5.text_input("First name")
                l_name=col6.text_input("Last name")
                passw1= col5.text_input("Enter a password")
                passw2= col6.text_input("Confirm Password")
                btn2=st.form_submit_button('Submit')
a =st.text_input('search your topic hear')
b= st.button('search')


tab1, tab2, tab3 ,tab4 ,tab5 = st.tabs(["Wikipedia", "Britaniaca", "Citiizendium", "Conservapedia","Encylopedia"])
with tab1:
        st.subheader('Wikipedia')
        st.markdown(f'<iframe src="https://en.wikipedia.org/wiki/{a}" style = "width:750px;height:500px"></iframe>',
        unsafe_allow_html=True)
with tab2:
        st.subheader('Encyclopedia of Britanica')
        st.markdown(f'<iframe src="https://www.britannica.com/search?query={a}" style = "width:750px;height:500px"></iframe>',
        unsafe_allow_html=True)
with tab3:
        st.subheader('Citizendium')
        st.markdown(f'<iframe src="https://citizendium.org/wiki/{a}" style="width:750px;height:500px"></iframe>',
        unsafe_allow_html=True)
with tab4:
        st.subheader('Conservapedia')
        st.markdown(f'<iframe src="https://www.conservapedia.com/{a}" style="width:750px;height:500px"></iframe>',
        unsafe_allow_html=True)
with tab5:
        st.subheader("Encyclopedia")
        st.markdown(f'<iframe src="https://www.encyclopedia.com/gsearch?q={a}" style="width:750px;height:500px"></iframe>', unsafe_allow_html=True)


