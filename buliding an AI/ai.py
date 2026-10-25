from openai import OpenAI

#put your own api key here and uncomment it 
# key = "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"

messages = []

client = OpenAI(
    api_key=key,  # This is the default and can be omitted
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create( messages=messages,
                        model="gpt-4o"
                        )
    
    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message["content"]}")

if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis, How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)