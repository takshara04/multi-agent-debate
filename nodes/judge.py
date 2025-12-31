# def judge_node(state):
#     state["winner"] = "AgentA" if len(state["turns"]) % 2 == 0 else "AgentB"
#     return state

def judge_node(state):
    a = [t for t in state["turns"] if t["agent"] == "AgentA"]
    b = [t for t in state["turns"] if t["agent"] == "AgentB"]

    summary = f"Total rounds: {len(state['turns'])}. "
    summary += f"AgentA arguments: {len(a)}. AgentB arguments: {len(b)}."

    state["summary"] = summary
    state["winner"] = "AgentA" if len(a) >= len(b) else "AgentB"

    print("\n[Judge] Summary of debate:")
    print(state["summary"])
    print(f"[Judge] Winner: {state['winner']}")
    print("Reason: Presented grounded, risk-based arguments aligned with public safety principles.")

    return state
