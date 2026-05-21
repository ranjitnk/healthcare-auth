import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the variables from your .env file
load_dotenv()

# Initialize the GitHub Models client
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ.get("GITHUB_TOKEN") 
)

def ask_ai(user_prompt, system_prompt="You are a helpful assistant."):
    """A reusable function to send prompts to GPT-4o"""
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model="gpt-4o",
            temperature=0.7 # Lower numbers (0.2) are more factual; higher (1.0) are more creative
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with AI: {e}"

# --- Example of using it in your project ---
if __name__ == "__main__":
    result = ask_ai("Give me a 1-sentence slogan for a healthcare AI security app.")
    print(result)