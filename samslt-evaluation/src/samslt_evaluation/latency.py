def summarize_latency(values):
    return {"count":len(values),"mean":sum(values)/len(values) if values else None,"max":max(values) if values else None}
