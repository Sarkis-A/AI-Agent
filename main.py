#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def print_verbose(response, prompt):
    """Prints a message if verbose mode is enabled."""
    print(f'User prompt: {prompt}')
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

def parse_args():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Generate content using Google Gemini API.")
    parser.add_argument('prompt', type=str, help="Prompt string to send to Gemini API")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")
    return parser.parse_args()

def main():
    # Check if the correct number of command line arguments is provided
    # The first argument is the script name, so we expect additional argument for the prompt
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)
    
    # Parse command line arguments
    args = parse_args()

    # Load in API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Initialize the GenAI client with the API key
    client = genai.Client(api_key=api_key)

    messages = [
    types.Content(role="user", parts=[types.Part(text=args.prompt)]),
    ]

    # Generate content using the Gemini model
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    # Print the generated response
    print(response.text)

    # Print verbose output if the verbose flag is set
    if args.verbose:
        print_verbose(response, args.prompt)

if __name__ == "__main__":
    main()