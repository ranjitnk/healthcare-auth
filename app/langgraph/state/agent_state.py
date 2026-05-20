from typing import TypedDict, List

class AgentState(TypedDict):

    claim_text: str

    extracted_entities: dict

    retrieved_policy: str

    validation_result: dict

    final_decision: dict

    reasoning_logs: List[str]