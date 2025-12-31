from langgraph.graph import StateGraph, END
from state import init_state
from nodes.user_input import user_input_node
from nodes.agent import agent_node
from nodes.memory import memory_node
from nodes.judge import judge_node
from nodes.router import router
from nodes.logger import logger_node

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("input", user_input_node)
    graph.add_node("memory", memory_node)
    graph.add_node("agentA", lambda s: agent_node(s, "AgentA", "Scientist"))
    graph.add_node("agentB", lambda s: agent_node(s, "AgentB", "Philosopher"))
    graph.add_node("judge", judge_node)
    graph.add_node("logger", lambda s: (logger_node(s, "state update"), s)[1])

    graph.set_entry_point("input")

    graph.add_edge("input", "memory")
    graph.add_edge("memory", "logger")

    graph.add_conditional_edges("logger", router, {
        "agentA": "agentA",
        "agentB": "agentB",
        "judge": "judge"
    })

    graph.add_edge("agentA", "memory")
    graph.add_edge("agentB", "memory")
    graph.add_edge("judge", "logger")
    graph.add_edge("logger", END)

    return graph.compile()

