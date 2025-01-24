import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # konversi dari centimeter ke meter
    if height_m == 0:
        return 0
    bmi = weight / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

st.title("Kalkulator BMI")
st.write("Selamat datang di kalkulator BMI! Masukkan berat dan tinggi badan Anda untuk mengetahui kategori BMI Anda.")

berat = st.number_input("Masukkan berat badan (kg):", value=0.0)
tinggi = st.number_input("Masukkan tinggi badan (cm):", value=0.0)

if berat > 0 and tinggi > 0:
    bmi = calculate_bmi(berat, tinggi)
    kategori = bmi_category(bmi)
    st.write(f"**BMI Anda adalah:** {bmi:.2f}")
    st.write(f"**Kategori BMI Anda adalah:** {kategori}")

    # Simpan data pengguna
    data = {
        'tanggal': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'berat': [berat],
        'tinggi': [tinggi],
        'bmi': [bmi],
        'kategori': [kategori]
    }
    df = pd.DataFrame(data)
    df.to_csv('data_bmi.csv', mode='a', header=not os.path.exists('data_bmi.csv'), index=False)
    st.write("Data telah disimpan ke file 'data_bmi.csv'")

    # Grafik BMI vs Tinggi
    fig, ax = plt.subplots()
    ax.plot([tinggi], [bmi], 'bo-')
    ax.set_xlabel('Tinggi (cm)')
    ax.set_ylabel('BMI')
    ax.set_title('Grafik BMI vs Tinggi')
    st.pyplot(fig)
else:
    st.write("Harap masukkan berat dan tinggi badan yang valid")

st.sidebar.title("Tentang")
st.sidebar.info("""
                Aplikasi ini dibuat oleh kelompok Almira77.
                Dengan menggunakan Streamlit, Github, dan VSCode.
                Untuk informasi lebih lanjut, kunjungi [Github](https://github.com/almirafansgariskeras98/Almira-77.git).
""")
