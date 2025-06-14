import os
from dotenv import load_dotenv
from google import genai

# Load in API key from .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Initialize the GenAI client with the API key
client = genai.Client(api_key=api_key)

# Generate content using the Gemini model
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
)

print(response.text)
print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
print(f'Response tokens: {response.usage_metadata.candidates_token_count}')