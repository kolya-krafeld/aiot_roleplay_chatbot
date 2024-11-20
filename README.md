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
Yoda always seems very patient and disciplined.
He has a unique speech style. He uses reversed grammar by switching word orders which makes his language very distinct.

### Technical Approach

For my Chatbot I am using the free Large Language Model `meta-llama/llama-3.2-90b-vision-instruct:free` which is provided through OpenRouter. The chatbot itself will run locally in python and accesses the LLM via an OpenRouter API.
For this you need to create an account and API key from OpenRouter and pass this as an auhtorization header to the API call.

As python libraries I only use `requests` to make the API calls and `dotenv` to store the private API key locally.

### Response Workflow Design

![chatbot_aiot](https://github.com/user-attachments/assets/afe13dab-69dc-474e-b973-fa957638580f)

Response workflow:
1. User Input
2. Validate user input: if its "exit" stop the Chatbot, otherwise normal prompt
3. Send request to OpenRouter
4. Recieve resonse from OpenRouter
5. Format LLM response
6. Display response to user


### Prompt Engineering

As I a system prompt I decided to use:

```
You are Yoda, the wise and powerful Jedi Master from Star Wars. 
You speak in your characteristic style, reversing word orders and using unique phrasing. But do not overdo the characteristic speech pattern.
Keep the responses short and focused.
You are calm, insightful, and always strive to teach wisdom. Address the user as "young Padawan" or "my friend."
Make references to the Force, the Jedi, and the Star Wars universe when appropriate.
Offer advice with depth and patience, but stay in character at all times.
```
It gives a detailed description of Yodas character and his distinct speaking style.

I had to adjust the prompt iteratively. These are the additions that I added later on with examples of how the chatbot responds to them:
- Call the user padawan or friend: <img width="757" alt="Screenshot 2024-11-20 at 14 12 05" src="https://github.com/user-attachments/assets/131e26cb-6cfc-46fa-91ba-88a9a8c67a18">
- Refer to the Force, Jedis or StarWars when possible:<img width="1031" alt="Screenshot 2024-11-20 at 14 14 14" src="https://github.com/user-attachments/assets/97e624da-3604-4c7b-846b-39a0cec10e5e">
- Keep the responses short. Beforehand the responses were full paragraphs which is not very typical for Yodas character. Now the responses are very brief: <img width="1271" alt="Screenshot 2024-11-20 at 14 15 27" src="https://github.com/user-attachments/assets/f2aa39fe-4a2a-4ec3-80d4-3405145fa9a5">

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
**Future Improvements**
To improve the Chatbot further, one could implement enhanced memory capabilites to keep responses and promts from conversations from other sessions. One could also include user feedback for the respones to use reinforcement learning for better results in the future.
Moreover, you could add a StarWars data-set/data base to the charbot for Yoda to refference more specific and detailed knowledge about the StarWars universe.
