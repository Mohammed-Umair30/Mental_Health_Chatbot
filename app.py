import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer with caching
@st.cache_resource
def load_model():
    model_path = "empathetic_model/content/empathetic_model"  # Correct local path
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    return tokenizer, model

tokenizer, model = load_model()

st.title("🤖 Empathetic Chatbot")

# Session state to store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input box
user_input = st.text_input("You:", key="input")

if user_input:
    # Format chat history more clearly with Speaker/Listener pairs
    history_text = ""
    for x in st.session_state.history:
        history_text += f"Speaker: {x['user']}\nListener: {x['bot']}\n"

    # Append new user input
    prompt = f"{history_text}Speaker: {user_input}\nListener:"

    # Generate model response
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        eos_token_id=tokenizer.eos_token_id,
        repetition_penalty=1.2,  # helps reduce repeated lines
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Only keep model's response after last 'Listener:'
    if "Listener:" in response:
        bot_reply = response.split("Listener:")[-1].strip().split("Speaker:")[0].strip()
    else:
        bot_reply = response.strip()

    # Update history
    st.session_state.history.append({"user": user_input, "bot": bot_reply})

# Display chat history
for entry in reversed(st.session_state.history):
    st.markdown(f"**You:** {entry['user']}")
    st.markdown(f"**Bot:** {entry['bot']}")
    st.markdown("---")
