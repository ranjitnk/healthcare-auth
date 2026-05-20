from app.services.llm.llm_service import extract_entities

def extraction_agent(state):

    text = state["claim_text"]

    entities = extract_entities(text)

    logs = state.get("reasoning_logs", [])

    logs.append(
        f"[Extraction Agent] Extracted entities: {entities}"
    )

    state["extracted_entities"] = entities

    state["reasoning_logs"] = logs

    return state