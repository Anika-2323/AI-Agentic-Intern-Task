import streamlit as st
import google.generativeai as genai
import json
import re

genai.configure(api_key="AIzaSyDow5X3OmcJ8wtk8qYv-jb-i-91urWlTtI")

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Support Ticket Classifier", page_icon="🤖")

st.title("🤖 AI Support Ticket Classifier")
st.write("Enter multiple messages (one per line)")

def classify_messages(messages):
    prompt = f"""
You are a support ticket classifier.

Classify EACH message into:
- Category: Billing, Technical Issue, Account, General Inquiry
- Priority: High, Medium, Low

Return ONLY JSON ARRAY like:
[
  {{
    "message": "",
    "category": "",
    "priority": ""
  }}
]

Messages:
{messages}
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    # Clean markdown
    if "```" in text:
        text = text.split("```")[1].replace("json", "").strip()

    # Extract JSON safely
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    else:
        raise ValueError("Invalid JSON from model")

# 🧾 Multi-input (one per line)
user_input = st.text_area(
    "Enter messages (one per line):",
    height=150
)

if st.button("Classify All"):
    if user_input:
        try:
            messages = [m.strip() for m in user_input.split("\n") if m.strip()]

            result = classify_messages(messages)

            st.subheader("Results:")
            st.json(result)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter at least one message.")
