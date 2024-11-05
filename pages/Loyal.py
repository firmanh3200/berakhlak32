import streamlit as st

st.set_page_config(layout='wide')

st.title('Panduan Berakhlak Pegawai BPS')
with st.container(border=True):
  st.header('Loyal', divider='green')
  st.subheader('Berdedikasi dan mengutamakan kepentingan Bangsa dan Negara')
  
with st.expander('Memegang teguh ideologi Pancasila, Undang-Undang Dasar Negara Republik Indonesia tahun 1945, setia kepada Negara Kesatuan Republik Indonesia serta pemerintahan yang sah'):
  st.success('Memegang teguh ideologi Pancasila, Undang-Undang Dasar Negara Republik Indonesia tahun 1945, setia kepada Negara Kesatuan Republik Indonesia serta pemerintahan yang sah')
  st.write('1. Menghayati dan mengamalkan nilai-nilai Pancasila dan Undang-Undang Dasar dalam kehidupan sehari-hari (di rumah, kantor, dan aktivitas sosial);')
  st.write('2. Setia dan taat kepada Negara Kesatuan Republik Indonesia; dan')
  st.write('3. Menjaga kehomatan dan kerahasiaan bangsa dan negara Indonesia dimanapun berada.')

with st.expander('Menjaga nama baik sesama ASN, pimpinan, instansi, dan negara'):
  st.success('Menjaga nama baik sesama ASN, pimpinan, instansi, dan negara')
  st.write('1. Menjadi contoh keteladanan yang baik (role model) dalam masyarakat')
  st.write('2. Menaati kode etik ASN dan peraturan yang berlaku dimanapun berada serta menjaga nama baik organisasi')
  st.write('3. Bijak dalam melakukan aktivitas di sosial media.')

with st.expander('Menjaga rahasia jabatan dan negara'):
  st.success('Menjaga rahasia jabatan dan negara')
  st.write('1. Memegang teguh rahasia jabatan dan negara;')
  st.write('2. Bersikap amanah')
  st.write('3. Berhati-hati dalam berbicara dan bersikap.')
