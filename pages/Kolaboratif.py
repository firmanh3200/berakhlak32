import streamlit as st

st.set_page_config(layout='wide')

st.title('Panduan Berakhlak Pegawai BPS')
with st.container(border=True):
  st.header('Kolaboratif', divider='green')
  st.subheader('Membangun kerja sama yang sinergis')
  
with st.expander('Memberi kesempatan kepada berbagai pihak untuk berkontribusi'):
  st.success('Memberi kesempatan kepada berbagai pihak untuk berkontribusi')
  st.write('1. Pendelegasian tugas dan tanggung jawab kepada seluruh anggota tim kerja sesuai dengan proporsi dan kompetensi masing-masing')
  st.write('2. Mendukung pelaksanaan diskusi kelompok dalam menyelesaikan tugas organisasi')
  st.write('3. Memberikan kesempatan semua anggota tim ikut berpartisipasi dalam meningkatkan pencapaian tujuan organisasi. ')

with st.expander('Terbuka dalam bekerja sama untuk menghasilkan nilai tambah'):
  st.success('Terbuka dalam bekerja sama untuk menghasilkan nilai tambah')
  st.write('1. Menjalin komunikasi dengan berbagai pihak dalam menjalankan tugas dan program kerja untuk peningkatan kinerja organisasi;')
  st.write('2. Melakukan evaluasi secara bersama agar pencapaian tujuan organisasi lebih efektif dan efisien di masa mendatang')
  st.write('3. Bersedia melakukan pekerjaan secara bersama untuk mencapai tujuan organisasi (tidak silo).')

with st.expander('Menggerakkan pemanfaatan berbagai sumber daya untuk tujuan bersama'):
  st.success('Menggerakkan pemanfaatan berbagai sumber daya untuk tujuan bersama')
  st.write('1. Menginventarisir seluruh sumber daya yang ada agar dapat dimanfaatkan untuk peningkatan tujuan organisasi;')
  st.write('2. Cermat melihat semua potensi yang ada dalam lingkungan kerja dan dimanfaatkan untuk kemajuan organisasi')
  st.write('3. Mengembangkan dan meningkatkan kapabilitas SDM yang ada untuk meningkatkan capaian organisasi.')
