
def run_chatbot():
    """
    A simple rule-based chatbot that responds to a few predefined user inputs.
    The conversation continues until the user types 'bye'.
    """
    print("Chatbot: Hi! How can I help you today?")

    while True:
        
    
        user_input = input("You: ").lower()

        
        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm a computer program, but thanks for asking!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            
            break
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")


run_chatbot()
