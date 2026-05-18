import os
from groq import Groq

client = Groq(
    api_key= os.getenv("GROQ_API_KEY"),
)

messages = [] #all chats are saved here and can be used later for chat logs

while True:
    
  user = input("You: ")
  
  if user.lower() == "exit":
    print("Chat Ended!")
    break

  messages.append({"role": "user", "content": user})

  chat_completion = client.chat.completions.create(
      messages=messages,
      model="llama-3.3-70b-versatile",
  )
  
  reply = chat_completion.choices[0].message.content
  print("Bot:", reply)
  messages.append({"role": "assistant", "content": reply})
