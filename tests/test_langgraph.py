from app.langgraph.orchestrator.workflow import graph

from app.langgraph.rag.policy_loader import load_sample_policy

load_sample_policy()

initial_state = {

    "claim_text": """
    Patient Name: Alice Johnson
    Insurance ID: INS7777
    Procedure: MRI
    """,

    "extracted_entities": {},

    "retrieved_policy": "",

    "validation_result": {},

    "final_decision": {},

    "reasoning_logs": []
}

result = graph.invoke(initial_state)

print(result)