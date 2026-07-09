import streamlit as st

st.set_page_config(page_title="حاسبة بسيطة", page_icon="🧮", layout="centered")

st.title("🧮 حاسبة بسيطة")

# اختيار العملية
operation = st.selectbox(
    "اختر العملية الحسابية:",
    ["جمع (+)", "طرح (-)", "ضرب (×)", "قسمة (÷)"]
)

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("الرقم الأول", value=0.0, format="%.4f")
with col2:
    num2 = st.number_input("الرقم الثاني", value=0.0, format="%.4f")

if st.button("احسب", use_container_width=True):
    try:
        if operation == "جمع (+)":
            result = num1 + num2
            symbol = "+"
        elif operation == "طرح (-)":
            result = num1 - num2
            symbol = "-"
        elif operation == "ضرب (×)":
            result = num1 * num2
            symbol = "×"
        elif operation == "قسمة (÷)":
            if num2 == 0:
                st.error("لا يمكن القسمة على صفر!")
                st.stop()
            result = num1 / num2
            symbol = "÷"

        st.success(f"النتيجة: {num1} {symbol} {num2} = {result}")

    except Exception as e:
        st.error(f"حدث خطأ: {e}")

st.markdown("---")
st.caption("تطبيق حاسبة بسيط مبني بـ Streamlit")
