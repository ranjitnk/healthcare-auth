class EHRService:

    def update_status(self, patient_id, status):
        return {
            "patient_id": patient_id,
            "status": status
        }