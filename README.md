# AI_Chatbot
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
    "python libraries?":"puppet,panda,numpy.",
    "who made you?":"I was created using Python"
    "what is health?":  "Health is a state of complete physical, mental and social well-being."
    "who created python?" : "Python was created by Guido van Rossum in 1991."
    "what is python used for?" : "Python is used for web development, data science, AI, automation and more."
    "what is a function in python?" : "A function is a reusable block of code that performs a specific task."
     "what is numpy?" : "NumPy is a Python library used for numerical computations and arrays."
     "what is pandas?" : "Pandas is a Python library used for data manipulation and analysis."
     "what is opencv?" : "OpenCV is a Python library used for image and video processing."
     "what is flask?" : "Flask is a lightweight Python web framework used to build web applications."
     "what is django?" : "Django is a powerful Python web framework used for full stack web development."
     "what is machine learning?" : "Machine learning is a type of AI where machines learn from data without being programmed."
     "what is deep learning?" : "Deep learning is a type of machine learning that uses neural networks with many layers."
     "what is a chatbot?" :"A chatbot is an AI program that simulates conversation with humans."
     "what is automation?" : "Automation is using technology to perform tasks with minimal human involvement."
     "what is a dataset?" : "A dataset is a collection of data used to train and test machine learning models."

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
