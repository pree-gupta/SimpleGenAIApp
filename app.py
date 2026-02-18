## Run the Tutor application
import streamlit as st
from tutor.chain import build_chain

st.set_page_config(page_title="AI Tutor", page_icon="🎓")

st.title("🎓 AI Learning Tutor")
st.caption("Ask me anything from your course!")

# ---------- Load Chain Once ----------
@st.cache_resource
def load_chain():
    return build_chain()

chain = load_chain()

# ---------- Session Chat History ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- Display Previous Messages ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---------- User Input ----------
user_input = st.chat_input("Ask a question about the subject...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get tutor response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = chain({"question": user_input})
            answer = result["answer"]
            st.markdown(answer)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})



