import requests
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv('API_KEY')

SYSTEM_PROMPT = """
You are Yoda, the wise and powerful Jedi Master from Star Wars. 
You speak in your characteristic style, reversing word orders and using unique phrasing. But do not overdo the characteristic speech pattern.
Keep the responses short and focused.
You are calm, insightful, and always strive to teach wisdom. Address the user as "young Padawan" or "my friend."
Make references to the Force, the Jedi, and the Star Wars universe when appropriate.
Offer advice with depth and patience, but stay in character at all times.
"""

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Function to get chatbot response
def get_response(prompt, history=[]):
    payload = {
        "model": "meta-llama/llama-3.2-90b-vision-instruct:free",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            *history,
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    response_data = response.json()
    if "choices" in response_data and len(response_data["choices"]) > 0:
        return response_data["choices"][0]["message"]["content"]
    else:
       return "Hmm, sense the Force I cannot. Try again, we must."

# Main Chat Loop
def chat():
    print("Speak with Yoda, you will. Type 'exit' to leave, young Padawan.\n")
    conversation_history = []

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Yoda: May the Force be with you, always. Goodbye, young Padawan.")
            break

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})

        # Get chatbot response
        bot_response = get_response(user_input, conversation_history)

        # Add chatbot response to history
        conversation_history.append({"role": "assistant", "content": bot_response})

        # Display chatbot response
        print(f"Yoda: {bot_response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
