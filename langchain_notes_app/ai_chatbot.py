import streamlit as st
from datetime import datetime
import requests
import json

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot (Free Hugging Face API)")

# Smart response function
def get_ai_response(message):
    message_lower = message.lower()
    
    # Specific responses for common questions
    if any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings']):
        return "Hello! How can I help you today? 😊"
    
    elif 'apple' in message_lower:
        return "Apple can refer to two things:\n\n🍎 **The Fruit**: A nutritious and delicious fruit, rich in fiber and vitamins. Great for snacking!\n\n📱 **Apple Inc.**: A major technology company that creates iPhones, iPads, Mac computers, and other innovative products. Founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976."
    
    elif any(word in message_lower for word in ['python', 'programming', 'code']):
        return "Python is a popular programming language known for its simplicity and versatility. It's great for web development, data science, AI, and automation!"
    
    elif any(word in message_lower for word in ['ai', 'artificial intelligence', 'machine learning']):
        return "Artificial Intelligence (AI) is the simulation of human intelligence in machines. It includes machine learning, natural language processing, and computer vision. Very exciting field!"
    
    elif any(word in message_lower for word in ['weather', 'temperature']):
        return "I don't have access to real-time weather data, but you can check your local weather on weather apps or websites like weather.com!"
    
    elif any(word in message_lower for word in ['thank', 'thanks']):
        return "You're very welcome! Is there anything else I can help you with? 😊"
    
    elif any(word in message_lower for word in ['bye', 'goodbye', 'see you']):
        return "Goodbye! Have a wonderful day! 👋"
    
    elif 'how are you' in message_lower:
        return "I'm doing great, thank you for asking! I'm here and ready to help. How are you doing?"
    
    elif any(word in message_lower for word in ['name', 'who are you']):
        return "I'm an AI chatbot created to help answer your questions and have conversations. You can ask me about various topics!"
    
    else:
        # Generic helpful response
        return f"That's an interesting question about '{message}'! While I may not have specific information about that topic, I'm here to help. Could you tell me more about what you'd like to know?"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.timestamps = []

# Display chat history
for i, msg in enumerate(st.session_state.messages):
    role = msg["role"]
    timestamp = st.session_state.timestamps[i] if i < len(st.session_state.timestamps) else ""
    
    with st.chat_message(role):
        st.markdown(msg["content"])
        st.caption(f"🕒 {timestamp}")

# User input
if user_input := st.chat_input("Type your message..."):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.timestamps.append(timestamp)
    
    with st.chat_message("user"):
        st.markdown(user_input)
        st.caption(f"🕒 {timestamp}")
    
    # Generate AI response
    with st.spinner("🤖 Thinking..."):
        bot_response = get_ai_response(user_input)
    bot_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.session_state.timestamps.append(bot_timestamp)
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)
        st.caption(f"🕒 {bot_timestamp}")

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.session_state.timestamps = []
    st.rerun()

st.info("🤖 This is a smart conversational chatbot! For document-based questions, use the RAG chatbot.")