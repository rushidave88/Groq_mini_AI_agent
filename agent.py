import json
from config import get_client, SYSTEM_PROMPT
from memory import Memory
from tools import TOOL_SCHEMAS, dispatch
from extractor import extract_structured


class Agent:

    def __init__(self):
        
        self.client = get_client()

        
        self.memory = Memory()

    def chat(self, user_input):

       
        if user_input.lower().startswith("/extract "):
            text = user_input[len("/extract "):].strip()
            if not text:
                return "Usage: /extract <your text here>"
            return extract_structured(text)

        
        self.memory.add("user", user_input)

       
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages = messages + self.memory.get_messages()

        try:
            
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                tools=TOOL_SCHEMAS,
                tool_choice="auto"
            )

            
            message = response.choices[0].message

            
            if message.tool_calls:

                
                messages.append(message)

                
                for tool_call in message.tool_calls:

                    
                    name = tool_call.function.name

                    try:
                        args = json.loads(tool_call.function.arguments)
                    except json.JSONDecodeError:
                        args = {}

                    
                    result = dispatch(name, args)

                    
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    })

                
                follow_up = self.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages
                )
                final_reply = follow_up.choices[0].message.content

            else:
                
                final_reply = message.content

        except Exception as e:
            return f"⚠️ Error: {e}"

        
        self.memory.add("assistant", final_reply)

        
        return final_reply