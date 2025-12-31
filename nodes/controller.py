from langgraph.graph import StateGraph, END
from nodes.agent import agent_node
from nodes.judge import judge_node
from nodes.router import router
from nodes.logger import logger_node

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("agentA", lambda s: agent_node(s, "AgentA", "Scientist"))
    graph.add_node("agentB", lambda s: agent_node(s, "AgentB", "Philosopher"))
    graph.add_node("judge", judge_node)
    graph.add_node("logger", logger_node)

    graph.set_entry_point("agentA")

    graph.add_edge("agentA", "logger")
    graph.add_edge("agentB", "logger")

    graph.add_conditional_edges("logger", router, {
        "agentA": "agentA",
        "agentB": "agentB",
        "judge": "judge"
    })

    graph.add_edge("judge", END)
    return graph.compile()
