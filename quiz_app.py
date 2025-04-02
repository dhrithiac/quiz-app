import streamlit as st
import pandas as pd

def load_quiz(file):
    xls = pd.questions_GMAT_PYA1(file)
    df = pd.read_excel(xls, sheet_name='Sheet1')
    df = df.dropna(subset=["Question", "Options", "Correct Answer"])
    return df

st.title("Simple Quiz App")

uploaded_file = st.file_uploader("Upload your quiz Excel file", type=["xlsx"])

if uploaded_file:
    df = load_quiz(uploaded_file)
    score = 0
    user_answers = {}

    for index, row in df.iterrows():
        options = str(row['Options']).split('\n')
        user_answer = st.radio(f"Q{index + 1}: {row['Question']}", options, key=f"question_{index}")
        user_answers[f"question_{index}"] = user_answer
    
    if st.button("Submit Quiz"):
        for index, row in df.iterrows():
            correct_answer = str(row['Correct Answer']).strip()
            if user_answers[f"question_{index}"].strip().upper() == correct_answer.upper():
                score += 1
        st.write(f"Your final score: {score}/{len(df)}")
