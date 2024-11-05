import streamlit as st

st.set_page_config(layout='wide')

st.title('Panduan Berakhlak Pegawai BPS')
with st.container(border=True):
  st.header('Kompeten', divider='green')
  st.subheader('Terus belajar dan mengembangkan kapabilitas')
  
with st.expander('Meningkatkan kompetensi diri untuk menjawab tantangan yang selalu berubah'):
  st.success('Meningkatkan kompetensi diri untuk menjawab tantangan yang selalu berubah')
  st.write('1. Meningkatkan kompetensi diri melalui pendidikan (formal/nonformal/kursus/diklat) yang diselenggarakan baik secara daring maupun luring')
  st.write('2. Bertukar pikiran dan berdiskusi dengan berbagai pihak untuk meningkatkan kompetensi diri; dan')
  st.write('3. Senang belajar dan berupaya mengikuti perkembangan terkini.')

with st.expander('Membantu orang lain belajar'):
  st.success('Membantu orang lain belajar')
  st.write('1. Aktif mendorong dan membantu orang lain untuk senantiasa meningkatkan pengetahuan dan kemampuan')
  st.write('2. Gemar membagikan pengetahuan, pengalaman, dan hal-hal positif terkait dengan pembelajaran yang dapat meningkatkan kapasitas individu di sekitarnya; dan')
  st.write('3. Menciptakan sarana dan lingkungan yang kondusif untuk belajar.')

with st.expander('Melaksanakan tugas dengan kualitas terbaik'):
  st.success('Melaksanakan tugas dengan kualitas terbaik')
  st.write('1. Melaksanakan tugas yang diberikan dengan hasil akhir yang maksimal;')
  st.write('2. Menetapkan standar kualitas yang tinggi dalam penyelesaian pekerjaan; dan')
  st.write('3. Menjaga dan meningkatkan kualitas hasil pekerjaan dengan melakukan evaluasi secara berkala dan sistematis.')
