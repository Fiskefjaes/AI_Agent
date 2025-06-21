import os
import sys
from dotenv import load_dotenv
from google import genai







load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)


try:
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=sys.argv[1])
    print(response.text)
except IndexError:
    print("There was an error!")
    sys.exit(1)

try:
    if response.usage_metadata:

        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Total Tokens for this interaction: {response.usage_metadata.total_token_count}")
    else:
        print("No usage metadata available in the response.")
except NameError:
    print("Bad argument provided, so no usage data.")





