import streamlit as st

st.set_page_config(layout='wide')

st.title('Panduan Berakhlak Pegawai BPS')
with st.container(border=True):
  st.header('Harmonis', divider='green')
  st.subheader('Saling peduli dan menghargai perbedaan')
  
with st.expander('Menghargai setiap orang apapun latar belakangnya'):
  st.success('Menghargai setiap orang apapun latar belakangnya')
  st.write('1. Menerima saran dan masukan dari siapapun tanpa melihat latar belakang jabatan, serta mengutamakan musyawarah mufakat')
  st.write('2. Memberikan apresiasi terhadap hasil kerja anggota tim ataupun rekan kerja yang lain')
  st.write('3. Menjaga sikap dan berlaku sopan santun terhadap siapa pun dalam pergaulan sosial baik di dalam kantor maupun di lingkungan sekitar, termasuk di media sosial')

with st.expander('Suka menolong orang lain'):
  st.success('Suka menolong orang lain')
  st.write('1. Saling membantu dalam penyelesaian pekerjaan dan memberikan solusi atas kesulitan rekan kerja yang lain')
  st.write('2. Menunjukkan kepedulian dan empati terhadap rekan kerja, atasan, atau bawahan ketika mengalami kesulitan')
  st.write('3. Memberikan bantuan materi maupun non materi bagi rekan kerja yang terkena musibah dan kesulitan lainnya.')

with st.expander('Membangun lingkungan kerja yang kondusif'):
  st.success('Membangun lingkungan kerja yang kondusif')
  st.write('1. Mengembangkan sikap toleransi dan menghargai keanekaragaman budaya serta keyakinan dalam kehidupan sehari-hari baik di lingkungan kerja ataupun dalam bermasyarakat;')
  st.write('2. Menjaga hubungan baik dengan rekan kerja, atasan, bawahan dan stakeholders dengan menerapkan senyum, salam, dan sapa')
  st.write('3. Membuat suasana kantor yang nyaman.')
