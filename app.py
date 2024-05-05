import os
from openai import AsyncOpenAI


from chainlit.playground.providers.openai import ChatOpenAI
import chainlit as cl

from dotenv import load_dotenv

load_dotenv() 

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

print('All is good')

template = """SQL tables (and columns):
* Customers(customer_id, signup_date)
* Streaming(customer_id, video_id, watch_date, watch_minutes)

A well-written SQL query that {input}:
```"""


settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["```"],
}