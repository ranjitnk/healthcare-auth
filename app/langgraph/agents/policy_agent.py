from app.langgraph.rag.retriever import retrieve_policy

def policy_agent(state):

    procedure = state["extracted_entities"].get(
        "procedure",
        ""
    )

    policy = retrieve_policy(procedure)

    logs = state.get("reasoning_logs", [])

    logs.append(
        f"[Policy Agent] Retrieved policy for procedure: {procedure}"
    )

    state["retrieved_policy"] = policy

    state["reasoning_logs"] = logs

    return state