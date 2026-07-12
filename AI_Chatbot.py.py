#AI Chatbot Project
response={
  "hi":"hello",
"how are you?":"i am fine thank you. how are you?",
    "what is python?":"python is high level language.",
    "what is java?":"Java is sensitive language",
    "what is c++?":"c++ is a language",
    "what is ai?":"ai is a technology",
    "what is flask?":"for development",
    "what is django?":"app development",
    "what is your name?":"Bot",
    "python is sensitive language?":"yes",
    "java and python are used for web development?":"yes",
    "python full stack which frameworks are needed?":"flask,django,database",
    "full form of ai?":"artificial intelligence ",
    "which is best full stack or python full stack?":"both are best in their places.",
    "can u understand urdu?":"yes",
    "python libraries?":"puppet,markdown,numpy.",
    "who made you?":"I was created using Python"

}
while True:
 user=input("You:").lower()
 if user=="exit":
    print("Goodbye!")
    break
 elif user in response:
    print("Bot:",response[user.lower()])
 else:
    print("Sorry! i can't Understand.")
