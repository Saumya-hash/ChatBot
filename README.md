🤖 Rule-Based Chatbot in Python


A simple terminal-based chatbot built using Python and regular expressions (regex). This chatbot matches user input against predefined patterns and responds accordingly — great for understanding how rule-based Natural Language Processing (NLP) works!



📌 Features
Responds to:
Greetings (hi, hello, hey)
Casual questions (how are you?, what's up?)
Identity queries (who are you?, your name?)
Jokes and humor
Farewells (bye, goodbye, exit)
Help or support requests
Thanks
Mentions of weather
Uses randomized responses to add variation
Fallback replies for unmatched inputs
Easy to expand with new patterns and replies


🧠 How It Works
Uses a list of regex-based rules to match user input.
If a match is found, the bot selects a random response from the corresponding list.
If no match is found, it returns a fallback message.
Continues until the user types a farewell keyword (e.g., bye, exit, quit).
