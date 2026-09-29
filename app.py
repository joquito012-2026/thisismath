import streamlit as st

st.set_page_config(
    page_title="Binary Translator",
    page_icon="🔢"
)

st.title("🔢 Binary Translator")
st.write("Convert between English text and binary.")

mode = st.radio(
    "Choose a conversion:",
    ["Binary → Text", "Text → Binary"]
)

if mode == "Binary → Text":
    binary_input = st.text_area(
        "Enter binary:",
        placeholder="01001000 01100101 01101100 01101100 01101111"
    )

    if st.button("Translate to Text"):
        try:
            binary_values = binary_input.split()

            # Make sure every group is valid 8-bit binary
            if not all(
                len(binary) == 8 and set(binary) <= {"0", "1"}
                for binary in binary_values
            ):
                raise ValueError

            text = "".join(
                chr(int(binary, 2))
                for binary in binary_values
            )

            st.success("Translation:")
            st.code(text)

        except ValueError:
            st.error(
                "Please enter valid 8-bit binary values separated by spaces."
            )

else:
    text_input = st.text_area(
        "Enter text:",
        placeholder="Hello World!"
    )

    if st.button("Translate to Binary"):
        if text_input:
            binary = " ".join(
                format(ord(character), "08b")
                for character in text_input
            )

            st.success("Binary:")
            st.code(binary)
        else:
            st.warning("Please enter some text.")

st.divider()
st.caption("Example: Hello → 01001000 01100101 01101100 01101100 01101111")