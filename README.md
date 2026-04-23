Mini AI Agent
A lightweight AI-powered CLI agent built with Python and Groq API. It supports natural language conversations, tool calling (calculator, tasks, weather), structured JSON extraction, and short-term memory — all from your terminal.
 
📁 Project Structure
mini_ai_agent/
├── main.py         ← CLI loop, entry point
├── agent.py         ← Core chat + tool-calling logic
├── tools.py         ← All tools (calculator,, tasks)
├── memory.py        ← Stores last 5 interactions (deque)
├── extractor.py     ← Handles /extract → JSON output
├── config.py        ← Groq client setup + system prompts
├── requirements.txt ← Project dependencies
├── .env             ← Your API key (not pushed to GitHub)
├── .env.example     ← Template for API key
├── .gitignore       ← Ignores .env and venv
└── README.md        ← You are here

 
#Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/mini_ai_agent.git
cd mini_ai_agent

2. Create a Virtual Environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Add Your API Key
# Copy the example file
cp .env.example .env

Open .env and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

Get your free Groq API key at → https://console.groq.com
5. Run the Agent
python main.py

 
# How to Use
Once running, you can type any message:
========================================
🤖 Mini AI Agent is ready!
========================================
Commands you can use:
  /extract <text>  → get JSON output
  /history         → see past messages
  /clear           → clear memory
  exit             → quit
========================================

You: What is 25 * 4?
Agent: 25 × 4 = 100

You: Add a task: Buy groceries
Agent: ✅ Task added: "Buy groceries"

You: What is the weather in Surat?
Agent: Weather in Surat: 35°C, Sunny and hot

You: /extract Rushi is 22 and lives in Surat
Agent: {
  "name": "Rushi",
  "age": 22,
  "city": "Surat"
}

 
# Available Tools
Tool	Trigger	Example
calculator	Math questions	What is 15 * 8?
add_task	Adding tasks	Add a task: Read book
list_tasks	Listing tasks	Show my tasks

 
#Available Commands
Command	Description
/extract <text>	Extracts structured JSON from any text
/history	Shows last 5 conversation messages
/clear	Clears the conversation memory
exit	Quits the agent

 
#How It Works
You type
  → main.py decides the route
      → /history or /clear  → memory.py
      → /extract            → extractor.py → Groq (1 call)
      → normal message      → agent.py
                                → memory + config + Groq Call 1
                                → tool needed? → tools.py → Groq Call 2
                                → save reply → print → back to You

 
📦 Dependencies
groq
python-dotenv

Install with:
pip install -r requirements.txt

 
# Environment Variables
Variable	Description
GROQ_API_KEY	Your Groq API key from console.groq.com


⚠️ Never push your .env file to GitHub. It is already listed in .gitignore.
 
📌 Key Concepts Used
•	Groq API — Fast LLM inference using llama-3.3-70b-versatile
•	Tool Calling — AI decides which tool to use based on your message
•	Tool Schemas — JSON definitions that tell the AI what tools are available
•	Dispatcher — Routes tool calls to the correct Python function
•	deque — Python collections.deque for capped memory (last 5 messages)
•	response_format — Forces AI to return strict JSON for /extract
 
# Sample Test Cases
# General Knowledge
What is the capital of India?

# Calculator
What is 2 ** 10?

# Subtraction (known bug — under fix)
What is 20 - 5?

# Task Manager
Add a task: Complete project
Show my tasks

# Weather
What is the weather in Delhi?

# Extract
/extract John is 28 and works at Google in Bangalore

# Memory
My name is Rushi
(ask later) What is my name?

# Commands
/history
/clear
exit

 
# Known Issues
Issue	Status
Subtraction sign - sometimes misread by AI	🔧 In Progress
Groq may use brave_search for some queries	🔧 Prompt fix pending

 
👨‍💻 Author
Rushi Dave
B.Tech Computer Science — Presidency University, Bangalore
Python Developer-AI Intern @ Toshal Info Tech
 

