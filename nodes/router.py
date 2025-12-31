
def router(state):
    if state["round"] >= 8:
        return "judge"

    return "agentA" if state["turn"] == "B" else "agentB"

