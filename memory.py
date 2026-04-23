from collections import deque

class Memory:
    
    def __init__(self):
        self.history= deque(maxlen=5)

    def add(self, role, content):
        message={"role": role, "content": content}
        self.history.append(message)

    def get_messages(self):
        return list(self.history)
    
    def show_history(self):
        if len(self.history)==0:
            print("No history yet.")
            return
        
        print("Conversation History:")
        for i, message in enumerate(self.history,1):
            if message["role"]=="user":
                label="YOU"
            else:
                label="AI"
            print(f"{i}. {label}: {message['content']}")
        print()

    def clear(self):
        self.history.clear()

    
