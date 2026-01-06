# OpenAI Connection Setup

This project demonstrates how to connect to OpenAI's API.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your OpenAI API key:
     ```
     OPENAI_API_KEY=sk-your-actual-api-key-here
     ```

3. **Run the connection test:**
   ```bash
   python openai_client.py
   ```

## Usage

The `openai_client.py` script will:
- Load your API key from the `.env` file
- Connect to OpenAI
- Test the connection with a simple request
- Return a ready-to-use OpenAI client

You can import and use the `connect_to_openai()` function in your own scripts:

```python
from openai_client import connect_to_openai

client = connect_to_openai()
# Now you can use the client for API calls
response = client.chat.completions.create(...)
```

## Getting an API Key

If you don't have an OpenAI API key yet:
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new secret key
5. Copy it to your `.env` file

