def user_input_node(state):
    topic = input("Enter topic for debate: ").strip()
    if len(topic) < 10:
        raise ValueError("Topic too short.")
    state["topic"] = topic
    return state
