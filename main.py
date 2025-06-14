#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    # Check if the correct number of command line arguments is provided
    # The first argument is the script name, so we expect one additional argument for the prompt
    if len(sys.argv) != 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)
    
    # Load in API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize the GenAI client with the API key
    client = genai.Client(api_key=api_key)

    # Generate content using the Gemini model
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=str(sys.argv[1])
    )

    print(response.text)
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

if __name__ == "__main__":
    main()