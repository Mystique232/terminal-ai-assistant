
# Terminal AI Assistant

A simple AI assistant built with Python that runs in the terminal and uses the OpenAI API to answer questions.

## Features

- Loads API keys securely using python-dotenv.
- Uses a system prompt to guide AI responses.
- Accepts questions continuously.
- Supports exit and quit commands.
- Displays AI responses, model name, and token usage.
- Includes basic error handling.

## Requirements

- Python 3
- OpenAI API key

## Installation

1. Clone or download this project.
2. Open the project folder in your terminal.
3. Create a virtual environment:

   python3 -m venv .venv

4. Activate it:

   source .venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

6. Create a .env file and add your API key:

   OPENAI_API_KEY=your_api_key_here

## How to Run

Run the following command:

python3 main.py

## Example Interaction

Welcome to My Terminal AI Assistant!

You: What is Python?

Assistant: Python is a programming language used to
create applications, websites, and automate tasks.

Model: gpt-4o-mini

Input tokens: 10
Output tokens: 20
Total tokens: 30

You: exit

Assistant: Goodbye! See you next time.

## Security

Never share your API key or upload your .env file to GitHub.

The .env file is included in .gitignore.

## Author

Terminal AI Assistant Project
