import json
import os
from datetime import datetime

LOG_PATH = "logs/debate_log_latest.json"

def logger_node(state):
    os.makedirs("logs", exist_ok=True)

    stamped_turns = []
    for t in state["turns"]:
        stamped_turns.append({
            "time": datetime.now().isoformat(),
            "round": t["round"],
            "agent": t["agent"],
            "text": t["text"]
        })

    record = {
        "final_round": state["round"],
        "winner": state.get("winner", ""),
        "summary": state.get("summary", ""),
        "turns": stamped_turns
    }

    with open(LOG_PATH, "w") as f:
        json.dump(record, f, indent=2)

    return state
