from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = 'https://api.deepseek.com/v1' 
API_KEY = os.getenv("API_KEY") # your-api_key
MODEL = 'deepseek-chat' # the model you used
with open('PROMPT.txt', 'r') as file:
    PROMPT = file.read()

class AIclient:
    """Client based on OpenAI lib. Use for summarizing the content of the aritcles"""

    def __init__(self, base_url=BASE_URL, api_key=API_KEY, prompt=PROMPT, model=MODEL):
        if API_KEY == None:
            raise OpenAIError('API_KEY not provided')
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
                    {'role': 'user', 'content': '请你对用户传进来的文章内容进行总结，总结至50字以内并返回输出结果注意：你应当只返回总结结果，不要返回额外的文字内容。以下是文章内容：' + raw_content}
                    ]
                )
            summarize = response.choices[0].message.content
        except OpenAIError as e:
            print(f'failed to call AI assistant, error {e}')
        else:
            print('successful summarization')
            print('----------------------------------------')
            return summarize