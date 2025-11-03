import streamlit as st
from core.explainer import explain_concept
from core.summarizer import summarize_text
from core.quizzer import generate_quiz

def chat_ui(selected_mode):
    """Main chat interface with history and mode-specific behavior."""

    st.subheader(f"💬 StudyBuddy Chat - Mode: {selected_mode}")

    # Initialize session
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input box
    if prompt := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response based on mode
        with st.chat_message("assistant"):
            with st.spinner("Gemini is thinking..."):
                if selected_mode == "Explainer":
                    response = explain_concept(prompt)
                elif selected_mode == "Summarizer":
                    response = summarize_text(prompt)
                elif selected_mode == "Quizzer":
                    response = generate_quiz(prompt)
                else:
                    response = "⚠️ Unknown mode selected."

                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
