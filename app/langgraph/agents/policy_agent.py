from app.langgraph.rag.retriever import retrieve_policy

def policy_agent(state):

    entities = state["extracted_entities"]

    procedure = entities.get("procedure", "")

    diagnosis = entities.get("diagnosis", "")

    policy = retrieve_policy(
        procedure,
        diagnosis
    )

    state["retrieved_policy"] = policy

    logs = state.get("reasoning_logs", [])

    logs.append(
        f"[Policy Agent] Retrieved policy for procedure: {procedure}"
    )

    state["reasoning_logs"] = logs

    return state