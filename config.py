import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_client():
    if not GROQ_API_KEY:
        raise EnvironmentError("GROQ_API_KEY not found in .env file.")
    return Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are a helpful AI assistant with access to tools.

You have these tools available:
- calculator: use for any math calculations
- add_task: use to add a task
- list_tasks: use to list all tasks


For general knowledge questions like capitals, history, science, 
definitions — answer directly from your knowledge. 
Do NOT say you need internet for basic facts.
Do NOT use brave_search or any web search tool.

Be confident and concise in your answers."""

SYSTEM_EXTRACT_PROMPT = """Extract all key entities from the user's text and return ONLY a valid JSON object.
Include fields like name, age, city, date, amount, or any other clearly mentioned attributes.
Return ONLY the JSON — no explanation, no markdown, no extra text."""