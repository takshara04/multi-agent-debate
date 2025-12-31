from nodes.controller import build_graph
from state import init_state

print("Starting debate between Scientist and Philosopher...\n")
topic = input("Enter topic for debate: ")

graph = build_graph()
final = graph.invoke(init_state(topic))

print("\n[Judge] Summary of debate:")
print(final["summary"])
print(f"[Judge] Winner: {final['winner']}")
print("\nFull log saved to logs/debate_log_latest.json")
