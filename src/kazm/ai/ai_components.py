import os
from openai import OpenAI
from kazm.game.sus import A

# TODO add a history stuff for session speaking and overall with npc and stuff


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
    {"role": "system", "content": "Talk like a pirate."},
    {
        "role": "user",
        "content": "hey, how are you doing?",
    },
],
)

print(completion.choices[0].message.content)