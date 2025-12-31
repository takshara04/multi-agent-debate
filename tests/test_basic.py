from state import init_state
from nodes.agent import agent_node
from nodes.judge import judge_node

def test_agent_adds_turn():
    state = init_state()
    state["topic"] = "Test topic"
    agent_node(state, "AgentA", "Scientist")
    assert len(state["turns"]) == 1

def test_judge_outputs_winner():
    state = init_state()
    state["turns"] = [{"agent":"AgentA"},{"agent":"AgentB"}]
    judge_node(state)
    assert state["winner"] in ["AgentA", "AgentB"]
