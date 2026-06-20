import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(".local.env", override=True)
api_key=os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Open API key is not set. Please set it")
client = OpenAI(api_key=api_key)


def chat_with_agent(user_message: str) -> str:
    if not client:
        return "AI is not available right now becuase the API Key is missing"
    
    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
            {"role": "system", "content": """
             You are a job appication assistant. Help the user search for jobs, 
             which match resume skills, draft cover and suggest application steps.
             Always ask for confirmation before applying automatically"""},
             {"role": "user", "content": user_message}
            ]
         )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI request failed: {e}"
    


print("Hello, I'm your chatbot! How can I assist you today?")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Thank you!, see you next Time!!!")
        break
    reply = chat_with_agent(user_input)
    print("\nBot:", reply)
