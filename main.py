import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types

if len(sys.argv) < 2:
    print("Expected 2 arguments")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]


client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

print(response.text)

verbose = "--verbose" in sys.argv[2:]

if verbose:
    print(
        f"""\
User prompt: {user_prompt}
Prompt tokens: {response.usage_metadata.prompt_token_count}
Response tokens: {response.usage_metadata.candidates_token_count}"""
    )
