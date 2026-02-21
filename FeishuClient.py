from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()

WEBHOOK_URL = getenv("WEBHOOK_URL")
if WEBHOOK_URL == None:
    raise ValueError('missing webhook_url')
HEADERS = {'Content-Type': 'application/json'}

class FeishuClient:

    def __init__(self, headers=HEADERS, webhook_url=WEBHOOK_URL):
        self.webhook_url = webhook_url
        self.headers = headers
    
    def format_message(self, message):
        formatted_message = {
            'msg_type': 'post',
            'content': {
                'post': {
                    'zh_cn': {
                        'title': '新通知',
                        'content': [[
                            {
                                'tag': 'text',
                                'text': '[SJTU_Message_Bot]: ' + message
                            }
                        ]]
                    }
                }
            }
        }
        return formatted_message

    def send(self, message: str):
        message = self.format_message(message)
        try:
            post = requests.post(url=self.webhook_url,
                                headers=self.headers,
                                json=message)
            post.raise_for_status()
        except requests.RequestException as e:
            print('飞书助手信息发送失败')
            print(e)
        else:
            print('通告信息已全部发送至飞书客户端')