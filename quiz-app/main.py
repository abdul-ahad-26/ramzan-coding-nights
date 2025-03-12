"""
we are building a quiz app using python, streamlit for ui, uv for virtual environment whcih will ask a question selected randomly from the questions array.
Each question will have options and a answer,
If selected option is same as the answer for the question,
the question is solved else not solved
and after 5 second question will be changed
"""

# Imports
import streamlit as st
import random
import time

st.title("🐍 Python Quiz App")

questions = [
    {
        "question": "What is the output of print(2 * 3 ** 3)?",
        "options": ["18", "54", "216", "512"],
        "answer": "54",
        "difficulty": "medium"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "Tuple",
        "difficulty": "easy"
    },
    {
        "question": "What will type([]) return?",
        "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"],
        "answer": "<class 'list'>",
        "difficulty": "easy"
    },
    {
        "question": "How do you create an empty set in Python?",
        "options": ["{}", "set()", "[]", "()"],
        "answer": "set()",
        "difficulty": "medium"
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": ["//", "--", "#", "/* */"],
        "answer": "#",
        "difficulty": "easy"
    },
    {
        "question": "What is the time complexity of searching for an element in a dictionary by key?",
        "options": ["O(1)", "O(n)", "O(log n)"],
        "answer": "O(1)",
        "difficulty": "hard"
    },
    {
        "question": "How do you handle exceptions in Python?",
        "options": ["try-except", "if-else", "while"],
        "answer": "try-except",
        "difficulty": "medium"
    },
    {
        "question": "Which module is used for regular expressions in Python?",
        "options": ["regex", "re"],
        "answer": "re",
        "difficulty": "medium"
    }
]

def load_next_question():
    st.warning("Loading next question...")
    time.sleep(2)
    st.session_state.current_question = random.choice(questions)
    st.rerun()



if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)


question = st.session_state.current_question

difficulty_level ="Difficulty: " + question["difficulty"].capitalize()

st.info(difficulty_level)
st.subheader(question["question"])

selected_option = st.radio("Choose the answer", question["options"], key="answer")

if st.button("Submit Answer"):

    if selected_option is not question["answer"]:
        st.error("Error, correct answer is " + question["answer"])
    else:
        st.success("Answer is correct")
        st.balloons()
        load_next_question()

if st.button("Skip"):
    load_next_question()