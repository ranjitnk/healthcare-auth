from app.langgraph.rag.vector_store import collection

def retrieve_policy(query):

    results = collection.query(
        query_texts=[query],
        n_results=1
    )

    documents = results["documents"][0]

    return documents[0] if documents else ""