import os

import dotenv
import openai

dotenv.load_dotenv()


openai.api_key = os.environ.get('OPENAI_API_KEY')

print(openai.Engine.list())
