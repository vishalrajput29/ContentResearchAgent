import streamlit as st
from crew_module import run_crew

st.set_page_config(page_title="YouTube Blog Writer", page_icon="📝", layout="centered")

st.title("🎥 YouTube Blog Writer AI 📝")

# User Input
topic = st.text_input("Enter your topic to generate blog:", "")

if st.button("Generate Blog"):
    if topic:
        with st.spinner("Generating blog content..."):
            try:
                result = run_crew(topic)
                st.success("Blog generated successfully!")
                st.write(result)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a topic!")
