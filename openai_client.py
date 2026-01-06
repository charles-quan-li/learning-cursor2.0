import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def connect_to_openai():
    """Connect to OpenAI API and test the connection."""
    # Get API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found. Please set it in your .env file or environment variables."
        )
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Test the connection with a simple request
    try:
        print("Connecting to OpenAI...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Say 'Hello! Connection successful.' in one sentence."}
            ],
            max_tokens=50
        )
        
        message = response.choices[0].message.content
        print(f"✅ Connection successful!")
        print(f"Response: {message}")
        
        return client
        
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        raise

if __name__ == "__main__":
    client = connect_to_openai()
    print("\nOpenAI client is ready to use!")

