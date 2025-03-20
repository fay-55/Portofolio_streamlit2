import streamlit as st

st.set_page_config(layout='wide')
st.title('Portfolio Saya')
st.header('Data Scientist')
st.sidebar.title('Navigasi Halaman')
page = st.sidebar.radio('Pilih halaman', ['Tentang saya', 
                                          'Dashboard', 'Prediction', 
                                          'Kontak'])

if page == 'Tentang saya':
    import aboutme
    aboutme.about_me()
elif page == 'Kontak':
    import kontak
    kontak.munculkan_kontak()
elif page == 'Dashboard':
    import Dashboard
    Dashboard.tampilan_dashboard()
elif page == 'Prediction':
    import prediksi
    
    # if st.button('Project A'):
       # prediksi.project1()

   # if st.button('Project B'):
       # prediksi.project2()