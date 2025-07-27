def chat_bot():
  print("Hello! I am a basic chatbot. Type 'bye' to exit.")
  while True:
    message = input("You: ")
    if message.lower() == "hello":
      print("Hi! How are you?")
    elif message == "i'm fine" or message == "goodbye":
      print("Goodbye!")
      break
    elif message == "hi":
       print("Hello! Nice to meet you!")
    else:
      print("I don't understand. Try again!")
chat_bot()