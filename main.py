from agent import Agent

agent = Agent()

print("=" * 40)
print("🤖 Mini AI Agent is ready!")
print("=" * 40)
print("Commands you can use:")
print("  /extract <text>  → get JSON output")
print("  /history         → see past messages")
print("  /clear           → clear memory")
print("  exit             → quit")
print("=" * 40)
print()

while True:

    user_input = input("You: ").strip()

    if user_input == "":
        continue

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    if user_input.lower() == "/history":
        agent.memory.show_history()
        continue

    if user_input.lower() == "/clear":
        agent.memory.clear()
        print("🧹 Memory cleared!\n")
        continue

    reply = agent.chat(user_input)

    print(f"Agent: {reply}")
    print()