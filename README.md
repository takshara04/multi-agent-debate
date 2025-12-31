# Multi-Agent Debate DAG (LangGraph)

This project implements a LangGraph-based multi-agent debate system where two autonomous agents engage in a structured, turn-based debate over a user-provided topic. The system enforces strict turn order, memory isolation, coherence validation, and produces a judge summary with a declared winner after 8 rounds.

## Features
- CLI-driven topic input  
- 8-round structured debate (4 turns per agent)  
- Strict DAG-based routing and turn enforcement  
- Persona-driven agents (Scientist & Philosopher)  
- Memory isolation and repetition prevention  
- Automatic coherence & topic-drift validation  
- Judge node with final decision & reasoning  
- Graphviz DAG generation (dag.png)  
- Persistent debate logging (logs/debate_log.json)  
- Automated validation tests  

## How to Run
pip install langgraph ollama graphviz  
brew install graphviz  
ollama serve  
ollama pull phi3  
python run_debate.py  

## Generate DAG Diagram
python generate_dag.py  

## Tests
python -m pytest tests/test_basic.py  

## Output
- Round-by-round CLI debate  
- Final judge summary & declared winner  
- Logs stored in logs/debate_log.json  
- DAG image in dag.png  

## Project Structure
multi_agent_debate/  
nodes/  
personas/  
tests/  
logs/  
run_debate.py  
generate_dag.py  
dag.png  
graph.py  
state.py  
README.md  

## Summary
This project demonstrates a complete LangGraph DAG-based multi-agent orchestration system with routing, memory, validation, testing, logging, and judge-based evaluation.
