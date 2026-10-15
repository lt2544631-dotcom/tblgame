import streamlit as st
import random

st.set_page_config(page_title="Plants vs Zombies Streamlit", layout="centered")

st.title("🌻 Plants vs. Zombies (Streamlit Edition)")

# Khởi tạo trạng thái game (Session State)
if "sun" not in st.session_state:
    st.session_state.sun = 100
if "grid" not in st.session_state:
    # Lưới 3 hàng, 5 cột (0: Trống, '🌻': Hướng dương, '🌱': Bắn đậu)
    st.session_state.grid = [[None for _ in range(5)] for _ in range(3)]
if "zombies" not in st.session_state:
    st.session_state.zombies = [random.randint(0, 2)] # Vị trí hàng của Zombie
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Hiển thị chỉ số
st.metric(label="Mặt trời (Sun)", value=st.session_state.sun)

# Chọn loại cây
plant_choice = st.radio("Chọn cây để trồng:", ["🌻 Hướng dương (50 Sun)", "🌱 Đậu bắn (100 Sun)"])

# Bàn chơi (Grid)
st.write("### Sân cỏ")
for r in range(3):
    cols = st.columns(5)
    for c in range(5):
        cell_label = st.session_state.grid[r][c] or "🔲"
        if cols[c].button(f"{cell_label}", key=f"btn_{r}_{c}"):
            if "Hướng dương" in plant_choice and st.session_state.sun >= 50:
                st.session_state.grid[r][c] = "🌻"
                st.session_state.sun -= 50
                st.rerun()
            elif "Đậu bắn" in plant_choice and st.session_state.sun >= 100:
                st.session_state.grid[r][c] = "🌱"
                st.session_state.sun -= 100
                st.rerun()

# Nút chuyển lượt (Next Turn)
if st.button("▶️ Lượt tiếp theo (Next Turn)"):
    # Cộng nắng từ Hướng dương
    for r in range(3):
        for c in range(5):
            if st.session_state.grid[r][c] == "🌻":
                st.session_state.sun += 25
    st.rerun()