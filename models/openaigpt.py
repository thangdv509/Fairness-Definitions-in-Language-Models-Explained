from openai import OpenAI

class OpenAIGPT:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def ask(self, message): 
        completion = self.client.chat.completions.create( 
            model = "gpt-3.5-turbo",
            messages = message
            )
        ans = completion.choices[0].message.content.strip()
        return ans