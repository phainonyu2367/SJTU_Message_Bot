# intro 
This is a simple python-bot that scrapes down the information from the notices from [https://www.sjtu.edu.cn/tg/].

It uses LLM to summarize the content of the notices and send it to your Feishu bot.

# requirements
uv: 0.10.0
python: 3.10+

# quickStart
create a `.env` file in the root and set the following api-key/url.
- API_KEY: your deepseek api-key
- WEBHOOK_URL: your Feishu bot webhook url

use `uv sync` to sync the virtual environment

use `uv run main.py` to run the project.