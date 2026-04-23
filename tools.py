import json



# 1: Calculator
# ─────────────────────────────────────────

def calculator(expression):
    
    allowed = set("0123456789+-**/(). %")
    for char in expression:
        if char not in allowed:
            return "Error: Invalid characters in expression."

    try:
        result = eval(expression)
        return str(result)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"



# 2: Task Manager
# ─────────────────────────────────────────


tasks = []

def add_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(task)
    return f"✅ Task added: \"{title}\""


def list_tasks():
    if len(tasks) == 0:
        return "📋 No tasks yet."

    lines = []
    for task in tasks:
        if task["done"]:
            status = "✅"
        else:
            status = "⬜"
        lines.append(f"  {status} [{task['id']}] {task['title']}")

    return "📋 Your Tasks:\n" + "\n".join(lines)




TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a math expression and return the result.",

            "parameters": {
                "type": "object",

                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A math expression like '12 * 7 + 3'"
                    }
                },

                "required": ["expression"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "add_task",
            "description": "Add a new task to the task list.",

            "parameters": {
                "type": "object",

                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The task description"
                    }
                },

                "required": ["title"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_tasks",
            "description": "Show all tasks in the task list.",

            "parameters": {
                "type": "object",

                "properties": {}
            }
        }
    }
]



TOOL_MAP = {
    "calculator": calculator,
    "add_task":   add_task,
    "list_tasks": list_tasks,
}


def dispatch(tool_name, arguments):
    func = TOOL_MAP.get(tool_name)

    if func is None:
        return f"Error: Unknown tool '{tool_name}'."

    try:
        return func(**arguments)
    except Exception as e:
        return f"Error running tool '{tool_name}': {e}"