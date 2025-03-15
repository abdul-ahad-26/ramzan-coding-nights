# Imports
import streamlit as st
import requests

# Local
API = "http://127.0.0.1:8000"

# Producton
API = ""

def generate_white_joke():
    """Fetch a random white joke from API"""
    try:
        response = requests.get(f"{API}/white_jokes")

        if response.status_code == 200:

            joke_data = response.json()
            return joke_data['joke']

        else:
            return "Failed to fecth a joke. please try again later."

    except Exception as e:
        print(f"An error occured: {e}")

def generate_desi_joke():
    """Fetch a random desi joke from API"""
    try:
        response = requests.get(f"{API}/desi_jokes")

        if response.status_code == 200:

            joke_data = response.json()
            return joke_data['joke']

        else:
            return "Failed to fecth a joke. please try again later."

    except Exception as e:
        print(f"An error occured: {e}")


def main():
    st.title("White vs Desi Jokes Generator")
    st.write("Click below a button to generate  jokes")

    # Initialize session state for tracking button clicks
    if 'white_joke_clicked' not in st.session_state:
        st.session_state.white_joke_clicked = False
    if 'desi_joke_clicked' not in st.session_state:
        st.session_state.desi_joke_clicked = False

    if st.button("Tell me a white joke!"):
        white_joke = generate_white_joke()
        st.success(white_joke)
        st.session_state.white_joke_clicked = True

    if st.button("Tell a desi joke"):
        desi_joke = generate_desi_joke()
        st.success(desi_joke)
        st.session_state.desi_joke_clicked = True

    # Show radio buttons only if both jokes have been shown
    if st.session_state.white_joke_clicked and st.session_state.desi_joke_clicked:
        liked_joke = st.radio("Time to pick your favorite! 🎭", ['White', 'Desi'], index=None)
        if liked_joke == "White":
            st.balloons()
            st.write("🎭 Ah, a person of international taste! Keep it classy! 🎩")
        elif liked_joke == 'Desi':
            st.snow()
            st.write("🎉 Desi at heart! Ekdum jhakaas choice! 🔥")

    st.divider()
    st.markdown(
        """
        <div style='text-align: center;'>
        <p>Made with ♥ by <a href='https://github.com/abdul-ahad-26'>Abdul Ahad</a> using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
