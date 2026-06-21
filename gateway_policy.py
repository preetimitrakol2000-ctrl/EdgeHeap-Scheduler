# Evaluates message payloads to parse systemic priority weights
def assess_priority_rank(event_label):
    if "CRITICAL" in event_label: return 10
    if "WARNING" in event_label: return 5
    return 1
