import streamlit as st

st.title("Siapakah Kamu? - Mini Personality Quiz")

st.header("1. Kamu paling suka ngapain?")
q1 = st.radio("Pilih satu:", [
    "Ngoding sampai lupa waktu", #programmer
    "Bikin layout & warna yang estetik", #designer
    "Main data dan analisa tren" #datascientist
], key="q1")

st.header("2. Kamu lebih suka alat yang mana?")
q2 = st.radio("Pilih satu:", [
    "VS Code", #programmer
    "Figma", #designer
    "Google Colab" #datascientist
], key="q2")

st.header("3. Motto kamu?")
q3 = st.radio("Pilih satu:", [
    "Keep calm and debug the code", #programmer
    "Design is thinking made visual", #designer
    "In data we trust" #datascientist
], key="q3")

# Tombol untuk melihat hasil
if st.button("Lihat Hasil"):
    # Atur skor awal
    skor_programmer = 0
    skor_designer = 0
    skor_datascientist = 0
    
    # Hitung skor untuk soal 1
    if q1 == "Ngoding sampai lupa waktu":
        skor_programmer = skor_programmer + 1
    elif q1 == "Bikin layout & warna yang estetik":
        skor_designer = skor_designer + 1
    else:
        skor_datascientist = skor_datascientist + 1
    
    # Hitung skor untuk soal 2
    if q2 == "VS Code":
        skor_programmer = skor_programmer + 1
    elif q2 == "Figma":
        skor_designer = skor_designer + 1
    else:
        skor_datascientist = skor_datascientist + 1
    
    # Hitung skor untuk soal 3
    if q3 == "Keep calm and debug the code":
        skor_programmer = skor_programmer + 1
    elif q3 == "Design is thinking made visual":
        skor_designer = skor_designer + 1
    else:
        skor_datascientist = skor_datascientist + 1

    # Tampilkan hasil
    st.subheader("🧾 Hasil Kamu:")
    hasil = max(skor_programmer, skor_designer, skor_datascientist)
    # hasil = (0, 0, 3)

# Tampilkan hasil berdasarkan siapa yang punya skor tertinggi
    if hasil == skor_programmer:
        st.success("💻 Kamu cocok jadi PROGRAMMER sejati!")
        st.markdown("#### Programmer adalah orang yang menciptakan perangkat lunak dan aplikasi. Mereka memiliki kemampuan untuk memecahkan masalah dan menciptakan solusi inovatif.")
        st.image("https://media.giphy.com/media/26tPghhb3709o2F9u/giphy.gif")
    elif hasil == skor_designer:
        st.success("🎨 Kamu cocok jadi UI/UX DESIGNER kreatif!")
        st.image("https://media.giphy.com/media/YTbZzCkRQCEJa/giphy.gif")
    else:
        st.success("📊 Kamu cocok jadi DATA SCIENTIST masa depan!")
        st.image("https://media.giphy.com/media/3o7aD0MhFszXG5Z8rO/giphy.gif")
