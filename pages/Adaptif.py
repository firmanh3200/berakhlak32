import streamlit as st

st.set_page_config(layout='wide')

st.title('Panduan Berakhlak Pegawai BPS')
with st.container(border=True):
  st.header('Adaptif', divider='green')
  st.subheader('Terus berinovasi dan antusias dalam menggerakkan serta menghadapi perubahan')
  
with st.expander('Cepat menyesuaikan diri menghadapi perubahan'):
  st.success('Memegang teguh ideologi Pancasila, Undang-Undang Dasar Negara Republik Indonesia tahun 1945, setia kepada Negara Kesatuan Republik Indonesia serta pemerintahan yang sah')
  st.write('1. Cepat beradaptasi terhadap tuntutan perubahan dalam organisasi')
  st.write('2. Bersikap agile dan sigap menanggapi perubahan yang terjadi')
  st.write('3. Segera mengubah pola pikir dan cara kerja sesuai tuntutan perubahan.')

with st.expander('Terus berinovasi dan mengembangkan kreativitas'):
  st.success('Terus berinovasi dan mengembangkan kreativitas')
  st.write('1. Tidak terpaku pada pola lama dan berani mencoba hal baru untuk mendapatkan hasil kerja yang lebih baik;')
  st.write('2. Mengembangkan ide/cara baru dalam menyelesaikan tugas/pekerjaan agar lebih efektif dan efisien; dan')
  st.write('3. Memanfaatkan berbagai media dalam mengembangkan kreativitas.')

with st.expander('Bertindak proaktif'):
  st.success('Bertindak proaktif')
  st.write('1. Secara mandiri mampu berkinerja baik tanpa menunggu perintah;')
  st.write('2. Gesit dalam mengambil inisiatif tindakan')
  st.write('3. Mampu melihat peluang untuk kinerja yang lebih baik.')
