# Imports
import streamlit as st
import zxcvbn
from bloom_filter2 import BloomFilter
import time


# Function to load the breached passwords into a Bloom filter
@st.cache_resource
def load_bloom_filter(file_path):
    bloom = BloomFilter(max_elements=1000000, error_rate=0.01)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                password = line.strip()
                bloom.add(password)
        return bloom
    except FileNotFoundError:
        st.error("❌ Breach data file not found")
        return None


st.title("🔐 Password Strength & Breach Checker")

# Description for users
st.write(
    "🔎 This tool checks your password strength and verifies if it has been breached. "
    "We compare your password against **1,000,000+ leaked passwords** from public data breaches. "
    "For security, your password is **never stored or sent online**."
)

with st.spinner("🔄 Loading password breach database..."):
    BLOOM_FILTER = load_bloom_filter("breached-passwords.txt")

password = st.text_input("Enter your password:", type="password")


if st.button("Check Password"):
    with st.spinner("🔄 Checking password..."):
        time.sleep(1.5)

        strength = zxcvbn.zxcvbn(password)
        st.subheader("🔹 Password Strength:")
        st.progress(strength["score"] / 4)

        for suggestion in strength["feedback"]["suggestions"]:
            st.warning(f"⚠ {suggestion}")

        st.subheader("🔍 Breach Check:")
        if BLOOM_FILTER is not None and password in BLOOM_FILTER:
            st.error(
                "🚨 WARNING: This password has been found in a data breach! Change it immediately."
            )
        else:
            st.success("✅ Safe: This password was NOT found in any known breaches.")
    st.success("✅ Check completed!")

for i in range(5):
    print()