import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_prompt = contents=sys.argv[1]

# system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT' ## Copied to prompts.py


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

try:
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),

)
    
    print(response.text)    

except IndexError:
    print("There was an error!")
    sys.exit(1)

verbosity = "--verbose" in sys.argv

if verbosity:

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    try:
        if response.usage_metadata:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
            #print(f"Total Tokens for this interaction: {response.usage_metadata.total_token_count}")
        else:
            print("No usage metadata available in the response.")
    except NameError:
        print("Bad argument provided, so no usage data.")
