def validation_agent(state):

    entities = state["extracted_entities"]

    policy = state["retrieved_policy"]

    missing = []

    if not entities.get("insurance_id"):
        missing.append("insurance_id")

    if "diagnosis" not in policy.lower():
        missing.append("diagnosis")

    compliance_score = 100 - (len(missing) * 30)

    result = {
        "missing_items": missing,
        "compliance_score": compliance_score
    }

    logs = state.get("reasoning_logs", [])

    logs.append(
        f"[Validation Agent] Compliance score: {compliance_score}"
    )

    state["validation_result"] = result

    state["reasoning_logs"] = logs

    return state