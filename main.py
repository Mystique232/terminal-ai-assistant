
import os
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, RateLimitError

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OpenAI API key is missing. Check your .env file.")
    raise SystemExit(1)

# Create AI client
client = OpenAI(api_key=api_key)

MODEL = "gpt-4o-mini"

# System prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant.
Explain concepts in simple language.
Give clear and easy-to-understand answers.
Do not invent facts when you are unsure.
If you don't know something, say so.
"""

# Welcome message
print("\nWelcome to My Terminal AI Assistant!")
print("Ask me anything. Type 'exit' or 'quit' to stop.\n")

# Conversation loop
while True:
    question = input("You: ").strip()

    if question.lower() in ["exit", "quit"]:
        print("Assistant: Goodbye! See you next time.")
        break

    if not question:
        continue

    try:
        response = client.responses.create(
            model=MODEL,
            instructions=SYSTEM_PROMPT,
            input=question
        )

        print("\nAssistant:", response.output_text)
        print("Model:", response.model)

        if response.usage:
            print("Input tokens:", response.usage.input_tokens)
            print("Output tokens:", response.usage.output_tokens)
            print("Total tokens:", response.usage.total_tokens)

        print()

    except AuthenticationError:
        print("Error: Invalid API key. Check your .env file.")

    except RateLimitError:
        print("Error: API rate limit reached or insufficient API quota.")

    except Exception as error:
        print("Unexpected error:", error)
