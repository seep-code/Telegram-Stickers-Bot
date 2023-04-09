def chat_responses(input_text):

    user_message = str(input_text).lower()

    if user_message in ['hello', 'hi', "what's up", "what's up?" 'howdy', 'hey', 'sup']:
        return "Hey, do you want to make some stickers?"

    if user_message in ['who are you?', 'who are you']:
        return "My name is Easy Stickers Bot, I can help you make stickers."

    return "I don't understand you."
