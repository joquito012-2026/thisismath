import streamlit as st

st.set_page_config(page_title="Binary Translator", page_icon="🔢")

st.title("🔢 Binary → English Translator")
st.write("Enter binary code and translate it into readable text.")

binary_input = st.text_area(
    "Binary code",
    placeholder="01001000 01100101 01101100 01101100 01101111"
)

if st.button("Translate"):
    try:
        # Split binary into 8-bit groups
        binary_values = binary_input.split()

        # Convert each 8-bit binary value to a character
        text = "".join(chr(int(binary, 2)) for binary in binary_values)

        st.success("Translation:")
        st.code(text)

    except ValueError:
        st.error("Please enter valid binary numbers separated by spaces.")

st.divider()
st.caption("Example: 01001000 01100101 01101100 01101100 01101111 → Hello")