dashboard_metrics = {
    "processed": 0,
    "approved": 0,
    "rejected": 0
}

def update_dashboard_metrics(validation_result):

    dashboard_metrics["processed"] += 1

    if validation_result["approved"]:
        dashboard_metrics["approved"] += 1
    else:
        dashboard_metrics["rejected"] += 1

def get_dashboard_metrics():

    return dashboard_metrics