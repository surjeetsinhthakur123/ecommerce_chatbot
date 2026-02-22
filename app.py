import streamlit as st
from services.groq_service import GroqService
from memory.conversation_manager import ConversationManager
from prompts.prompt_manager import PromptManager

st.set_page_config(page_title="E-commerce AI Assistant", layout="wide")

st.title("🛒 AI E-commerce Chatbot (Groq Powered)")

try:
    ConversationManager.initialize()
    llm = GroqService()

except Exception as e:
    st.error(f"Startup Error: {str(e)}")
    st.stop()

# Display previous chat
for message in ConversationManager.get_history():
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Ask about products, shipping, returns..."):

    ConversationManager.add_message("User", user_input)

    with st.chat_message("User"):
        st.markdown(user_input)

    with st.chat_message("Assistant"):
        with st.spinner("Thinking..."):

            messages = PromptManager.build_messages(
                ConversationManager.get_history(),
                user_input
            )

            response = llm.generate_response(messages)

            st.markdown(response)

    ConversationManager.add_message("Assistant", response)