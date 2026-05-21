import os

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(

    base_url="https://models.inference.ai.azure.com",

    api_key=os.getenv("GITHUB_TOKEN")
)

print("CLIENT BASE URL:", client.base_url)