import streamlit as st

st.set_page_config(layout='wide')

st.title('Panduan Berakhlak Pegawai BPS')
with st.container(border=True):
  st.header('Akuntabel', divider='green')
  st.subheader('Bertanggung jawab atas kepercayaan yang diberikan')
  
with st.expander('Melaksanakan tugas dengan jujur, bertanggung jawab, cermat, disiplin, dan berintegritas tinggi'):
  st.success('Melaksanakan tugas dengan jujur, bertanggung jawab, cermat, disiplin, dan berintegritas tinggi')
  st.write('1. Melaksanakan pekerjaan dengan akuntabel baik teknis maupun administrasi')
  st.write('2. Bekerja sesuai SOP dan mengikuti jadwal yang sudah ditetapkan; dan')
  st.write('3. Bersikap integritas dengan menolak perilaku yang tidak sesuai dengan aturan.')

with st.expander('Menggunakan kekayaan dan barang milik negara secara bertanggung jawab, efektif, dan efisien'):
  st.success('Menggunakan kekayaan dan barang milik negara secara bertanggung jawab, efektif, dan efisien')
  st.write('1. Memanfaatkan sarana dan prasarana (barang milik negara) secara efektif, efisien, dan sesuai dengan peruntukannya')
  st.write('2. Memelihara sarana dan prasarana (barang milik negara) dengan baik; dan')
  st.write('3. Menyadari hak pakai bukan hak milik atas sarana dan prasarana (barang milik negara).')

with st.expander('Tidak menyalahgunakan kewenangan jabatan'):
  st.success('Tidak menyalahgunakan kewenangan jabatan')
  st.write('1. Melaksanakan tugas pokok dan fungsi sesuai aturan atau kebijakan yang berlaku;')
  st.write('2. Tidak terlibat dalam praktik Korupsi, Kolusi dan Nepotisme (KKN); dan')
  st.write('3. Tidak memberikan dan/atau meminta perlakuan khusus kepada siapapun.')
