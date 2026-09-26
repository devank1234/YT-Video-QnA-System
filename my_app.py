import streamlit as st
from QnA_system import extract_video_id, process_video

st.title("🎙️ YouTube Video Q&A Chatbot")

# Session state initialization
if 'qa_chain' not in st.session_state:
    st.session_state.qa_chain = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'video_loaded' not in st.session_state:
    st.session_state.video_loaded = False

# YouTube video input
video_url = st.text_input("🔗 Enter YouTube Video URL:")
video_id = extract_video_id(video_url)

# Process video
if st.button("🔍 Process Video") and video_id:
    with st.spinner("Fetching transcript and setting up the QA system..."):
        qa_chain, error = process_video(video_id)
        if error:
            st.error(f"❌ {error}")
            st.session_state.video_loaded = False
        else:
            st.session_state.qa_chain = qa_chain
            st.session_state.messages = []  # Reset chat history
            st.session_state.video_loaded = True
            st.success("✅ Video processed! Start chatting below.")

# Show info if not loaded
if not st.session_state.video_loaded:
    st.info("Paste a valid YouTube video URL and click 'Process Video' to begin.")
    st.stop()

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg['role']).markdown(msg['content'])

# Chat input
user_input = st.chat_input("Ask any question about the video...")

if user_input and user_input.strip():
    # Add user message
    st.chat_message('user').markdown(user_input)
    st.session_state.messages.append({'role': 'user', 'content': user_input})

    try:
        with st.spinner("Thinking..."):
            response = st.session_state.qa_chain.invoke({"query": user_input})
            result = response["result"]
        
        # Show assistant message
        st.chat_message('assistant').markdown(result)
        st.session_state.messages.append({'role': 'assistant', 'content': result})

        # Clear button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

    except Exception as e:
        st.error(f"⚠️ An error occurred: {str(e)}")
