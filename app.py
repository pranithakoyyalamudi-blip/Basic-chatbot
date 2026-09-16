"""CodeAlpha Basic Chatbot - Streamlit Web UI.

A modern, responsive web interface for the rule-based chatbot.
Reuses the deterministic logic in main.py without retraining or AI models.
"""

import sys
import os
import time
import streamlit as st

# Ensure parent and local directory are on sys.path to import main
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from main import get_bot_response, is_exit_command

# Streamlit Page Configuration
st.set_page_config(
    page_title="CodeAlpha Basic Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom Styling
st.markdown(
    """
    <style>
    .stChatMessage {
        border-radius: 12px;
        padding: 8px 12px;
        margin-bottom: 8px;
    }
    .quick-btn {
        margin: 2px;
    }
    .header-badge {
        display: inline-block;
        background-color: #2e7d32;
        color: white;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_name" not in st.session_state:
    st.session_state.user_name = "Friend"

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    welcome_msg = (
        f"Hello! I am the **CodeAlpha Basic Chatbot** — an interactive, rule-based assistant.\n\n"
        f"I can converse, tell jokes, share tech facts, check time, and more! "
        f"Type a message below or use the quick buttons in the sidebar."
    )
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

# Sidebar Configuration
with st.sidebar:
    st.image("https://api.iconify.design/noto:robot.svg", width=64)
    st.title("Chatbot Settings")
    st.caption("CodeAlpha Python Programming Internship")

    st.markdown("---")
    st.subheader("👤 User Profile")
    new_name = st.text_input(
        "Your Name:",
        value=st.session_state.user_name if st.session_state.user_name != "Friend" else "",
        placeholder="Enter your name...",
        help="Personalizes greetings and conversation responses.",
    ).strip()

    if new_name:
        st.session_state.user_name = new_name.title()
    else:
        st.session_state.user_name = "Friend"

    st.markdown(f"**Current User:** `{st.session_state.user_name}`")

    st.markdown("---")
    st.subheader("⚡ Quick Actions")
    st.caption("Click any button to send an instant prompt:")

    quick_actions = [
        ("😄 Tell me a joke", "tell me a joke"),
        ("💡 Tech fact", "tell me a fact"),
        ("🪙 Flip a coin", "flip a coin"),
        ("🎲 Roll a die", "roll a die"),
        ("⏰ What time is it?", "what time is it"),
        ("📅 Today's date", "what is today's date"),
        ("❓ Help commands", "help"),
    ]

    selected_quick_prompt = None
    col1, col2 = st.columns(2)
    for idx, (label, prompt_val) in enumerate(quick_actions):
        col = col1 if idx % 2 == 0 else col2
        if col.button(label, key=f"quick_{idx}", use_container_width=True):
            selected_quick_prompt = prompt_val

    st.markdown("---")
    if st.button("🗑️ Clear Conversation", use_container_width=True, type="secondary"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": f"Chat reset! Hi {st.session_state.user_name}, how can I help you today?",
            }
        ]
        st.rerun()

    st.markdown("---")
    with st.expander("ℹ️ About this Chatbot"):
        st.write(
            """
            - **Architecture**: 100% Rule-Based (Deterministic)
            - **Models/APIs**: None (No LLM, zero training needed)
            - **Personalization**: Dynamic name recognition
            - **Built for**: CodeAlpha Python Programming Internship
            """
        )

# Main Chat Header
col_header, col_badge = st.columns([4, 1])
with col_header:
    st.title("🤖 Basic Chatbot")
    st.caption(f"Chatting with: **{st.session_state.user_name}** | Status: Rule-Based Engine Active")
with col_badge:
    st.markdown("<div style='text-align: right; margin-top: 15px;'><span class='header-badge'>🟢 Online</span></div>", unsafe_allow_html=True)

# Render Chat History
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


def process_user_message(user_input_text: str):
    """Processes a user message and returns the chatbot's response."""
    # 1. Record and display user message
    st.session_state.messages.append({"role": "user", "content": user_input_text})
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input_text)

    # 2. Normalize and compute rule-based response
    cleaned = user_input_text.strip().lower()
    user_name = st.session_state.user_name
    bot_reply = get_bot_response(cleaned, user_name=user_name)

    # 3. Stream/Display bot message
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        # Simulated subtle typing effect
        full_text = ""
        for char in bot_reply:
            full_text += char
            time.sleep(0.005)
            message_placeholder.markdown(full_text + "▌")
        message_placeholder.markdown(full_text)

    # 4. Save to session state
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})


# Handle Quick Prompt Click
if selected_quick_prompt:
    process_user_message(selected_quick_prompt)
    st.rerun()

# Chat Input Bar
prompt = st.chat_input(f"Message Basic Chatbot as {st.session_state.user_name}...")
if prompt:
    process_user_message(prompt)
    st.rerun()
