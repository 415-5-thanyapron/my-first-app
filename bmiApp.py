import streamlit as st

# ส่วนที่ 1 หัวข้อหน้าเว็บ
st.markdown("## :red[⚖️ คำนวณดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")

# ส่วนที่ 2 รับค่าน้ำหนักและส่วนสูง
weight = st.number_input(
    "กรอกน้ำหนักของคุณ (กิโลกรัม):",
    min_value=1.0
)

height_cm = st.number_input(
    "กรอกส่วนสูงของคุณ (เซนติเมตร):",
    min_value=1.0
)

# ส่วนที่ 3 คำนวณ BMI
height_m = height_cm / 100
bmi = weight / (height_m ** 2)

# ส่วนที่ 4 แสดงผล
st.write(f"### ค่า BMI ของคุณคือ {bmi:.2f}")

if bmi < 18.5:
    st.info("น้ำหนักน้อย")
elif bmi < 23:
    st.success("น้ำหนักปกติ")
elif bmi < 25:
    st.warning("น้ำหนักเกิน")
else:
    st.error("อ้วน")
