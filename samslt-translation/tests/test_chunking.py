from samslt_translation.chunking import iter_chunks
def test_chunks(): assert len(list(iter_chunks(list(range(10)),4)))==3
