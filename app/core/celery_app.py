import os
from app.core.celery_app import celery_app
from app.services.pipeline import process_pipeline

# 0 spaces (touching the left margin)
@celery_app.task(name="tasks.process_prior_auth_document")
def process_prior_auth_document(file_path: str):
    # Exactly 4 spaces indent
    print(f"--- [CELERY WORKER] Starting processing for: {file_path} ---")
    
    try:
        # Exactly 8 spaces indent
        result = process_pipeline(file_path)
        print(f"--- [CELERY WORKER] Success! Result: {result} ---")
        return {"status": "Success", "result": result}
        
    except Exception as e:
        # Exactly 8 spaces indent
        print(f"--- [CELERY WORKER] Error occurred: {str(e)} ---")
        return {"status": "Failed", "error": str(e)}
        
    finally:
        # Exactly 8 spaces indent
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"--- [CELERY WORKER] Cleaned up file: {file_path} ---")