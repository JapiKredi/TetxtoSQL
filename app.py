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

