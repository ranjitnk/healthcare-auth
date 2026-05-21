from app.services.llm.openai_client import client

def validation_agent(state):

    entities = state["extracted_entities"]

    policy = state["retrieved_policy"]

    prompt = f"""
    You are a healthcare insurance validation AI.

    Validate this healthcare claim.

    Claim Entities:
    {entities}

    Insurance Policy:
    {policy}

    Determine:

    1. Missing information
    2. Compliance score (0-100)
    3. Recommendation:
       - APPROVED
       - REQUEST_INFO
       - DENIED

    Return concise reasoning.
    """
    print("VALIDATION CLIENT:", client.base_url)
    response = client.chat.completions.create(

        model="gpt-4o",

        messages=[
            {
                "role": "system",
                "content": "You are a healthcare prior authorization validation agent."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    ai_reasoning = response.choices[0].message.content

    logs = state.get("reasoning_logs", [])

    logs.append(
        "[Validation Agent] GPT validation completed"
    )

    # Temporary structured output
    result = {

        "missing_items": [],

        "compliance_score": 95,

        "ai_reasoning": ai_reasoning
    }

    state["validation_result"] = result

    state["reasoning_logs"] = logs

    return state