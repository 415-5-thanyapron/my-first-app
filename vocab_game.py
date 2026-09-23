import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# กำหนดค่าเริ่มต้น
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


# ฟังก์ชันเริ่มเกมใหม่
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# แสดงผลคะแนน
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ข้อ 1
    if u_ans1 == "banana":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: คำตอบที่ถูกคือ banana")

    # ข้อ 2
    if u_ans2 == "school":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: คำตอบที่ถูกคือ school")

    # ข้อ 3
    if u_ans3 == "teacher":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: คำตอบที่ถูกคือ teacher")

    # ข้อ 4
    if u_ans4 == "library":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: คำตอบที่ถูกคือ library")

    st.info(f"🏆 ได้คะแนนรวม: {score}/4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ปุ่มเริ่มเกม
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# แสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# ช่องตอบคำถาม
ans1 = st.text_input(
    "ข้อ 1: I eat a `b _ n _ n _` every morning. 🍌",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: I go to `s _ h _ _ l` every day. 🏫",
    value=st.session_state.ans2_val
)

ans3 = st.text_input(
    "ข้อ 3: My `t _ _ c h _ r` teaches English. 👨‍🏫",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "ข้อ 4: I read books in the `l _ b r _ r y`. 📚",
    value=st.session_state.ans4_val
)

# อัปเดตคำตอบ
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4


# ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()


# แสดงผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.write("นางสาว ธันยพร เชื้อหล้า เลขที่ 5 ม.4/15")
