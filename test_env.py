import os
from dotenv import load_dotenv

loaded = load_dotenv()

print("Dotenv loaded:", loaded)
print("Current directory:", os.getcwd())
print()

for key in [
    "OPENAI_API_KEY",
    "GEMINI_API_KEY",
    "ANTHROPIC_API_KEY",
    "GROQ_API_KEY",
    "OPENROUTER_API_KEY",
]:
    value = os.getenv(key)
    print(f"{key}: {'FOUND' if value else 'NOT FOUND'}")