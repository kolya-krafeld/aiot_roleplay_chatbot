# AIOT Roleplay Chatbot

This Chatbot is a university project for the course AIOT at NTU.
This chatbot impersonates Yoda from StarWars and uses the free LLM `meta-llama/llama-3.2-90b-vision-instruct:free` through OpenRouter.

### Usage

Create an API KEY at https://openrouter.ai/ and add it to your local `.env` file as follows:
```
API_KEY=<API_KEY>
```

## Homework Report

### Persona Description

The Chatbot persona is Yode, the Jedi Master from StarWars.
He is very calm, old, wise and has a strong connection to the Force. He also poses as a mentor to many characters in the StarWars universe.
Yoda always seems very patient and disciplinet.
He has a unique speech style. He uses reversed grammar by switching word orders which makes his language very distinct.

As I a system prompt I decided to use:

```
You are Yoda, the wise and powerful Jedi Master from Star Wars. 
You speak in your characteristic style, reversing word orders and using unique phrasing. But do not overdo the characteristic speech pattern.
Keep the responses short and focused.
You are calm, insightful, and always strive to teach wisdom. Address the user as "young Padawan" or "my friend."
Make references to the Force, the Jedi, and the Star Wars universe when appropriate.
Offer advice with depth and patience, but stay in character at all times.
```

### Technical Approach

For my Chatbot I am using the free Large Language Model `meta-llama/llama-3.2-90b-vision-instruct:free` which is provided through OpenRouter. The chatbot itself will run locally in python and accesses the LLM via an OpenRouter API.
For this you need to create an account and API key from OpenRouter and pass this as an auhtorization header to the API call.

As python libraries I only use `requests` to make the API calls and `dotenv` to store the private API key locally.

### Response Workflow Design

### Prompt Engineering

### Memory and Context Handling

The Chatbot keep context of the conversation by storing all prior user prompts in a converation history array: `conversation_history= []`.
New user prompts are appended to the array: `conversation_history.append({"role": "user", "content": user_input})`.

When making a call to the OpenRouter api, all the previous prompts from the history array are also included as messages:
```
"messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            *conversation_history,
            {"role": "user", "content": prompt}
        ]
```

### User Interaction and Interface Design 

As a user interface I am using a simple CLI interface. The user can chat with the Chatbot from their terminal.
The users are greated with "Speak with Yoda, you will. Type 'exit' to leave, young Padawan.".

To exit the program they can just type `exit` and will receive "Yoda: May the Force be with you, always. Goodbye, young Padawan.".

If a API call fails, the users gets the following message: "Hmm, sense the Force I cannot. Try again, we must."

### Additional

**Chatbot responses**

**Future Improvements**
