# def memory_node(state):
#     return state

def memory_node(state):
    if state["turns"]:
        last = state["turns"][-1]["text"].lower()
        if state["topic"].lower().split()[0] not in last:
            print("Coherence warning: possible topic drift detected.")
    return state
