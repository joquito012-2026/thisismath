import streamlit as st

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Binary Translator",
    page_icon="01",
    layout="centered",
)

# ============================================================
# Styling
# ============================================================

st.markdown(
    """
    <style>
        .block-container {
            max-width: 850px;
            padding-top: 3rem;
            padding-bottom: 3rem;
        }

        .title {
            text-align: center;
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .subtitle {
            text-align: center;
            color: #777;
            font-size: 1.05rem;
            margin-bottom: 2rem;
        }

        .result-label {
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 0.4rem;
        }

        .footer {
            text-align: center;
            color: #888;
            font-size: 0.85rem;
            margin-top: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# Header
# ============================================================

st.markdown(
    '<div class="title">Binary Translator</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Convert text to binary and binary back to text.</div>',
    unsafe_allow_html=True,
)

# ============================================================
# Conversion Functions
# ============================================================


def binary_to_text(binary: str) -> str:
    """Convert binary bytes into UTF-8 text."""

    # Remove whitespace so both formats work:
    # 01001000 01101001
    # 0100100001101001
    cleaned = "".join(binary.split())

    if not cleaned:
        raise ValueError("Please enter some binary.")

    if any(char not in "01" for char in cleaned):
        raise ValueError("Binary can only contain 0 and 1.")

    if len(cleaned) % 8 != 0:
        raise ValueError("Binary must contain complete 8-bit groups.")

    byte_values = [
        int(cleaned[i:i + 8], 2)
        for i in range(0, len(cleaned), 8)
    ]

    try:
        return bytes(byte_values).decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError(
            "The binary does not represent valid UTF-8 text."
        )


def text_to_binary(text: str) -> str:
    """Convert UTF-8 text into binary."""

    if not text:
        raise ValueError("Please enter some text.")

    return " ".join(
        format(byte, "08b")
        for byte in text.encode("utf-8")
    )


# ============================================================
# Mode
# ============================================================

mode = st.segmented_control(
    "Conversion",
    ["Binary → Text", "Text → Binary"],
    default="Binary → Text",
)

st.write("")

# ============================================================
# Binary → Text
# ============================================================

if mode == "Binary → Text":

    binary_input = st.text_area(
        "Binary",
        placeholder="01001000 01100101 01101100 01101100 01101111",
        height=180,
        label_visibility="visible",
    )

    if st.button(
        "Translate",
        type="primary",
        use_container_width=True,
    ):
        try:
            result = binary_to_text(binary_input)

            st.success("Translation complete")

            st.text_area(
                "Result",
                value=result,
                height=120,
            )

        except ValueError as error:
            st.error(str(error))


# ============================================================
# Text → Binary
# ============================================================

else:

    text_input = st.text_area(
        "Text",
        placeholder="Hello, world!",
        height=180,
        label_visibility="visible",
    )

    if st.button(
        "Translate",
        type="primary",
        use_container_width=True,
    ):
        try:
            result = text_to_binary(text_input)

            st.success("Translation complete")

            st.text_area(
                "Result",
                value=result,
                height=180,
            )

        except ValueError as error:
            st.error(str(error))


# ============================================================
# Examples
# ============================================================

with st.expander("Examples"):

    st.markdown("**Binary → Text**")

    st.code(
        "01001000 01100101 01101100 01101100 01101111"
    )

    st.write("Result: `Hello`")

    st.markdown("**Text → Binary**")

    st.code("Hello")

    st.write(
        "Result: `01001000 01100101 01101100 01101100 01101111`"
    )


# ============================================================
# Footer
# ============================================================

st.markdown(
    '<div class="footer">Binary Translator • UTF-8 supported</div>',
    unsafe_allow_html=True,
)