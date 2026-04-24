import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyA7H_mo5fagW5FPANnUy4rFFTs_jpZNTzo")
model = genai.GenerativeModel("gemini-2.5-flash")
messages = [
    "My payment got deducted but service is not activated",
    "App crashes every time I login",
    "How to change my email address?"
]

def classify_all(messages):
    prompt = f"""
You are a support ticket classifier.

Classify each message into:
- Category: Billing, Technical Issue, Account, General Inquiry
- Priority: High, Medium, Low

Return ONLY JSON ARRAY:
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
    if "```" in text:
        text = text.split("```")[1].replace("json", "").strip()
    return json.loads(text)
result = classify_all(messages)
print(json.dumps(result, indent=2))
