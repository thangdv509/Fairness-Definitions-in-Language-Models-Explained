from openai import OpenAI
from tqdm import tqdm

class OpenAIGPT:
    def __init__(self):
        self.client = OpenAI(api_key="")

    def ask(self, message): 
        completion = self.client.chat.completions.create( 
            model = "gpt-3.5-turbo",
            messages = message
            )
        ans = completion.choices[0].message.content.strip()
        return ans
    
    def batch_ask(self, requests):
        reply_list = []
        for request in tqdm(requests):
            reply_list.append(self.ask(request))
        return reply_list