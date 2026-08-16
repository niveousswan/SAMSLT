from samslt import SAMSLTPipeline
def test_describe():
    p=SAMSLTPipeline("es","en")
    assert p.describe()["target_language"]=="en"
