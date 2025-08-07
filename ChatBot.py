import re
import random
rules = [
    (r'hi|hello|hey', [
        "Hello there! 👋 How can I help you?",
        "Hey! I'm here to chat. What brings you today?"
    ]),
    (r'how are you\??|what\'s up\??', [
        "I'm just a bunch of code, but if I had feelings, I'd say I'm doing well! How about you?",
        "I'm functioning as expected 😊. How are you doing?"
    ]),
    (r'(who|what) are you\??|your name\??', [
        "I'm your friendly rule-based chatbot! You can callBot.",
        "They call me PerplexBot, your digital assistant."
    ]),
    (r'tell me a joke|make me laugh', [
        "Why did the computer show up at work late? It had a hard drive!",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]),
    (r'(goodbye|bye|see you)', [
        "Goodbye! Chat again soon. 👋",
        "See you later! Take care."
    ]),
    (r'help|support', [
        "I'm here to help! What do you need support with?",
        "Happy to help! Describe your issue, please."
    ]),
    (r'(?i)thank(s| you)', [
        "You're welcome! 😊",
        "No problem at all!"
    ]),
    (r'(.*)weather(.*)', [
        "I can't give live weather updates, but I hope it's sunny for you.",
        "The weather's always pleasant inside a chatbot!"
    ]),

]

fallbacks = [
    "I'm not sure I understand. Can you rephrase?",
    "Interesting—tell me more.",
    "I’m still learning! Ask me something else.",
]

def match_rule(user_input):
    user_input = user_input.lower()
    for pattern, responses in rules:
        if re.search(pattern, user_input):
            return random.choice(responses)
    return random.choice(fallbacks)

def main():
    print("PerplexBot: Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if re.search(r'\b(bye|goodbye|exit|quit)\b', user, re.IGNORECASE):
            print("PerplexBot:", random.choice([
                "Goodbye! Have a great day.",
                "See you next time. 👋"
            ]))
            break
        response = match_rule(user)
        print("PerplexBot:", response)

if __name__ == '__main__':
    main()
