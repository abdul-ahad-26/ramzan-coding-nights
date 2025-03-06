# Imports
import streamlit as st
import string
import secrets  


def generate_password(length, use_digits, use_special):
    """Generate a secure random password based on user preferences."""
    characters = string.ascii_letters  # A-Z, a-z

    if use_digits:
        characters += string.digits  # 0-9
    if use_special:
        characters += string.punctuation  # Special characters like @, #, $

    # Generate password securely
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# Streamlit UI
st.title("🔑 Secure Password Generator")

# User input options
length = st.slider("Select Password Length", min_value=30, max_value=60, value=40)
use_digits = st.checkbox("Include Digits (0-9)")
use_special = st.checkbox("Include Special Characters (!@#$...)")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)

    # Display password
    st.success("Password generated successfully!")
    st.code(password, language="plaintext")    
    
    # User instruction
    st.write("Click inside the box and press `Ctrl + C` to copy.")

