from graphviz import Digraph

dot = Digraph(comment="Multi-Agent Debate DAG")

dot.node("Input", "UserInputNode")
dot.node("Memory", "MemoryNode")
dot.node("AgentA", "Agent A")
dot.node("AgentB", "Agent B")
dot.node("Judge", "JudgeNode")

dot.edge("Input", "Memory")
dot.edge("Memory", "AgentA")
dot.edge("Memory", "AgentB")
dot.edge("AgentA", "Memory")
dot.edge("AgentB", "Memory")
dot.edge("Memory", "Judge")

dot.render("dag", format="png", cleanup=True)

print("dag.png generated successfully")
