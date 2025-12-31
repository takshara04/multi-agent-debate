import ollama

def agent_node(state, agent_name, persona):
    # round & turn update
    state["round"] += 1
    state["turn"] = "B" if state["turn"] == "A" else "A"

    # recent memory
    memory = "\n".join([t["text"] for t in state["turns"]][-4:])
    topic = state["topic"]

    prompt = f"""
You are a {persona}.
Debate topic: {topic}

Previous arguments:
{memory}

Rules:
- Give exactly ONE concise argument.
- Max 2–3 short lines.
- Stay strictly on topic.
- Do NOT repeat earlier points.
- No paragraphs, no fluff.

Now give your argument:
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response["message"]["content"].strip()
    reply = "\n".join(reply.split("\n")[:3])  # hard limit to 3 lines

    state["turns"].append({
        "round": state["round"],
        "agent": agent_name,
        "text": reply
    })

    print(f"[Round {state['round']}] {agent_name.replace('Agent','')}: {reply}")
    return state
