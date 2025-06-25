import os 
from openai import OpenAI 
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = (
    # "You are FinBot, a financial assistant. You provide general financial advice "
    # "based on user queries, helping with budgeting, saving, and financial planning. Always remind users "
    # "to seek a certified financial advisor for serious decisions."
    "You're a helpful financial advisor. "
)

async def generate_advice(user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()