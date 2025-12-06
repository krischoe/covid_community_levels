from etl import transform

def test_summarize():
    out = transform.summarize()
    assert isinstance(out, dict)
    assert out["rows"] >= 0