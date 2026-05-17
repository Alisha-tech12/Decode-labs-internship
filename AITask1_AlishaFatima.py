import random

print("Chatbot ready! Type bye to exit...")

greetings= [
    "Hello! What brings you here?",
    "Hey! How can I help you?",
    "Greetings! What brings you here?"
]

feeling_responses=[
    "I'm just a chatbot but I'm doing great.",
    "I'm doing well, thanks for asking!",
    "I'm doing fine, how about you?"
]

ai_responses=[
    "AI is like teaching a child but with math and computers!",
    "AI stands for Artificial Intelligence. It is the simulation of human intelligence in machines that are programmed to think and learn like humans."
]
def get_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "bye":
        return "Goodbye"
    
    if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
        return random.choice(greetings)
    
    elif any(word in user_input for word in ["how are you?", "how do you do?", "how's it going?"]):
        return random.choice(feeling_responses)
    
    elif any(word in user_input for word in ["what is ai?", "ai", "artificial intelligence"]):
        return random.choice(ai_responses)

    elif "what is your name?" in user_input:
        return "I'm chatbot 1.0, your virtual assistant."
    
    elif "help" in user_input:
        return "Sure! I can help you with information about AI, answer general questions, or just chat. What would you like to know?"
    
    else:
        return "I don't understand that. Type 'bye' to exit."
    
while True:
    user_input = input("You: ")
    response = get_response(user_input)

    if response == "Goodbye":
        farewells = ["Bye! Come back soon!", "If you need anything don't hesitate to ask. Until then Take care!", "Goodbye!"]
        print(f"Chatbot: {random.choice(farewells)}")
        break

    print(f"Chatbot: {response}")
