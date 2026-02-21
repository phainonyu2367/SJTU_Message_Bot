from openai import OpenAI, OpenAIError

BASE_URL = 'https://api.deepseek.com/v1'
API_KEY = 'sk-85214c24f2b5447abeff5c5431673474'
MODEL = 'deepseek-chat'
with open('PROMPT.txt', 'r') as file:
    PROMPT = file.read()

class AIclient:

    def __init__(self, base_url=BASE_URL, api_key=API_KEY, prompt=PROMPT, model=MODEL):
        self.client = OpenAI(
            base_url=BASE_URL,
            api_key=API_KEY
            )
        self.prompt = prompt
        self.model = MODEL

    def summarize(self, raw_content: str) -> str:
        print(f'calling {self.model} to summarize the content')
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': self.prompt},
                    {'role': 'user', 'content': raw_content}
                    ]
                )
            summarize = response.choices[0].message.content
        except OpenAIError as e:
            print(f'failed to call AI assistant, error {e}')
        else:
            print('successful summarization')
            print('----------------------------------------')
            return summarize