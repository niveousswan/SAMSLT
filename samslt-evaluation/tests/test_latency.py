from samslt_evaluation.latency import summarize_latency
def test_latency(): assert summarize_latency([1,2])["mean"]==1.5
