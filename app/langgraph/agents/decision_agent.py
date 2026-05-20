def decision_agent(state):

    validation = state["validation_result"]

    score = validation["compliance_score"]

    if score >= 80:
        status = "APPROVED"

    elif score >= 50:
        status = "REQUEST_INFO"

    else:
        status = "DENIED"

    decision = {
        "status": status,
        "compliance_score": score
    }

    logs = state.get("reasoning_logs", [])

    logs.append(
        f"[Decision Agent] Final decision: {status}"
    )

    state["final_decision"] = decision

    state["reasoning_logs"] = logs

    return state