import streamlit as st

st.set_page_config(layout='wide')

st.title('Panduan Berakhlak Pegawai BPS')
st.header('Berorientasi Pelayanan', divider='green')
st.subheader('Komitmen memberikan pelayanan prima demi kepuasan masyarakat')
with st.expander('Memahami dan memenuhi kebutuhan masyarakat'):
  st.success('Memahami dan memenuhi kebutuhan masyarakat')
  st.write('1. Mengidentifikasi kebutuhan stakeholders secara proaktif dalam rangka memberikan pelayanan prima')
  st.write('2. Turut serta dalam menyampaikan ragam data dan/atau informasi yang tersedia di BPS kepada stakeholders')
  st.write('3. Memberikan pelayanan rekomendasi dan konsultasi statistik berdasarkan kebutuhan konsumen atau pengguna data')

with st.expander('Ramah, cekatan, solutif, dan dapat diandalkan'):
  st.success('Ramah, cekatan, solutif, dan dapat diandalkan')
  st.write('1. Memberikan solusi terhadap permasalahan terkait data yang dihadapi stakeholders')
  st.write('2. Responsif dalam memberikan pelayanan')
  st.write('3. Menerapkan 5S (Senyum, Sapa, Salam, Sopan dan Santun) ketika memberikan pelayanan')

with st.expander('Melakukan perbaikan tiada henti'):
  st.success('Melakukan perbaikan tiada henti')
  st.write('1. Melakukan evaluasi untuk meningkatkan kualitas dan memperbaiki kekurangan')
  st.write('2. Menindaklanjuti setiap kritik, saran, dan masukan untuk perbaikan pelayanan')
  st.write('3. Melakukan upaya peningkatan wawasan dan pengetahuan dalam rangka
peningkatan kualitas pelayanan')
